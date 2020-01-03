from django.shortcuts import render
from .models import colleges
from django.db.models import Q

from django.shortcuts import get_object_or_404  # for detail function 

# Create your views here.
def state(request):
    list= colleges.objects 
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query)

            results= colleges.objects.filter(lookups).distinct()
            

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'state.html', context)

        else:
            return render(request, 'state.html',{'state_list':list})

    else:
        return render(request, 'state.html',{'state_list':list})

def state_colleges(request):
    
    college_list= colleges.objects
    
    
    return render(request, 'home.html',{'list':college_list})


def detail(request, college_id):
    detail= get_object_or_404(colleges, pk= college_id)
    return render(request, 'detail.html', {'college':detail})