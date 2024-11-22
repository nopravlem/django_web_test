from django.urls import path
from . import views

urlpatterns = [
    path('', views.parse_XML_file, name='parse_XML_file'),
]
