from django.conf.urls import url, include
from django.contrib import admin
from . import views as djangonautic_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as articles_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^about/$', djangonautic_views.about),
    url(r'^$', articles_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)