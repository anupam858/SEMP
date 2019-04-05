from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import UserCollection
from django.contrib.auth.models import Group, User
from dash import views
from django.contrib.auth import login,logout, authenticate

# Create your views here.



def home(request):

      return(render(request, 'home\semp.html', {}))

def signup(request):


      if request.method=='POST':
            org_name1 = request.POST.get('orgname')
            org_id1 = request.POST.get('id')
            email1 = request.POST.get('email')
            phone1 = request.POST.get('number')
            password1 = request.POST.get('psw')
            #password1 = make_password(password, salt=None, hasher='default')
            user_type1 = 'admin'
            

            uc = UserCollection()
            uc.org_name = org_name1
            uc.org_id = org_id1
            uc.email = email1
            uc.phone = phone1
            uc.user_type = user_type1
            uc.user_acctd = [{event_id:'noid', event_name: 'noname'}]
            uc.save()

            username = org_id1 + email1

            user = User.objects.create_user(username, email1, password1)
            user.save()
            
      
      return(render(request,'home\semp.html',{'message':'User Registered'}))

def loggedin(request):

      org_id1 = request.GET.get('orid')
      email1 = request.GET.get('uname')
      passw1 = request.GET.get('psw')

      un = str(org_id1) + str(email1)

      user1 = authenticate(username= un , password=passw1)
      
      print(UserCollection.objects.filter(email=email1).values_list('user_type'))

      if (user1 is not None) and (str(UserCollection.objects.filter(email=email1).values_list('user_type')[0][0])== 'user'):
            
            login(request,user1)
            return(redirect('dashboard'))
      
      elif (user1 is not None) and (str(UserCollection.objects.filter(email=email1).values_list('user_type')[0][0])=='admin'):
            
            login(request, user1)
            return(redirect('dashboardadmin'))
      
      else:
            return(render(request,'home\semp.html', {}))
            
def loggedout(request):
      
      logout(request)
      return(render(request,'home\semp.html', {}))
                                          

            


      
      
      
