# greet/urls.py
from django.urls import path
from .views import greet

urlpatterns = [path("<str:additional_data>", greet.as_view(), name="greet")]
