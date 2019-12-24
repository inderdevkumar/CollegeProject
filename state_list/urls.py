from django.urls import path
#sfrom .views import (searchposts)

from . import views
#from .views import (search) 
    
urlpatterns = [
    #path('search', views.search, name='search'),
    path('searchposts', views.searchposts, name='searchposts'),
    
]