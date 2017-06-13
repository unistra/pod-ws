# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from .managers import PodsPodManager


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80, db_column='name')

    class Meta:
        managed = False
        db_table = 'auth_group'
        permissions = (('view_authgroup', 'Can view authgroup'),)


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, related_name='+', db_column='group_id')
    permission = models.ForeignKey('AuthPermission', related_name='+', db_column='permission_id')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        permissions = (('view_authgrouppermissions', 'Can view authgrouppermissions'),)
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    content_type = models.ForeignKey('DjangoContentType', related_name='+', db_column='content_type_id')
    codename = models.CharField(max_length=100, db_column='codename')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        permissions = (('view_authpermission', 'Can view authpermission'),)
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_column='password')
    last_login = models.DateTimeField(db_column='last_login', blank=True, null=True)
    is_superuser = models.BooleanField(db_column='is_superuser', default=False)
    username = models.CharField(unique=True, max_length=75, db_column='username')
    first_name = models.CharField(max_length=30, db_column='first_name')
    last_name = models.CharField(max_length=30, db_column='last_name')
    email = models.CharField(max_length=254, db_column='email')
    is_staff = models.BooleanField(db_column='is_staff', default=False)
    is_active = models.BooleanField(db_column='is_active', default=False)
    date_joined = models.DateTimeField(db_column='date_joined')

    class Meta:
        managed = False
        db_table = 'auth_user'
        permissions = (('view_authuser', 'Can view authuser'),)


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')
    group = models.ForeignKey(AuthGroup, related_name='+', db_column='group_id')

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        permissions = (('view_authusergroups', 'Can view authusergroups'),)
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')
    permission = models.ForeignKey(AuthPermission, related_name='+', db_column='permission_id')

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        permissions = (('view_authuseruserpermissions', 'Can view authuseruserpermissions'),)
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40, db_column='key')
    created = models.DateTimeField(db_column='created')
    user = models.OneToOneField(AuthUser, related_name='+', db_column='user_id')

    class Meta:
        managed = False
        db_table = 'authtoken_token'
        permissions = (('view_authtokentoken', 'Can view authtokentoken'),)


class CaptchaCaptchastore(models.Model):
    challenge = models.CharField(max_length=32, db_column='challenge')
    response = models.CharField(max_length=32, db_column='response')
    hashkey = models.CharField(unique=True, max_length=40, db_column='hashkey')
    expiration = models.DateTimeField(db_column='expiration')

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'
        permissions = (('view_captchacaptchastore', 'Can view captchacaptchastore'),)


class CoreContactus(models.Model):
    name = models.CharField(max_length=250, db_column='name')
    email = models.CharField(max_length=250, db_column='email')
    subject = models.CharField(max_length=250, db_column='subject')
    message = models.TextField(db_column='message')

    class Meta:
        managed = False
        db_table = 'core_contactus'
        permissions = (('view_corecontactus', 'Can view corecontactus'),)


class CoreEncodingtype(models.Model):
    name = models.CharField(max_length=250, db_column='name')
    bitrate_audio = models.CharField(max_length=250, db_column='bitrate_audio')
    bitrate_video = models.CharField(max_length=250, db_column='bitrate_video')
    output_height = models.IntegerField(db_column='output_height')
    mediatype = models.CharField(max_length=5, db_column='mediatype')

    class Meta:
        managed = False
        db_table = 'core_encodingtype'
        permissions = (('view_coreencodingtype', 'Can view coreencodingtype'),)


class CoreFilebrowse(models.Model):
    document = models.ForeignKey('FilerFile', related_name='+', db_column='document_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_filebrowse'
        permissions = (('view_corefilebrowse', 'Can view corefilebrowse'),)


class CorePagesmenubas(models.Model):
    order = models.SmallIntegerField(db_column='order', blank=True, null=True)
    page = models.ForeignKey('DjangoFlatpage', related_name='+', db_column='page_id')

    class Meta:
        managed = False
        db_table = 'core_pagesmenubas'
        permissions = (('view_corepagesmenubas', 'Can view corepagesmenubas'),)


class CoreUserprofile(models.Model):
    description = models.TextField(db_column='description')
    url = models.CharField(max_length=200, db_column='url')
    auth_type = models.CharField(max_length=20, db_column='auth_type')
    affiliation = models.CharField(max_length=50, db_column='affiliation')
    commentaire = models.TextField(db_column='commentaire')
    image = models.ForeignKey('FilerImage', related_name='+', db_column='image_id', blank=True, null=True)
    user = models.OneToOneField(AuthUser, related_name='+', db_column='user_id')

    class Meta:
        managed = False
        db_table = 'core_userprofile'
        permissions = (('view_coreuserprofile', 'Can view coreuserprofile'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField(db_column='action_time')
    object_id = models.TextField(db_column='object_id', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_column='object_repr')
    action_flag = models.SmallIntegerField(db_column='action_flag')
    change_message = models.TextField(db_column='change_message')
    content_type = models.ForeignKey('DjangoContentType', related_name='+', db_column='content_type_id', blank=True, null=True)
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')

    class Meta:
        managed = False
        db_table = 'django_admin_log'
        permissions = (('view_djangoadminlog', 'Can view djangoadminlog'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_column='app_label')
    model = models.CharField(max_length=100, db_column='model')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        permissions = (('view_djangocontenttype', 'Can view djangocontenttype'),)
        unique_together = (('app_label', 'model'),)


class DjangoFlatpage(models.Model):
    url = models.CharField(max_length=100, db_column='url')
    title = models.CharField(max_length=200, db_column='title')
    content = models.TextField(db_column='content')
    enable_comments = models.BooleanField(db_column='enable_comments', default=False)
    template_name = models.CharField(max_length=70, db_column='template_name')
    registration_required = models.BooleanField(db_column='registration_required', default=False)
    content_en = models.TextField(db_column='content_en', blank=True, null=True)
    content_fr = models.TextField(db_column='content_fr', blank=True, null=True)
    title_en = models.CharField(max_length=200, db_column='title_en', blank=True, null=True)
    title_fr = models.CharField(max_length=200, db_column='title_fr', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_flatpage'
        permissions = (('view_djangoflatpage', 'Can view djangoflatpage'),)


class DjangoFlatpageSites(models.Model):
    flatpage = models.ForeignKey(DjangoFlatpage, related_name='+', db_column='flatpage_id')
    site = models.ForeignKey('DjangoSite', related_name='+', db_column='site_id')

    class Meta:
        managed = False
        db_table = 'django_flatpage_sites'
        permissions = (('view_djangoflatpagesites', 'Can view djangoflatpagesites'),)
        unique_together = (('flatpage', 'site'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, db_column='app')
    name = models.CharField(max_length=255, db_column='name')
    applied = models.DateTimeField(db_column='applied')

    class Meta:
        managed = False
        db_table = 'django_migrations'
        permissions = (('view_djangomigrations', 'Can view djangomigrations'),)


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_column='session_key')
    session_data = models.TextField(db_column='session_data')
    expire_date = models.DateTimeField(db_column='expire_date')

    class Meta:
        managed = False
        db_table = 'django_session'
        permissions = (('view_djangosession', 'Can view djangosession'),)


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100, db_column='domain')
    name = models.CharField(max_length=50, db_column='name')

    class Meta:
        managed = False
        db_table = 'django_site'
        permissions = (('view_djangosite', 'Can view djangosite'),)


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40, db_column='storage_hash')
    name = models.CharField(max_length=255, db_column='name')
    modified = models.DateTimeField(db_column='modified')

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        permissions = (('view_easythumbnailssource', 'Can view easythumbnailssource'),)
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40, db_column='storage_hash')
    name = models.CharField(max_length=255, db_column='name')
    modified = models.DateTimeField(db_column='modified')
    source = models.ForeignKey(EasyThumbnailsSource, related_name='+', db_column='source_id')

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        permissions = (('view_easythumbnailsthumbnail', 'Can view easythumbnailsthumbnail'),)
        unique_together = (('storage_hash', 'name', 'source'),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.OneToOneField(EasyThumbnailsThumbnail, related_name='+', db_column='thumbnail_id')
    width = models.IntegerField(db_column='width', blank=True, null=True)
    height = models.IntegerField(db_column='height', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnaildimensions'
        permissions = (('view_easythumbnailsthumbnaildimensions', 'Can view easythumbnailsthumbnaildimensions'),)


class FilerClipboard(models.Model):
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')

    class Meta:
        managed = False
        db_table = 'filer_clipboard'
        permissions = (('view_filerclipboard', 'Can view filerclipboard'),)


class FilerClipboarditem(models.Model):
    clipboard = models.ForeignKey(FilerClipboard, related_name='+', db_column='clipboard_id')
    file = models.ForeignKey('FilerFile', related_name='+', db_column='file_id')

    class Meta:
        managed = False
        db_table = 'filer_clipboarditem'
        permissions = (('view_filerclipboarditem', 'Can view filerclipboarditem'),)


class FilerFile(models.Model):
    file = models.CharField(max_length=255, db_column='file', blank=True, null=True)
    field_file_size = models.IntegerField(db_column='_file_size', blank=True, null=True) # Field renamed because it started with '_'.
    sha1 = models.CharField(max_length=40, db_column='sha1')
    has_all_mandatory_data = models.BooleanField(db_column='has_all_mandatory_data', default=False)
    original_filename = models.CharField(max_length=255, db_column='original_filename', blank=True, null=True)
    name = models.CharField(max_length=255, db_column='name')
    description = models.TextField(db_column='description', blank=True, null=True)
    uploaded_at = models.DateTimeField(db_column='uploaded_at')
    modified_at = models.DateTimeField(db_column='modified_at')
    is_public = models.BooleanField(db_column='is_public', default=False)
    folder = models.ForeignKey('FilerFolder', related_name='+', db_column='folder_id', blank=True, null=True)
    owner = models.ForeignKey(AuthUser, related_name='+', db_column='owner_id', blank=True, null=True)
    polymorphic_ctype = models.ForeignKey(DjangoContentType, related_name='+', db_column='polymorphic_ctype_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_file'
        permissions = (('view_filerfile', 'Can view filerfile'),)


class FilerFolder(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    uploaded_at = models.DateTimeField(db_column='uploaded_at')
    created_at = models.DateTimeField(db_column='created_at')
    modified_at = models.DateTimeField(db_column='modified_at')
    lft = models.IntegerField(db_column='lft')
    rght = models.IntegerField(db_column='rght')
    tree_id = models.IntegerField(db_column='tree_id')
    level = models.IntegerField(db_column='level')
    owner = models.ForeignKey(AuthUser, related_name='+', db_column='owner_id', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='+', db_column='parent_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folder'
        permissions = (('view_filerfolder', 'Can view filerfolder'),)
        unique_together = (('parent', 'name'),)


class FilerFolderpermission(models.Model):
    type = models.SmallIntegerField(db_column='type')
    everybody = models.BooleanField(db_column='everybody', default=False)
    can_edit = models.SmallIntegerField(db_column='can_edit', blank=True, null=True)
    can_read = models.SmallIntegerField(db_column='can_read', blank=True, null=True)
    can_add_children = models.SmallIntegerField(db_column='can_add_children', blank=True, null=True)
    folder = models.ForeignKey(FilerFolder, related_name='+', db_column='folder_id', blank=True, null=True)
    group = models.ForeignKey(AuthGroup, related_name='+', db_column='group_id', blank=True, null=True)
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folderpermission'
        permissions = (('view_filerfolderpermission', 'Can view filerfolderpermission'),)


class FilerImage(models.Model):
    file_ptr = models.OneToOneField(FilerFile, primary_key=True, related_name='+', db_column='file_ptr_id')
    field_height = models.IntegerField(db_column='_height', blank=True, null=True) # Field renamed because it started with '_'.
    field_width = models.IntegerField(db_column='_width', blank=True, null=True) # Field renamed because it started with '_'.
    date_taken = models.DateTimeField(db_column='date_taken', blank=True, null=True)
    default_alt_text = models.CharField(max_length=255, db_column='default_alt_text', blank=True, null=True)
    default_caption = models.CharField(max_length=255, db_column='default_caption', blank=True, null=True)
    author = models.CharField(max_length=255, db_column='author', blank=True, null=True)
    must_always_publish_author_credit = models.BooleanField(db_column='must_always_publish_author_credit', default=False)
    must_always_publish_copyright = models.BooleanField(db_column='must_always_publish_copyright', default=False)
    subject_location = models.CharField(max_length=64, db_column='subject_location', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_image'
        permissions = (('view_filerimage', 'Can view filerimage'),)


class PodsBuilding(models.Model):
    name = models.CharField(unique=True, max_length=200, db_column='name')
    image = models.ForeignKey(FilerImage, related_name='+', db_column='image_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pods_building'
        permissions = (('view_podsbuilding', 'Can view podsbuilding'),)


class PodsChannel(models.Model):
    title = models.CharField(unique=True, max_length=100, db_column='title')
    title_fr = models.CharField(unique=True, max_length=100, db_column='title_fr', blank=True, null=True)
    title_en = models.CharField(unique=True, max_length=100, db_column='title_en', blank=True, null=True)
    slug = models.CharField(unique=True, max_length=100, db_column='slug')
    description = models.TextField(db_column='description')
    color = models.CharField(max_length=10, db_column='color', blank=True, null=True)
    style = models.TextField(db_column='style', blank=True, null=True)
    visible = models.BooleanField(db_column='visible', default=False)
    headband = models.ForeignKey(FilerImage, related_name='+', db_column='headband_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pods_channel'
        permissions = (('view_podschannel', 'Can view podschannel'),)


class PodsChannelOwners(models.Model):
    channel = models.ForeignKey(PodsChannel, related_name='+', db_column='channel_id')
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')

    class Meta:
        managed = False
        db_table = 'pods_channel_owners'
        permissions = (('view_podschannelowners', 'Can view podschannelowners'),)
        unique_together = (('channel', 'user'),)


class PodsChannelUsers(models.Model):
    channel = models.ForeignKey(PodsChannel, related_name='+', db_column='channel_id')
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')

    class Meta:
        managed = False
        db_table = 'pods_channel_users'
        permissions = (('view_podschannelusers', 'Can view podschannelusers'),)
        unique_together = (('channel', 'user'),)


class PodsChapterpods(models.Model):
    title = models.CharField(max_length=100, db_column='title')
    slug = models.CharField(unique=True, max_length=105, db_column='slug')
    time = models.IntegerField(db_column='time')
    video = models.ForeignKey('PodsPod', db_column='video_id')

    class Meta:
        managed = False
        db_table = 'pods_chapterpods'
        permissions = (('view_podschapterpods', 'Can view podschapterpods'),)


class PodsContributorpods(models.Model):
    name = models.CharField(max_length=200, db_column='name')
    email_address = models.CharField(max_length=254, db_column='email_address', blank=True, null=True)
    role = models.CharField(max_length=200, db_column='role')
    weblink = models.CharField(max_length=200, db_column='weblink', blank=True, null=True)
    video = models.ForeignKey('PodsPod', db_column='video_id')

    class Meta:
        managed = False
        db_table = 'pods_contributorpods'
        permissions = (('view_podscontributorpods', 'Can view podscontributorpods'),)


class PodsDiscipline(models.Model):
    title = models.CharField(unique=True, max_length=100, db_column='title')
    title_fr = models.CharField(unique=True, max_length=100, db_column='title_fr', blank=True, null=True)
    title_en = models.CharField(unique=True, max_length=100, db_column='title_en', blank=True, null=True)
    slug = models.CharField(unique=True, max_length=100, db_column='slug')
    description = models.TextField(db_column='description', blank=True, null=True)
    headband = models.ForeignKey(FilerImage, related_name='+', db_column='headband_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pods_discipline'
        permissions = (('view_podsdiscipline', 'Can view podsdiscipline'),)


class PodsDocpods(models.Model):
    document = models.ForeignKey(FilerFile, related_name='+', db_column='document_id', blank=True, null=True)
    video = models.ForeignKey('PodsPod', db_column='video_id')

    class Meta:
        managed = False
        db_table = 'pods_docpods'
        permissions = (('view_podsdocpods', 'Can view podsdocpods'),)


class PodsEncodingpods(models.Model):
    encodingfile = models.CharField(db_column='encodingFile', max_length=255, blank=True, null=True) # Field name made lowercase.
    encodingformat = models.CharField(db_column='encodingFormat', max_length=12) # Field name made lowercase.
    encodingtype = models.ForeignKey(CoreEncodingtype, db_column='encodingType_id', related_name='+') # Field name made lowercase.
    video = models.ForeignKey('PodsPod', db_column='video_id')

    class Meta:
        managed = False
        db_table = 'pods_encodingpods'
        permissions = (('view_podsencodingpods', 'Can view podsencodingpods'),)


class PodsEnrichpods(models.Model):
    title = models.CharField(max_length=100, db_column='title')
    slug = models.CharField(unique=True, max_length=105, db_column='slug')
    stop_video = models.BooleanField(db_column='stop_video', default=False)
    start = models.IntegerField(db_column='start')
    end = models.IntegerField(db_column='end')
    type = models.CharField(max_length=10, db_column='type', blank=True, null=True)
    richtext = models.TextField(db_column='richtext')
    weblink = models.CharField(max_length=200, db_column='weblink', blank=True, null=True)
    embed = models.TextField(db_column='embed', blank=True, null=True)
    document = models.ForeignKey(FilerFile, related_name='+', db_column='document_id', blank=True, null=True)
    image = models.ForeignKey(FilerImage, related_name='+', db_column='image_id', blank=True, null=True)
    video = models.ForeignKey('PodsPod', db_column='video_id')

    class Meta:
        managed = False
        db_table = 'pods_enrichpods'
        permissions = (('view_podsenrichpods', 'Can view podsenrichpods'),)


class PodsFavorites(models.Model):
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')
    video = models.ForeignKey('PodsPod', related_name='+', db_column='video_id')

    class Meta:
        managed = False
        db_table = 'pods_favorites'
        permissions = (('view_podsfavorites', 'Can view podsfavorites'),)


class PodsMediacourses(models.Model):
    title = models.CharField(max_length=200, db_column='title')
    date_added = models.DateTimeField(db_column='date_added')
    mediapath = models.CharField(unique=True, max_length=250, db_column='mediapath')
    started = models.BooleanField(db_column='started', default=False)
    error = models.TextField(db_column='error', blank=True, null=True)
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')

    class Meta:
        managed = False
        db_table = 'pods_mediacourses'
        permissions = (('view_podsmediacourses', 'Can view podsmediacourses'),)


class PodsNotes(models.Model):
    note = models.TextField(db_column='note', blank=True, null=True)
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')
    video = models.ForeignKey('PodsPod', related_name='+', db_column='video_id')

    class Meta:
        managed = False
        db_table = 'pods_notes'
        permissions = (('view_podsnotes', 'Can view podsnotes'),)


class PodsPod(models.Model):
    video = models.CharField(max_length=255, db_column='video')
    allow_downloading = models.BooleanField(db_column='allow_downloading', default=False)
    title = models.CharField(max_length=250, db_column='title')
    slug = models.CharField(unique=True, max_length=255, db_column='slug')
    date_added = models.DateField(db_column='date_added')
    date_evt = models.DateField(db_column='date_evt', blank=True, null=True)
    description = models.TextField(db_column='description')
    view_count = models.IntegerField(db_column='view_count')
    encoding_in_progress = models.BooleanField(db_column='encoding_in_progress', default=False)
    encoding_status = models.CharField(max_length=250, db_column='encoding_status', blank=True, null=True)
    to_encode = models.BooleanField(db_column='to_encode', default=False)
    overview = models.CharField(max_length=255, db_column='overview', blank=True, null=True)
    duration = models.IntegerField(db_column='duration')
    infovideo = models.TextField(db_column='infoVideo', blank=True, null=True) # Field name made lowercase.
    is_draft = models.BooleanField(db_column='is_draft', default=False)
    is_restricted = models.BooleanField(db_column='is_restricted', default=False)
    password = models.CharField(max_length=50, db_column='password', blank=True, null=True)
    owner = models.ForeignKey(AuthUser, related_name='+', db_column='owner_id')
    thumbnail = models.ForeignKey(FilerImage, related_name='+', db_column='thumbnail_id', blank=True, null=True)
    type = models.ForeignKey('PodsType', related_name='+', db_column='type_id')
    cursus = models.CharField(max_length=1, db_column='cursus')
    main_lang = models.CharField(max_length=2, db_column='main_lang')
    is_360 = models.BooleanField(db_column='is_360', default=False)

    objects = PodsPodManager()

    @property
    def tags(self):
        """ special case for tags """
        try:
            dct = DjangoContentType.objects.get(app_label="pods", model="pod")
            tti = TaggitTaggeditem.objects.filter(object_id=self.id, content_type=dct)
            tags = [i.tag.name for i in tti]
        except:
            tags = []
        finally:
            return tags

    @property
    def pod_media_url(self):
        return getattr(settings, "POD_MEDIA_URL", "")


    class Meta:
        managed = False
        db_table = 'pods_pod'
        permissions = (('view_podspod', 'Can view podspod'),)


class PodsPodChannel(models.Model):
    pod = models.ForeignKey(PodsPod, db_column='pod_id')
    channel = models.ForeignKey(PodsChannel, related_name='+', db_column='channel_id')

    class Meta:
        managed = False
        db_table = 'pods_pod_channel'
        permissions = (('view_podspodchannel', 'Can view podspodchannel'),)
        unique_together = (('pod', 'channel'),)


class PodsPodDiscipline(models.Model):
    pod = models.ForeignKey(PodsPod, db_column='pod_id')
    discipline = models.ForeignKey(PodsDiscipline, related_name='+', db_column='discipline_id')

    class Meta:
        managed = False
        db_table = 'pods_pod_discipline'
        permissions = (('view_podspoddiscipline', 'Can view podspoddiscipline'),)
        unique_together = (('pod', 'discipline'),)


class PodsPodTheme(models.Model):
    pod = models.ForeignKey(PodsPod, db_column='pod_id')
    theme = models.ForeignKey('PodsTheme', related_name='+', db_column='theme_id')

    class Meta:
        managed = False
        db_table = 'pods_pod_theme'
        permissions = (('view_podspodtheme', 'Can view podspodtheme'),)
        unique_together = (('pod', 'theme'),)


class PodsRecorder(models.Model):
    name = models.CharField(unique=True, max_length=200, db_column='name')
    adress_ip = models.GenericIPAddressField(unique=True, db_column='adress_ip')
    status = models.BooleanField(db_column='status', default=False)
    slide = models.BooleanField(db_column='slide', default=False)
    gmapurl = models.CharField(max_length=250, db_column='gmapurl', blank=True, null=True)
    is_restricted = models.BooleanField(db_column='is_restricted', default=False)
    building = models.ForeignKey(PodsBuilding, related_name='+', db_column='building_id')
    image = models.ForeignKey(FilerImage, related_name='+', db_column='image_id', blank=True, null=True)
    description = models.TextField(db_column='description')

    class Meta:
        managed = False
        db_table = 'pods_recorder'
        permissions = (('view_podsrecorder', 'Can view podsrecorder'),)


class PodsReportvideo(models.Model):
    comment = models.TextField(db_column='comment', blank=True, null=True)
    date_added = models.DateTimeField(db_column='date_added')
    user = models.ForeignKey(AuthUser, related_name='+', db_column='user_id')
    video = models.ForeignKey(PodsPod, related_name='+', db_column='video_id')
    answer = models.TextField(db_column='answer', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pods_reportvideo'
        permissions = (('view_podsreportvideo', 'Can view podsreportvideo'),)
        unique_together = (('video', 'user'),)


class PodsTheme(models.Model):
    title = models.CharField(unique=True, max_length=100, db_column='title')
    slug = models.CharField(unique=True, max_length=100, db_column='slug')
    description = models.TextField(db_column='description', blank=True, null=True)
    channel = models.ForeignKey(PodsChannel, related_name='+', db_column='channel_id')
    headband = models.ForeignKey(FilerImage, related_name='+', db_column='headband_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pods_theme'
        permissions = (('view_podstheme', 'Can view podstheme'),)


class PodsTrackpods(models.Model):
    kind = models.CharField(max_length=10, db_column='kind')
    lang = models.CharField(max_length=2, db_column='lang')
    src = models.ForeignKey(FilerFile, related_name='+', db_column='src_id', blank=True, null=True)
    video = models.ForeignKey(PodsPod, db_column='video_id')

    class Meta:
        managed = False
        db_table = 'pods_trackpods'
        permissions = (('view_podstrackpods', 'Can view podstrackpods'),)


class PodsType(models.Model):
    title = models.CharField(unique=True, max_length=100, db_column='title')
    title_fr = models.CharField(unique=True, max_length=100, db_column='title_fr', blank=True, null=True)
    title_en = models.CharField(unique=True, max_length=100, db_column='title_en', blank=True, null=True)
    slug = models.CharField(unique=True, max_length=100, db_column='slug')
    description = models.TextField(db_column='description', blank=True, null=True)
    headband = models.ForeignKey(FilerImage, related_name='+', db_column='headband_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pods_type'
        permissions = (('view_podstype', 'Can view podstype'),)


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100, db_column='name')
    slug = models.CharField(unique=True, max_length=100, db_column='slug')

    class Meta:
        managed = False
        db_table = 'taggit_tag'
        permissions = (('view_taggittag', 'Can view taggittag'),)


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField(db_column='object_id')
    content_type = models.ForeignKey(DjangoContentType, related_name='+', db_column='content_type_id')
    tag = models.ForeignKey(TaggitTag, related_name='+', db_column='tag_id')

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        permissions = (('view_taggittaggeditem', 'Can view taggittaggeditem'),)


class TaggitTemplatetagsAmodel(models.Model):
    name = models.CharField(max_length=50, db_column='name')

    class Meta:
        managed = False
        db_table = 'taggit_templatetags_amodel'
        permissions = (('view_taggittemplatetagsamodel', 'Can view taggittemplatetagsamodel'),)
