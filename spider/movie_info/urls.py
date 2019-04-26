from django.conf.urls import url
from . import views


app_name = 'movie_info'
urlpatterns = [
    url(r'^$',views.index),
    url(r'^pa/$',views.pa),
    url(r'^page/list_(\d+).html$',views.index),
    url(r'^detail/(\d+).html$',views.detail),
]