from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"HI index"}
    return render(request,'HelpPage/index.html',context=my_dict)

def help(request):
    my_dict = {'insert_me':"HI help"}
    return render(request,'HelpPage/index.html',context=my_dict)
