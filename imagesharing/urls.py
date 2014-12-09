from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'main'),
    url(r'^upload/$', views.index_handle_upload, name="upload")

)