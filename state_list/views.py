from django.shortcuts import render
from .models import states
from django.db.models import Q

# Create your views here.

def state(request):
    list= states.objects
    return render(request, 'state.html',{'state_list':list})


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query)

            results= states.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'state.html', context)

        else:
            return render(request, 'state.html')

    else:
        return render(request, 'state.html')

