from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('hide-admin/', views.hide_admin_view, name='hide_admin'),
]