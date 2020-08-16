from django.contrib.sitemaps import Sitemap
from .models import Profile


class ProfileSitemap(Sitemap):

    def items(self):
        return Profile.objects.all()
