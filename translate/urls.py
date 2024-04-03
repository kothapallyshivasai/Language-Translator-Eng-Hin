from django.urls import path
from .views import getResponse, index

urlpatterns = [
    path('', index, name="index"),
    path('getResponse', getResponse, name="getResponse")
]
