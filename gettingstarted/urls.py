from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("min", hello.views.min, name="min"),
    path("light_on", hello.views.light_on, name="light_on"),
    path("light_off", hello.views.light_off, name="light_off"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
