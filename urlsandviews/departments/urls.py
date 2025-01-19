from django.urls import path

from urlsandviews.departments.views import index

urlpatterns = [
    path('', index)
]