from django.urls import path

from mailings import views
from mailings.apps import MailingsConfig

app_name = MailingsConfig.name

urlpatterns = [
    path('create/', views.MailingCreateView.as_view(), name='create'),
    path('', views.MailingListView.as_view(), name='list'),
    path('view/<int:pk>/', views.MailingDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', views.MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.MailingDeleteView.as_view(), name='delete'),
    path('message/new/', views.MessageCreateView.as_view(), name='message-create'),
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    path('message/<int:pk>/', views.MessageDetailView.as_view(), name='message-detail'),
    path('message/<int:pk>/update/', views.MessageUpdateView.as_view(), name='message-update'),
    path('message/<int:pk>/delete/', views.MessageDeleteView.as_view(), name='message-delete'),
]
