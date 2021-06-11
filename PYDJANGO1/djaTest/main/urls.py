from django.urls import path

from . import views

urlpatterns = [
    # this is the path if nothing gets passed in
    path("", views.index, name="index"),
    # This is the path if v1 gets passed in.
    path("v1/", views.v1, name="view 1"),
]
