
from django.urls import path

from . import views
from .views import home
#from . import views.home

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete')
]
