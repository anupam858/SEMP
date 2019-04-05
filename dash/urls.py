from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dash, name='dashboard'),
    path('admindashboard', views.dashadmin, name='dashboardadmin')
]
