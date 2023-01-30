from django.urls import path

from .views import fileView

urlpatterns = [
    path("send/", fileView.as_view()),
]
