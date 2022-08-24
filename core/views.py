from django.shortcuts import render, HttpResponse
from core.models import Blog

def home(request):
    return render(request, 'base.html')

def blog(request):
    blogs = Blog.objects.all() 
    context = {'blogs': blogs }
    return render(request, 'blog.html', context)
    
def blogpost(request, slug):
    
    return HttpResponse(request, "this is {{slug}}" )
    

def contact(request):
   return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')