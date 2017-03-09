# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.

import django_filters
from . import models
from rest_framework.exceptions import APIException


class CustomFilterSet(django_filters.FilterSet):
    def custom_check_fields(self):
        data_keys = set([name for name, value in self.data.items()])
        fields_keys = set([name for name, value in self.filters.items()])
        fields_keys.add("format")
        if not data_keys.issubset(fields_keys):
            raise APIException("A filter is wrong")

    def __init__(self, data=None, queryset=None, prefix=None, strict=None):
        super(CustomFilterSet, self).__init__(data=data, queryset=queryset,
            prefix=prefix, strict=strict)
        self.custom_check_fields()


class AuthGroupListFilter(CustomFilterSet):
    class Meta:
        model = models.AuthGroup

class AuthGroupPermissionsListFilter(CustomFilterSet):
    class Meta:
        model = models.AuthGroupPermissions

class AuthPermissionListFilter(CustomFilterSet):
    class Meta:
        model = models.AuthPermission

class AuthUserListFilter(CustomFilterSet):
    class Meta:
        model = models.AuthUser

class AuthUserGroupsListFilter(CustomFilterSet):
    class Meta:
        model = models.AuthUserGroups

class AuthUserUserPermissionsListFilter(CustomFilterSet):
    class Meta:
        model = models.AuthUserUserPermissions

class AuthtokenTokenListFilter(CustomFilterSet):
    class Meta:
        model = models.AuthtokenToken

class CaptchaCaptchastoreListFilter(CustomFilterSet):
    class Meta:
        model = models.CaptchaCaptchastore

class CoreContactusListFilter(CustomFilterSet):
    class Meta:
        model = models.CoreContactus

class CoreEncodingtypeListFilter(CustomFilterSet):
    class Meta:
        model = models.CoreEncodingtype

class CoreFilebrowseListFilter(CustomFilterSet):
    class Meta:
        model = models.CoreFilebrowse

class CorePagesmenubasListFilter(CustomFilterSet):
    class Meta:
        model = models.CorePagesmenubas

class CoreUserprofileListFilter(CustomFilterSet):
    class Meta:
        model = models.CoreUserprofile

class DjangoAdminLogListFilter(CustomFilterSet):
    class Meta:
        model = models.DjangoAdminLog

class DjangoContentTypeListFilter(CustomFilterSet):
    class Meta:
        model = models.DjangoContentType

class DjangoFlatpageListFilter(CustomFilterSet):
    class Meta:
        model = models.DjangoFlatpage

class DjangoFlatpageSitesListFilter(CustomFilterSet):
    class Meta:
        model = models.DjangoFlatpageSites

class DjangoMigrationsListFilter(CustomFilterSet):
    class Meta:
        model = models.DjangoMigrations

class DjangoSessionListFilter(CustomFilterSet):
    class Meta:
        model = models.DjangoSession

class DjangoSiteListFilter(CustomFilterSet):
    class Meta:
        model = models.DjangoSite

class EasyThumbnailsSourceListFilter(CustomFilterSet):
    class Meta:
        model = models.EasyThumbnailsSource

class EasyThumbnailsThumbnailListFilter(CustomFilterSet):
    class Meta:
        model = models.EasyThumbnailsThumbnail

class EasyThumbnailsThumbnaildimensionsListFilter(CustomFilterSet):
    class Meta:
        model = models.EasyThumbnailsThumbnaildimensions

class FilerClipboardListFilter(CustomFilterSet):
    class Meta:
        model = models.FilerClipboard

class FilerClipboarditemListFilter(CustomFilterSet):
    class Meta:
        model = models.FilerClipboarditem

class FilerFileListFilter(CustomFilterSet):
    class Meta:
        model = models.FilerFile

class FilerFolderListFilter(CustomFilterSet):
    class Meta:
        model = models.FilerFolder

class FilerFolderpermissionListFilter(CustomFilterSet):
    class Meta:
        model = models.FilerFolderpermission

class FilerImageListFilter(CustomFilterSet):
    class Meta:
        model = models.FilerImage

class PodsBuildingListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsBuilding

class PodsChannelListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsChannel

class PodsChannelOwnersListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsChannelOwners

class PodsChannelUsersListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsChannelUsers

class PodsChapterpodsListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsChapterpods

class PodsContributorpodsListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsContributorpods

class PodsDisciplineListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsDiscipline

class PodsDocpodsListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsDocpods

class PodsEncodingpodsListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsEncodingpods

class PodsEnrichpodsListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsEnrichpods

class PodsFavoritesListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsFavorites

class PodsMediacoursesListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsMediacourses

class PodsNotesListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsNotes

class PodsPodListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsPod

class PodsPodChannelListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsPodChannel

class PodsPodDisciplineListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsPodDiscipline

class PodsPodThemeListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsPodTheme

class PodsRecorderListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsRecorder

class PodsReportvideoListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsReportvideo

class PodsThemeListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsTheme

class PodsTrackpodsListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsTrackpods

class PodsTypeListFilter(CustomFilterSet):
    class Meta:
        model = models.PodsType

class TaggitTagListFilter(CustomFilterSet):
    class Meta:
        model = models.TaggitTag

class TaggitTaggeditemListFilter(CustomFilterSet):
    class Meta:
        model = models.TaggitTaggeditem

class TaggitTemplatetagsAmodelListFilter(CustomFilterSet):
    class Meta:
        model = models.TaggitTemplatetagsAmodel
