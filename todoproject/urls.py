from django.contrib import admin
from django.urls import path
from xml.etree.ElementInclude import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("todoapp.urls"))
]
