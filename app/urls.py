from django.urls import path
from .views import (index, get_name) 

urlpatterns = [    
    path('',index,name = 'index'),
    path('ftest', get_name,name='ftest'),
]