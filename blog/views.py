from django.shortcuts import render, HttpResponse
from blog.models import Blog

# Create your views here.
def index(request):
    data = Blog.objects.all()
    result={'blogdata': data}
    return render(request, 'index.html', result)

def blog(request):
    blog = Blog.objects.all()
    result={'blog': blog}
    return render(request, 'blog.html', result)

def about(request):
    return render(request,'About.html')


def blogpost(request, parasite_name_slug):
    parasite = Blog.objects.filter(slug=parasite_name_slug).first()
    context_dict= {'parasite': parasite}
    return render(request, 'blogpost.html', context_dict)
    
   

def contact(request):
    return render(request, 'contact.html')


def search(request):
    return render(request, 'search.html')
