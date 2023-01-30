from django.urls import path

from .views import tradesView

urlpatterns = [
    path("balance/", tradesView.as_view()),
]
