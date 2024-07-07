from django.urls import path

from clients import views
from clients.apps import ClientsConfig

app_name = ClientsConfig.name

urlpatterns = [
    path('create/', views.ClientCreateView.as_view(), name='create'),
    path('', views.ClientListView.as_view(), name='list'),
    path('view/<int:pk>/', views.ClientDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', views.ClientUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.ClientDeleteView.as_view(), name='delete'),
]
