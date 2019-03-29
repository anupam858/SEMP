from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def dash(request):

      return(render(request, 'dash\dashskeleton.html', {}))
      
