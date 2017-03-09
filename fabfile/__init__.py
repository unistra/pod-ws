# -*- coding: utf-8 -*-

"""
"""

from fabric.api import (env, roles, execute, task, sudo, warn_only)
from os.path import join
import fabtools
import pydiploy
from fabric.operations import put
from .uwsgi import install_uwsgi, uwsgi_restart, app_uwsgi_conf


# edit config here !

env.user = 'root'  # user for ssh

env.remote_owner = 'django'  # remote server user
env.remote_group = 'di'  # remote server group

env.application_name = 'pod-ws'
env.root_package_name = 'hypnos'

env.remote_home = '/home/django'
env.remote_python_version = '2.7'
env.remote_virtualenv_root = join(env.remote_home, '.virtualenvs')
env.remote_virtualenv_dir = join(env.remote_virtualenv_root,
                                 env.application_name)
env.remote_repo_url = '.'  # git repository url
env.local_tmp_dir = '/tmp'
env.remote_static_root = '/var/www/restapis/'
env.locale = 'fr_FR.UTF-8'  # locale to use on remote
env.timezone = 'Europe/Paris'  # timezone for remote
env.keep_releases = 2  # number of old releases to keep before cleaning


@task
def test():
    env.user = 'root'
    env.roledefs = {
        'web': ['podcast-test.di.unistra.fr'],
        'lb': ['podcast-test.di.unistra.fr']
    }
    env.backends = ['127.0.0.1']
    env.server_name = 'pod-ws-test.u-strasbg.fr'
    env.short_server_name = 'pod-ws-test'
    env.server_ip = ''
    env.server_ssl_on = True
    env.nginx_location_extra_directives = [
        'client_max_body_size 4G', 'proxy_request_buffering off', 'proxy_connect_timeout 1800',
        'proxy_send_timeout 1800', 'proxy_read_timeout 1800', 'send_timeout 1800'
    ]
    env.goal = 'test'
    env.path_to_cert = '/etc/ssl/certs/wildcard.u-strasbg.fr.pem'
    env.path_to_cert_key = '/etc/ssl/private/wildcard.u-strasbg.fr.key'
    env.socket_port = '8001'
    env.socket_host = '127.0.0.1'
    env.static_folder = '/site_media/'
    env.map_settings = {
        'webservice_name': "DATABASES['webservice']['NAME']",
        'webservice_user': "DATABASES['webservice']['USER']",
        'webservice_password': "DATABASES['webservice']['PASSWORD']",
        'webservice_port': "DATABASES['webservice']['PORT']",
        'webservice_host': "DATABASES['webservice']['HOST']",
        'webservice_engine': "DATABASES['webservice']['ENGINE']"
    }
    execute(build_env)



# dont touch after that point if you don't know what you are doing !


@task
def tag(version_number):
    """ Set the version to deploy to `version_number`. """
    execute(pydiploy.prepare.tag, version=version_number)


@roles(['web', 'lb'])
def build_env():
    execute(pydiploy.prepare.build_env)


@task
def pre_install():
    """Pre install of backend & frontend"""
    execute(pre_install_backend)
    execute(pre_install_frontend)


@roles('web')
@task
def pre_install_backend(commands='/usr/bin/rsync', update_uwsgi=False):
    """ Installs requirements for uwsgi & virtualenv env """
    execute(pydiploy.require.system.add_user, commands=commands)
    execute(pydiploy.require.system.set_locale)
    execute(pydiploy.require.system.set_timezone)
    execute(pydiploy.require.system.update_pkg_index)
    execute(pydiploy.django.application_packages)
    # execute(pydiploy.require.circus.circus_pkg, update=upgrade_circus)
    execute(pydiploy.require.python.virtualenv.virtualenv)
    # execute(pydiploy.require.circus.upstart)
    execute(install_uwsgi, update=update_uwsgi)


@roles('lb')
@task
def pre_install_frontend():
    """Setup server for frontend"""
    execute(pydiploy.django.pre_install_frontend)


@task
def deploy(update_pkg=False):
    """Deploy code on server"""
    execute(deploy_backend, update_pkg)
    execute(deploy_frontend)


@roles('web')
@task
def deploy_backend(update_pkg=False, **kwargs):
    """Deploy code on server"""
    with pydiploy.django.wrap_deploy():
        execute(pydiploy.require.releases_manager.setup)
        execute(pydiploy.require.releases_manager.deploy_code)
        execute(pydiploy.require.django.utils.deploy_manage_file)
        execute(pydiploy.require.django.utils.deploy_wsgi_file)
        execute(
            pydiploy.require.python.utils.application_dependencies,
            update_pkg)
        execute(pydiploy.require.django.utils.app_settings, **kwargs)
        execute(pydiploy.require.django.command.django_prepare)
        execute(pydiploy.require.system.permissions)
        # execute(pydiploy.require.circus.app_reload)
        execute(uwsgi_restart)
        execute(pydiploy.require.releases_manager.cleanup)


@roles('lb')
@task
def deploy_frontend():
    """Deploy static files on load balancer"""
    execute(pydiploy.django.deploy_frontend)


@roles('web')
@task
def rollback():
    """ Rolls back django webapp """
    execute(pydiploy.require.releases_manager.rollback_code)
    # execute(pydiploy.require.circus.app_reload)
    execute(uwsgi_restart)


@task
def post_install():
    """post install for backend & frontend"""
    execute(post_install_backend)
    execute(post_install_frontend)


@roles('web')
@task
def post_install_backend():
    """ Post-installation of webapp"""
    #execute(pydiploy.require.circus.app_circus_conf)
    execute(app_uwsgi_conf)
    # execute(pydiploy.require.circus.app_reload)
    execute(uwsgi_restart)


@roles('lb')
@task
def post_install_frontend():
    """Post installation of frontend"""
    #execute(pydiploy.django.post_install_frontend)
    execute(pydiploy.require.nginx.web_configuration)
    execute(pydiploy.require.nginx.nginx_restart)


@roles('web')
@task
def install_postgres(user=None, dbname=None, password=None):
    """Install Postgres on remote"""
    execute(pydiploy.django.install_postgres_server,
            user=user, dbname=dbname, password=password)


@task
def reload():
    """Reload backend & frontend"""
    execute(reload_frontend)
    execute(reload_backend)


@roles('lb')
@task
def reload_frontend():
    execute(pydiploy.django.reload_frontend)


@roles('web')
@task
def reload_backend():
    """ Reloads backend """
    execute(uwsgi_restart)


@roles('lb')
@task
def set_down():
    """ Set app to maintenance mode """
    execute(pydiploy.django.set_app_down)


@roles('lb')
@task
def set_up():
    """ Set app to up mode """
    execute(pydiploy.django.set_app_up)


@roles('web')
@task
def custom_manage_cmd(cmd):
    """ Execute custom command in manage.py """
    execute(pydiploy.django.custom_manage_command, cmd)
