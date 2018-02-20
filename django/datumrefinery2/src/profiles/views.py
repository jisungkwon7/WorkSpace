from django.shortcuts import render

# Create your views here.
def index(request):
    context ={}
    template = 'index.html'
    return render(request,template,context)

def about(request):
    context ={}
    template = 'about.html'
    return render(request,template,context)

def worldpopulation(request):
    context ={}
    template = 'population/worldpopulation.html'
    return render(request,template,context)

def koreanpopulation(request):
    context ={}
    template = 'population/worldpopulation.html'
    return render(request,template,context)
