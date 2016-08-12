"""newblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin


from blog.views import post_list, post_detail, post_new, edit_post, post_delete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', post_list,name='posts'),
    url(r'^post(?P<pk>\d+)/$', post_detail,name='detail'),
    url(r'^add/', post_new, name='post_create'),
    url(r'^post(?P<pk>\d+)/edit/$', edit_post, name='edit_post'),
    url(r'^post(?P<pk>\d+)/delete/$', post_delete, name='post_delete'),

]
