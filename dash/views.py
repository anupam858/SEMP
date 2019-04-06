from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from home.models import UserCollection
from .models import UserRequest
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name='dashboard')
def dash(request):
      print('User Ran')
      usern = request.user.get_username()
      usern = usern.split('+')[1]
      selfdata = UserCollection.objects.filter(email=usern, user_type= 'user')

      return(render(request, 'dash\dashskeleton.html', {'Selfu':selfdata}))


@login_required(redirect_field_name='dashboard')
def requser(request):

      if request.method=='POST':

            ur = UserRequest()
            usern = request.user.get_username()
            usern = usern.split('+')[0]
            ur.org_id = usern
            ur.name = request.POST.get('name')
            ur.email = request.POST.get('email')
            ur.phone = request.POST.get('phone')
            ur.designation = request.POST.get('des')
            ur.gen_id = request.POST.get('id')
            ur.save()

      return(render(request,'dash\dashskeleton.html',{}))
            
      
@login_required(redirect_field_name='admindashboard')
def dashadmin(request):

      print('Admin Ran')
      usern = request.user.get_username()
      usern = usern.split('+')[0]
      selfdata = UserCollection.objects.filter(org_id=usern, user_type= 'admin')
      Users = UserCollection.objects.filter(org_id=usern, user_type= 'user')
      RUsers = UserRequest.objects.filter(org_id=usern)
      print(Users)
      print(RUsers)
      return(render(request, 'dash\dashadminskeleton.html', {'Users':Users, 'Selfu':selfdata, 'RUsers':RUsers}))
