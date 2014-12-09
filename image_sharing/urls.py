from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
import settings
from imagesharing import urls as appurls

urlpatterns = patterns('',
    url(r'^', include(appurls)),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)