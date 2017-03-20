# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.

from rest_framework import serializers
from rest_framework_fine_permissions.fields import ModelPermissionsField
from rest_framework_fine_permissions.serializers import ModelPermissionsSerializer
from . import models

class AuthGroupSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.AuthGroup

class AuthGroupPermissionsSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.AuthGroupPermissions

class AuthPermissionSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.AuthPermission

class AuthUserSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.AuthUser

class AuthUserGroupsSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.AuthUserGroups

class AuthUserUserPermissionsSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.AuthUserUserPermissions

class AuthtokenTokenSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.AuthtokenToken

class CaptchaCaptchastoreSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.CaptchaCaptchastore

class CoreContactusSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.CoreContactus

class CoreEncodingtypeSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.CoreEncodingtype

class CoreFilebrowseSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.CoreFilebrowse

class CorePagesmenubasSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.CorePagesmenubas

class CoreUserprofileSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.CoreUserprofile

class DjangoAdminLogSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.DjangoAdminLog

class DjangoContentTypeSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.DjangoContentType

class DjangoFlatpageSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.DjangoFlatpage

class DjangoFlatpageSitesSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.DjangoFlatpageSites

class DjangoMigrationsSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.DjangoMigrations

class DjangoSessionSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.DjangoSession

class DjangoSiteSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.DjangoSite

class EasyThumbnailsSourceSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.EasyThumbnailsSource

class EasyThumbnailsThumbnailSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.EasyThumbnailsThumbnail

class EasyThumbnailsThumbnaildimensionsSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.EasyThumbnailsThumbnaildimensions

class FilerClipboardSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.FilerClipboard

class FilerClipboarditemSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.FilerClipboarditem

class FilerFileSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.FilerFile

class FilerFolderSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.FilerFolder

class FilerFolderpermissionSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.FilerFolderpermission

class FilerImageSerializer(ModelPermissionsSerializer):
    file_ptr = ModelPermissionsField('webservice.FilerFileSerializer')

    class Meta:
        model = models.FilerImage

class PodsBuildingSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsBuilding

class PodsChannelSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsChannel

class PodsChannelOwnersSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsChannelOwners

class PodsChannelUsersSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsChannelUsers

class PodsChapterpodsSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsChapterpods

class PodsContributorpodsSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsContributorpods

class PodsDisciplineSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsDiscipline

class PodsFavoritesSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsFavorites

class PodsMediacoursesSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsMediacourses

class PodsNotesSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsNotes

class PodsRecorderSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsRecorder

class PodsReportvideoSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsReportvideo

class PodsThemeSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsTheme

class PodsTypeSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.PodsType

class TaggitTagSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.TaggitTag

class TaggitTaggeditemSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.TaggitTaggeditem

class TaggitTemplatetagsAmodelSerializer(ModelPermissionsSerializer):
    class Meta:
        model = models.TaggitTemplatetagsAmodel


##############
# Customized #
##############

class PodsEncodingpodsSerializer(ModelPermissionsSerializer):
    encodingtype = ModelPermissionsField('webservice.CoreEncodingtypeSerializer')

    class Meta:
        model = models.PodsEncodingpods


class PodsEnrichpodsSerializer(ModelPermissionsSerializer):
    document = ModelPermissionsField('webservice.FilerFileSerializer')

    class Meta:
        model = models.PodsEnrichpods


class PodsDocpodsSerializer(ModelPermissionsSerializer):
    document = ModelPermissionsField('webservice.FilerFileSerializer')

    class Meta:
        model = models.PodsDocpods


class PodsPodDisciplineSerializer(ModelPermissionsSerializer):
    discipline = ModelPermissionsField('webservice.PodsDisciplineSerializer')

    class Meta:
        model = models.PodsPodDiscipline


class PodsPodChannelSerializer(ModelPermissionsSerializer):
    channel = ModelPermissionsField('webservice.PodsChannelSerializer')

    class Meta:
        model = models.PodsPodChannel


class PodsPodThemeSerializer(ModelPermissionsSerializer):
    theme = ModelPermissionsField('webservice.PodsThemeSerializer')

    class Meta:
        model = models.PodsPodTheme


class PodsTrackpodsSerializer(ModelPermissionsSerializer):
    src = ModelPermissionsField('webservice.FilerFileSerializer')

    class Meta:
        model = models.PodsTrackpods


class PodsPodSerializer(ModelPermissionsSerializer):
    owner = ModelPermissionsField('webservice.AuthUserSerializer')
    type = ModelPermissionsField('webservice.PodsTypeSerializer')
    thumbnail = ModelPermissionsField('webservice.FilerImageSerializer')
    podsdocpods_set = ModelPermissionsField('webservice.PodsDocpodsSerializer')
    podsenrichpods_set = ModelPermissionsField('webservice.PodsEnrichpodsSerializer')
    podsencodingpods_set = ModelPermissionsField('webservice.PodsEncodingpodsSerializer')
    podscontributorpods_set = ModelPermissionsField('webservice.PodsContributorpodsSerializer')
    podspoddiscipline_set = ModelPermissionsField('webservice.PodsPodDisciplineSerializer')
    podspodchannel_set = ModelPermissionsField('webservice.PodsPodChannelSerializer')
    podspodtheme_set = ModelPermissionsField('webservice.PodsPodThemeSerializer')
    podstrackpods_set = ModelPermissionsField('webservice.PodsTrackpodsSerializer')
    podschapterpods_set = ModelPermissionsField('webservice.PodsChapterpodsSerializer')
    tags = serializers.ListField()

    class Meta:
        model = models.PodsPod
