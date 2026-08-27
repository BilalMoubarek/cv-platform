from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('submit-cv/', views.submit_cv_view, name='submit_cv'),
    path('my-submissions/', views.my_submissions_view, name='my_submissions'),
]