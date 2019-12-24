from django.shortcuts import render
from .models import colleges
from django.shortcuts import get_object_or_404  # for detail function 

# Create your views here.

def state_colleges(request):
    college_list= colleges.objects
    return render(request, 'home.html',{'list':college_list})


def detail(request, college_id):
    detail= get_object_or_404(colleges, pk= college_id)
    return render(request, 'detail.html', {'college':detail})