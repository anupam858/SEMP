from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from home.models import UserCollection
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def dash(request):
      print('User Ran')

      return(render(request, 'dash\dashskeleton.html', {}))


@login_required(login_url='/loginadm')
def dashadmin(request):

      print('Admin Ran')
      return(render(request, 'dash\dashadminskeleton.html', {}))
