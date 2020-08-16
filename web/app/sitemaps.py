from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['main:about']

    def location(self, obj):
        return reverse(obj)
