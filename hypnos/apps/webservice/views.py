# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.

import re
from rest_framework_fine_permissions.serializers import ModelPermissionsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from . import models
from . import serializers
from . import filters
from . import renderers
from . import permissions


class AuthGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AuthGroup.objects.all()
    serializer_class = serializers.AuthGroupSerializer

class AuthGroupList(generics.ListCreateAPIView):
    queryset = models.AuthGroup.objects.all()
    serializer_class = serializers.AuthGroupSerializer
    filter_class = filters.AuthGroupListFilter

class AuthGroupPermissionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AuthGroupPermissions.objects.all()
    serializer_class = serializers.AuthGroupPermissionsSerializer

class AuthGroupPermissionsList(generics.ListCreateAPIView):
    queryset = models.AuthGroupPermissions.objects.all()
    serializer_class = serializers.AuthGroupPermissionsSerializer
    filter_class = filters.AuthGroupPermissionsListFilter

class AuthPermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AuthPermission.objects.all()
    serializer_class = serializers.AuthPermissionSerializer

class AuthPermissionList(generics.ListCreateAPIView):
    queryset = models.AuthPermission.objects.all()
    serializer_class = serializers.AuthPermissionSerializer
    filter_class = filters.AuthPermissionListFilter

class AuthUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AuthUser.objects.all()
    serializer_class = serializers.AuthUserSerializer

class AuthUserList(generics.ListCreateAPIView):
    queryset = models.AuthUser.objects.all()
    serializer_class = serializers.AuthUserSerializer
    filter_class = filters.AuthUserListFilter

class AuthUserGroupsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AuthUserGroups.objects.all()
    serializer_class = serializers.AuthUserGroupsSerializer

class AuthUserGroupsList(generics.ListCreateAPIView):
    queryset = models.AuthUserGroups.objects.all()
    serializer_class = serializers.AuthUserGroupsSerializer
    filter_class = filters.AuthUserGroupsListFilter

class AuthUserUserPermissionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AuthUserUserPermissions.objects.all()
    serializer_class = serializers.AuthUserUserPermissionsSerializer

class AuthUserUserPermissionsList(generics.ListCreateAPIView):
    queryset = models.AuthUserUserPermissions.objects.all()
    serializer_class = serializers.AuthUserUserPermissionsSerializer
    filter_class = filters.AuthUserUserPermissionsListFilter

class AuthtokenTokenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AuthtokenToken.objects.all()
    serializer_class = serializers.AuthtokenTokenSerializer

class AuthtokenTokenList(generics.ListCreateAPIView):
    queryset = models.AuthtokenToken.objects.all()
    serializer_class = serializers.AuthtokenTokenSerializer
    filter_class = filters.AuthtokenTokenListFilter

class CaptchaCaptchastoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CaptchaCaptchastore.objects.all()
    serializer_class = serializers.CaptchaCaptchastoreSerializer

class CaptchaCaptchastoreList(generics.ListCreateAPIView):
    queryset = models.CaptchaCaptchastore.objects.all()
    serializer_class = serializers.CaptchaCaptchastoreSerializer
    filter_class = filters.CaptchaCaptchastoreListFilter

class CoreContactusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CoreContactus.objects.all()
    serializer_class = serializers.CoreContactusSerializer

class CoreContactusList(generics.ListCreateAPIView):
    queryset = models.CoreContactus.objects.all()
    serializer_class = serializers.CoreContactusSerializer
    filter_class = filters.CoreContactusListFilter

class CoreEncodingtypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CoreEncodingtype.objects.all()
    serializer_class = serializers.CoreEncodingtypeSerializer

class CoreEncodingtypeList(generics.ListCreateAPIView):
    queryset = models.CoreEncodingtype.objects.all()
    serializer_class = serializers.CoreEncodingtypeSerializer
    filter_class = filters.CoreEncodingtypeListFilter

class CoreFilebrowseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CoreFilebrowse.objects.all()
    serializer_class = serializers.CoreFilebrowseSerializer

class CoreFilebrowseList(generics.ListCreateAPIView):
    queryset = models.CoreFilebrowse.objects.all()
    serializer_class = serializers.CoreFilebrowseSerializer
    filter_class = filters.CoreFilebrowseListFilter

class CorePagesmenubasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CorePagesmenubas.objects.all()
    serializer_class = serializers.CorePagesmenubasSerializer

class CorePagesmenubasList(generics.ListCreateAPIView):
    queryset = models.CorePagesmenubas.objects.all()
    serializer_class = serializers.CorePagesmenubasSerializer
    filter_class = filters.CorePagesmenubasListFilter

class CoreUserprofileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CoreUserprofile.objects.all()
    serializer_class = serializers.CoreUserprofileSerializer

class CoreUserprofileList(generics.ListCreateAPIView):
    queryset = models.CoreUserprofile.objects.all()
    serializer_class = serializers.CoreUserprofileSerializer
    filter_class = filters.CoreUserprofileListFilter

class DjangoAdminLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DjangoAdminLog.objects.all()
    serializer_class = serializers.DjangoAdminLogSerializer

class DjangoAdminLogList(generics.ListCreateAPIView):
    queryset = models.DjangoAdminLog.objects.all()
    serializer_class = serializers.DjangoAdminLogSerializer
    filter_class = filters.DjangoAdminLogListFilter

class DjangoContentTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DjangoContentType.objects.all()
    serializer_class = serializers.DjangoContentTypeSerializer

class DjangoContentTypeList(generics.ListCreateAPIView):
    queryset = models.DjangoContentType.objects.all()
    serializer_class = serializers.DjangoContentTypeSerializer
    filter_class = filters.DjangoContentTypeListFilter

class DjangoFlatpageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DjangoFlatpage.objects.all()
    serializer_class = serializers.DjangoFlatpageSerializer

class DjangoFlatpageList(generics.ListCreateAPIView):
    queryset = models.DjangoFlatpage.objects.all()
    serializer_class = serializers.DjangoFlatpageSerializer
    filter_class = filters.DjangoFlatpageListFilter

class DjangoFlatpageSitesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DjangoFlatpageSites.objects.all()
    serializer_class = serializers.DjangoFlatpageSitesSerializer

class DjangoFlatpageSitesList(generics.ListCreateAPIView):
    queryset = models.DjangoFlatpageSites.objects.all()
    serializer_class = serializers.DjangoFlatpageSitesSerializer
    filter_class = filters.DjangoFlatpageSitesListFilter

class DjangoMigrationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DjangoMigrations.objects.all()
    serializer_class = serializers.DjangoMigrationsSerializer

class DjangoMigrationsList(generics.ListCreateAPIView):
    queryset = models.DjangoMigrations.objects.all()
    serializer_class = serializers.DjangoMigrationsSerializer
    filter_class = filters.DjangoMigrationsListFilter

class DjangoSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DjangoSession.objects.all()
    serializer_class = serializers.DjangoSessionSerializer

class DjangoSessionList(generics.ListCreateAPIView):
    queryset = models.DjangoSession.objects.all()
    serializer_class = serializers.DjangoSessionSerializer
    filter_class = filters.DjangoSessionListFilter

class DjangoSiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DjangoSite.objects.all()
    serializer_class = serializers.DjangoSiteSerializer

class DjangoSiteList(generics.ListCreateAPIView):
    queryset = models.DjangoSite.objects.all()
    serializer_class = serializers.DjangoSiteSerializer
    filter_class = filters.DjangoSiteListFilter

class EasyThumbnailsSourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EasyThumbnailsSource.objects.all()
    serializer_class = serializers.EasyThumbnailsSourceSerializer

class EasyThumbnailsSourceList(generics.ListCreateAPIView):
    queryset = models.EasyThumbnailsSource.objects.all()
    serializer_class = serializers.EasyThumbnailsSourceSerializer
    filter_class = filters.EasyThumbnailsSourceListFilter

class EasyThumbnailsThumbnailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EasyThumbnailsThumbnail.objects.all()
    serializer_class = serializers.EasyThumbnailsThumbnailSerializer

class EasyThumbnailsThumbnailList(generics.ListCreateAPIView):
    queryset = models.EasyThumbnailsThumbnail.objects.all()
    serializer_class = serializers.EasyThumbnailsThumbnailSerializer
    filter_class = filters.EasyThumbnailsThumbnailListFilter

class EasyThumbnailsThumbnaildimensionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.EasyThumbnailsThumbnaildimensions.objects.all()
    serializer_class = serializers.EasyThumbnailsThumbnaildimensionsSerializer

class EasyThumbnailsThumbnaildimensionsList(generics.ListCreateAPIView):
    queryset = models.EasyThumbnailsThumbnaildimensions.objects.all()
    serializer_class = serializers.EasyThumbnailsThumbnaildimensionsSerializer
    filter_class = filters.EasyThumbnailsThumbnaildimensionsListFilter

class FilerClipboardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FilerClipboard.objects.all()
    serializer_class = serializers.FilerClipboardSerializer

class FilerClipboardList(generics.ListCreateAPIView):
    queryset = models.FilerClipboard.objects.all()
    serializer_class = serializers.FilerClipboardSerializer
    filter_class = filters.FilerClipboardListFilter

class FilerClipboarditemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FilerClipboarditem.objects.all()
    serializer_class = serializers.FilerClipboarditemSerializer

class FilerClipboarditemList(generics.ListCreateAPIView):
    queryset = models.FilerClipboarditem.objects.all()
    serializer_class = serializers.FilerClipboarditemSerializer
    filter_class = filters.FilerClipboarditemListFilter

class FilerFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FilerFile.objects.all()
    serializer_class = serializers.FilerFileSerializer

class FilerFileList(generics.ListCreateAPIView):
    queryset = models.FilerFile.objects.all()
    serializer_class = serializers.FilerFileSerializer
    filter_class = filters.FilerFileListFilter

class FilerFolderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FilerFolder.objects.all()
    serializer_class = serializers.FilerFolderSerializer

class FilerFolderList(generics.ListCreateAPIView):
    queryset = models.FilerFolder.objects.all()
    serializer_class = serializers.FilerFolderSerializer
    filter_class = filters.FilerFolderListFilter

class FilerFolderpermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FilerFolderpermission.objects.all()
    serializer_class = serializers.FilerFolderpermissionSerializer

class FilerFolderpermissionList(generics.ListCreateAPIView):
    queryset = models.FilerFolderpermission.objects.all()
    serializer_class = serializers.FilerFolderpermissionSerializer
    filter_class = filters.FilerFolderpermissionListFilter

class FilerImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FilerImage.objects.all()
    serializer_class = serializers.FilerImageSerializer

class FilerImageList(generics.ListCreateAPIView):
    queryset = models.FilerImage.objects.all()
    serializer_class = serializers.FilerImageSerializer
    filter_class = filters.FilerImageListFilter

class PodsBuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsBuilding.objects.all()
    serializer_class = serializers.PodsBuildingSerializer

class PodsBuildingList(generics.ListCreateAPIView):
    queryset = models.PodsBuilding.objects.all()
    serializer_class = serializers.PodsBuildingSerializer
    filter_class = filters.PodsBuildingListFilter

class PodsChannelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsChannel.objects.all()
    serializer_class = serializers.PodsChannelSerializer

class PodsChannelList(generics.ListCreateAPIView):
    queryset = models.PodsChannel.objects.all()
    serializer_class = serializers.PodsChannelSerializer
    filter_class = filters.PodsChannelListFilter

class PodsChannelOwnersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsChannelOwners.objects.all()
    serializer_class = serializers.PodsChannelOwnersSerializer

class PodsChannelOwnersList(generics.ListCreateAPIView):
    queryset = models.PodsChannelOwners.objects.all()
    serializer_class = serializers.PodsChannelOwnersSerializer
    filter_class = filters.PodsChannelOwnersListFilter

class PodsChannelUsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsChannelUsers.objects.all()
    serializer_class = serializers.PodsChannelUsersSerializer

class PodsChannelUsersList(generics.ListCreateAPIView):
    queryset = models.PodsChannelUsers.objects.all()
    serializer_class = serializers.PodsChannelUsersSerializer
    filter_class = filters.PodsChannelUsersListFilter

class PodsChapterpodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsChapterpods.objects.all()
    serializer_class = serializers.PodsChapterpodsSerializer

class PodsChapterpodsList(generics.ListCreateAPIView):
    queryset = models.PodsChapterpods.objects.all()
    serializer_class = serializers.PodsChapterpodsSerializer
    filter_class = filters.PodsChapterpodsListFilter

class PodsContributorpodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsContributorpods.objects.all()
    serializer_class = serializers.PodsContributorpodsSerializer

class PodsContributorpodsList(generics.ListCreateAPIView):
    queryset = models.PodsContributorpods.objects.all()
    serializer_class = serializers.PodsContributorpodsSerializer
    filter_class = filters.PodsContributorpodsListFilter

class PodsDisciplineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsDiscipline.objects.all()
    serializer_class = serializers.PodsDisciplineSerializer

class PodsDisciplineList(generics.ListCreateAPIView):
    queryset = models.PodsDiscipline.objects.all()
    serializer_class = serializers.PodsDisciplineSerializer
    filter_class = filters.PodsDisciplineListFilter

class PodsDocpodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsDocpods.objects.all()
    serializer_class = serializers.PodsDocpodsSerializer

class PodsDocpodsList(generics.ListCreateAPIView):
    queryset = models.PodsDocpods.objects.all()
    serializer_class = serializers.PodsDocpodsSerializer
    filter_class = filters.PodsDocpodsListFilter

class PodsEncodingpodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsEncodingpods.objects.all()
    serializer_class = serializers.PodsEncodingpodsSerializer

class PodsEncodingpodsList(generics.ListCreateAPIView):
    queryset = models.PodsEncodingpods.objects.all()
    serializer_class = serializers.PodsEncodingpodsSerializer
    filter_class = filters.PodsEncodingpodsListFilter

class PodsEnrichpodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsEnrichpods.objects.all()
    serializer_class = serializers.PodsEnrichpodsSerializer

class PodsEnrichpodsList(generics.ListCreateAPIView):
    queryset = models.PodsEnrichpods.objects.all()
    serializer_class = serializers.PodsEnrichpodsSerializer
    filter_class = filters.PodsEnrichpodsListFilter

class PodsFavoritesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsFavorites.objects.all()
    serializer_class = serializers.PodsFavoritesSerializer

class PodsFavoritesList(generics.ListCreateAPIView):
    queryset = models.PodsFavorites.objects.all()
    serializer_class = serializers.PodsFavoritesSerializer
    filter_class = filters.PodsFavoritesListFilter

class PodsMediacoursesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsMediacourses.objects.all()
    serializer_class = serializers.PodsMediacoursesSerializer

class PodsMediacoursesList(generics.ListCreateAPIView):
    queryset = models.PodsMediacourses.objects.all()
    serializer_class = serializers.PodsMediacoursesSerializer
    filter_class = filters.PodsMediacoursesListFilter

class PodsNotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsNotes.objects.all()
    serializer_class = serializers.PodsNotesSerializer

class PodsNotesList(generics.ListCreateAPIView):
    queryset = models.PodsNotes.objects.all()
    serializer_class = serializers.PodsNotesSerializer
    filter_class = filters.PodsNotesListFilter

class PodsPodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsPod.objects.all()
    serializer_class = serializers.PodsPodSerializer

class PodsPodList(generics.ListCreateAPIView):
    queryset = models.PodsPod.objects.all()
    serializer_class = serializers.PodsPodSerializer
    filter_class = filters.PodsPodListFilter
    ordering_fields = ('id', 'title')

class PodsPodChannelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsPodChannel.objects.all()
    serializer_class = serializers.PodsPodChannelSerializer

class PodsPodChannelList(generics.ListCreateAPIView):
    queryset = models.PodsPodChannel.objects.all()
    serializer_class = serializers.PodsPodChannelSerializer
    filter_class = filters.PodsPodChannelListFilter

class PodsPodDisciplineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsPodDiscipline.objects.all()
    serializer_class = serializers.PodsPodDisciplineSerializer

class PodsPodDisciplineList(generics.ListCreateAPIView):
    queryset = models.PodsPodDiscipline.objects.all()
    serializer_class = serializers.PodsPodDisciplineSerializer
    filter_class = filters.PodsPodDisciplineListFilter

class PodsPodThemeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsPodTheme.objects.all()
    serializer_class = serializers.PodsPodThemeSerializer

class PodsPodThemeList(generics.ListCreateAPIView):
    queryset = models.PodsPodTheme.objects.all()
    serializer_class = serializers.PodsPodThemeSerializer
    filter_class = filters.PodsPodThemeListFilter

class PodsRecorderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsRecorder.objects.all()
    serializer_class = serializers.PodsRecorderSerializer

class PodsRecorderList(generics.ListCreateAPIView):
    queryset = models.PodsRecorder.objects.all()
    serializer_class = serializers.PodsRecorderSerializer
    filter_class = filters.PodsRecorderListFilter

class PodsReportvideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsReportvideo.objects.all()
    serializer_class = serializers.PodsReportvideoSerializer

class PodsReportvideoList(generics.ListCreateAPIView):
    queryset = models.PodsReportvideo.objects.all()
    serializer_class = serializers.PodsReportvideoSerializer
    filter_class = filters.PodsReportvideoListFilter

class PodsThemeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsTheme.objects.all()
    serializer_class = serializers.PodsThemeSerializer

class PodsThemeList(generics.ListCreateAPIView):
    queryset = models.PodsTheme.objects.all()
    serializer_class = serializers.PodsThemeSerializer
    filter_class = filters.PodsThemeListFilter

class PodsTrackpodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsTrackpods.objects.all()
    serializer_class = serializers.PodsTrackpodsSerializer

class PodsTrackpodsList(generics.ListCreateAPIView):
    queryset = models.PodsTrackpods.objects.all()
    serializer_class = serializers.PodsTrackpodsSerializer
    filter_class = filters.PodsTrackpodsListFilter

class PodsTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PodsType.objects.all()
    serializer_class = serializers.PodsTypeSerializer

class PodsTypeList(generics.ListCreateAPIView):
    queryset = models.PodsType.objects.all()
    serializer_class = serializers.PodsTypeSerializer
    filter_class = filters.PodsTypeListFilter

class TaggitTagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TaggitTag.objects.all()
    serializer_class = serializers.TaggitTagSerializer

class TaggitTagList(generics.ListCreateAPIView):
    queryset = models.TaggitTag.objects.all()
    serializer_class = serializers.TaggitTagSerializer
    filter_class = filters.TaggitTagListFilter

class TaggitTaggeditemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TaggitTaggeditem.objects.all()
    serializer_class = serializers.TaggitTaggeditemSerializer

class TaggitTaggeditemList(generics.ListCreateAPIView):
    queryset = models.TaggitTaggeditem.objects.all()
    serializer_class = serializers.TaggitTaggeditemSerializer
    filter_class = filters.TaggitTaggeditemListFilter

class TaggitTemplatetagsAmodelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TaggitTemplatetagsAmodel.objects.all()
    serializer_class = serializers.TaggitTemplatetagsAmodelSerializer

class TaggitTemplatetagsAmodelList(generics.ListCreateAPIView):
    queryset = models.TaggitTemplatetagsAmodel.objects.all()
    serializer_class = serializers.TaggitTemplatetagsAmodelSerializer
    filter_class = filters.TaggitTemplatetagsAmodelListFilter


## Special routes for sympa
@api_view(('GET',))
@permission_classes((permissions.WhitelistPermission,))
@renderer_classes((renderers.PlainTextRenderer,))
def mailing_list(request, type):
    """
    routes for sympa:
    - /webservice/mailinglist/all/ : all users
    - /webservice/mailinglist/owner/ : only users who have a video
    """
    if type.lower() == "all":
        users = models.AuthUser.objects.all()
    elif type.lower() == "owner":
        filter = models.PodsPod.objects.values_list('owner', flat=True).distinct()
        users = models.AuthUser.objects.filter(id__in=filter)
    else:
        raise Exception("Url not found")
    # Get a valid mails list
    mails_list = [u.email for u in users if u.email and re.match("[^@]+@[^@]+\.[^@]+", u.email)]
    return Response('\n'.join(mails_list))