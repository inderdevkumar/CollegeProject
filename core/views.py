from django.shortcuts import render
from .models import colleges

# Create your views here.

def home(request):
    college_list= colleges.objects
    return render(request, 'core/home.html',{'list':college_list})