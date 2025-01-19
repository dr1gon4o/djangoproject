from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    #return HttpResponse("<h1>hello!<h1>")
    return render(request, template_name='myapp/home.html', context={})

def add(request):
    # return HttpResponse("<h1>hihihi!<h1>")
    return render(request, template_name='myapp/add.html', context={})
def delete(request):
    # return HttpResponse("<h1>hohoho!<h1>")
    return render(request, template_name='myapp/delete.html', context={})
