from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("I am index")

def IamAppOne(request):
    my_dict = {'index_insert':"I am appone"}
    return render(request, '/proone/index.html',context=my_dict)
