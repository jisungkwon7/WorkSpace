from django.shortcuts import render
from blogframe.models import Post,Comment

from django.views.generic import (TemplateView,ListView
                                  )


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
    template = 'population/world.html'
    return render(request,template,context)

def koreanpopulation(request):
    context ={}
    template = 'population/korea.html'
    return render(request,template,context)



class AboutView(TemplateView):
    template_name = 'aboutview.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))
