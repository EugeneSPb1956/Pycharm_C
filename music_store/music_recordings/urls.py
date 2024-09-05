from django.urls import path
from .views import index

urlpaterrns = [
    path('main/', index, name='index'),
]
