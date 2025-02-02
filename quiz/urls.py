
from django.urls import path
from .views import quiz_view

urlpatterns = [
    path("mmse", quiz_view, name="mmse"),
]
