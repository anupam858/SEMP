from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from home.models import UserCollection, UserAssociation
from datetime import time
from .models import *
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name='log')
def dash(request):
      print('User Ran')
      usern = request.user.get_username()
      usern = usern.split('+')[1]
      selfdata = UserCollection.objects.filter(email=usern, user_type= 'user')

      return(render(request, 'dash\dashskeleton.html', {'Selfu':selfdata}))


@login_required(redirect_field_name='log')
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
            
      
@login_required(redirect_field_name='log')
def dashadmin(request):

      print('Admin Ran')
      usern = request.user.get_username()
      usern = usern.split('+')[0]
      selfdata = UserCollection.objects.filter(org_id=usern, user_type= 'admin')
      Users = UserCollection.objects.filter(org_id=usern, user_type= 'user')
      RUsers = UserRequest.objects.filter(org_id=usern)
      Ven = Venue.objects.filter(org_id= usern)
      print(Users)
      print(RUsers)
      print(Ven)
      return(render(request, 'dash\dashadminskeleton.html', {'Users':Users, 'Selfu':selfdata, 'RUsers':RUsers, 'Venue':Ven}))

@login_required(redirect_field_name='log')
def venueins(request):

      print('Inserting Venue')

      if request.method=='POST':
            
            v_occ = Voccupy()
            venue = Venue()
            v_occ.eid = 'noid'
            #v_occ.edate = '1000-01-01'
            v_occ.etime_s = time(00,00,00)
            v_occ.etime_e = time(00,00,00)
            venue.org_id = request.user.get_username().split('+')[0]
            venue.v_name= request.POST.get('v_name')
            venue.capacity= request.POST.get('v_capacity')
            venue.floor = request.POST.get('v_floor')
            venue.room_no = request.POST.get('v_room')
            venue.occupancy = [v_occ]

            venue.save()
            
      usern = request.user.get_username()
      usern = usern.split('+')[0]
      selfdata = UserCollection.objects.filter(org_id=usern, user_type= 'admin')
      Users = UserCollection.objects.filter(org_id=usern, user_type= 'user')
      RUsers = UserRequest.objects.filter(org_id=usern)
      Ven = Venue.objects.filter(org_id= usern)
      
      #return(render(request, 'dash\dashadminskeleton.html', {'Users':Users, 'Selfu':selfdata, 'RUsers':RUsers, 'Venue':Ven}))
      return(redirect('dashboardadmin'))
      
@login_required(redirect_field_name='log')
def adduser(request):

      if request.method=='POST':
            
            nu = UserCollection()
            ua = UserAssociation()
            ua.event_id='noid'
            ua.event_name= 'noname'
            usern = request.user.get_username()
            orgid= usern.split('+')[0]
            username1=request.POST.get('u_name')
            useremail=request.POST.get('u_mail')
            userphone=request.POST.get('u_phone')
            userdesignation=request.POST.get('u_desig')
            usergen_id=request.POST.get('u_id')
            for orgname in UserCollection.objects.filter(org_id= usern, user_type= 'admin'):
                  nu.org_name = orgname
                  
            Users = UserCollection.objects.filter(org_id=usern, user_type= 'user')
            
            
            
            
            nu.org_id = orgid
            nu.name=username1
            nu.email = useremail
            nu.phone = userphone
            nu.gen_id = usergen_id
            nu.designation = userdesignation
            nu.user_type = 'user'
            nu.user_acctd = [ua]
            nu.save()
            

            username = orgid +'+'+ useremail

            user = User.objects.create_user(username, useremail, 'password')
            user.save()
            
      return(redirect('dashboardadmin'))
            
            
