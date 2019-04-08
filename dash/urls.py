from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dash, name='dashboard'),
    path('admindashboard', views.dashadmin, name='dashboardadmin'),
    path('reqtoadmin', views.requser, name='requestuser'),
    path('admindashboard/venue', views.venueins, name='venue'),
    path('admindashboard/adduser', views.adduser, name='adduser')
]
