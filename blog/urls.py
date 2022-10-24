from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('bugatti',buga,name='bugatti'),
    path('bugadetail',bugadetail,name='bugadetail')
]