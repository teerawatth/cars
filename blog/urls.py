from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('bugatti',buga,name='bugatti'),
    path('bugadetail/<int:pk>',bugadetail,name = 'bugadetail'),
    path('koenig',koenig,name='koenig'),
    path('koenigdetail/<int:pk>',koenigdetail,name = 'koenigdetail'),
]