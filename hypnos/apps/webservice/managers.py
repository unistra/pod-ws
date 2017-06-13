from django.db import models

class PodsPodManager(models.Manager):
    """ Pods Pod manager """

    def get_queryset(self):
        """ queryset """
        return super(PodsPodManager, self).get_queryset().prefetch_related(
        "podspodchannel_set", "podspoddiscipline_set", "podspodtheme_set", "podscontributorpods_set",
        "type", "owner", "podsdocpods_set", "podsenrichpods_set", "podsencodingpods_set", "podstrackpods_set",
        "podschapterpods_set", "podsencodingpods_set__encodingtype")