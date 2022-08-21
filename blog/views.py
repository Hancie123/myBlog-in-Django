from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'About.html')


def blogpost(request, slug):
    return HttpResponse(f"You are viewing {slug}")

def contact(request):
    return render(request, 'contact.html')
