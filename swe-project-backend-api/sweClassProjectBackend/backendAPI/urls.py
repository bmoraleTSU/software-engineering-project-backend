from django.urls import path
from rest_framework import renderers
from . import views
from backendAPI.views import AbcClientViewSet

urlpatterns = [
  path('clients/', views.AbcClientViewSet.as_view({'get': 'list'})),
  path('clients/<int:id>/', views.AbcClientViewSet.as_view({'get': 'list'})),
]

#Add other URLs for APIS here