from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    #https://docs.djangoproject.com/en/3.0/ref/contrib/sitemaps/.
    #relevance ...?? maximum value is 1
    def items(self):
        return Post.published.all()
    def lastmod(self, obj):
        return obj.updated