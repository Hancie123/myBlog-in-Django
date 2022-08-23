from django.shortcuts import render, HttpResponse
from blog.models import Blog,Contact
import math

# Create your views here.
def index(request):
    data = Blog.objects.all()
    result={'blogdata': data}
    return render(request, 'index.html', result)

def blog(request):
    no_of_post=3
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)


    blog = Blog.objects.all()
    length=len(blog)
    blog=blog[(page-1)*no_of_post: page*no_of_post]
    if page>1:
        prev=page-1
    else:
        prev=None

    if page<math.ceil(length/no_of_post):
        nxt= page+1

    else:
        nxt=None
   




    result={'blog': blog, 'prev': prev, 'nxt': nxt}
    return render(request, 'blog.html', result)

def about(request):
    return render(request,'About.html')


def blogpost(request, slug):
    blogs = Blog.objects.filter(slug=slug).first()
    context_dict= {'blogs': blogs}
    return render(request, 'blogpost.html', context_dict)
    
   

def contact(request):

    context={'success':False}
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ins=Contact(name=name, email=email, message=message)
        ins.save()
        context={'success':True}

    


    return render(request, 'contact.html', context)


def search(request):
    return render(request, 'search.html')
