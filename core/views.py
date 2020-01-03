from django.shortcuts import render
from .models import colleges
from django.db.models import Q

from django.shortcuts import get_object_or_404  # for detail function 

# Create your views here.



def state(request):
  
    lists = colleges.objects.distinct('state') # To get all object datas with distinct state object
    
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(state__icontains=query)

            results= colleges.objects.filter(lookups).distinct()
            

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'state.html', context)

        else:
            return render(request, 'state.html',{'state_list':lists})

    else:
        return render(request, 'state.html',{'state_list':lists})




def detail(request, college_id):
    detail= get_object_or_404(colleges, pk= college_id)
    return render(request, 'detail.html', {'college':detail})

    