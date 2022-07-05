from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="view 1"),
    path("another/", views.another, name="another view"),
    path("lastone/", views.lastone, name="last one"),
]