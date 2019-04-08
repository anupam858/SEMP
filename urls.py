from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signup, name='sign'),
    path('login/', views.loggedin, name='log'),
    path('logout/', views.loggedout, name='logout'),
    path('customer/', views.chome, name='chomepage'),
    path('customer/signup/', views.signup_c, name='signup'),
    
]
