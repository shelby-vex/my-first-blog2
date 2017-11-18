from djano.conf.urls import urls
from . import views

urlpatterns = [
    urls(r'^$', views.post_list, name='post_list')
]
