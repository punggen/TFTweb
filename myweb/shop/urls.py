# shop/urls.py
from django.conf.urls import url
from . import views
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$',views.home),
    url(r'^register',views.register),
    url(r'^login',views.User_login),
    url(r'^personal',views.personal),
    url(r'^logout',views.User_logout),
    url(r'^reset',views.reset_password),
    url(r'^car',views.car),
    url(r'^(?P<product_id>[0-9]+)/$',views.product_detail),
    url(r'^post/(?P<post_id>[0-9]+)/$',views.post_detail),
    url(r'^addpost',views.addpost),
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]