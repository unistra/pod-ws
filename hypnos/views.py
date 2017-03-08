# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.apps import apps


def home(request):
    models = apps.get_app_config("webservice").models
    html = "<html><body><h1>Pod-ws</h1>"
    for m in models.keys():
        html += '<div><a href="/webservice/{url}">{url}</a></div>'.format(url=m)
    html += "</body></html>"
    return HttpResponse(html)
