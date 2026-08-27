from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.admin_dashboard_view, name='dashboard'),
    path('users/', views.admin_users_view, name='users'),
    path('messages/', views.admin_messages_view, name='messages'),
    path('cvs/', views.admin_cvs_view, name='cvs'),
    path('notification/read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
]