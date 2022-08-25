from django.http import HttpResponse
from django.shortcuts import render
from core.models import Blog

def home(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all() # This functions fetc all data stored in Blog 
    context = {'blogs': blogs }
    return render(request, 'blog.html', context)
    
def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first() # filter function helps to grab particular object from database
    print(blog)
    context = { 'blog': blog }                                              # first  function helps to fetch first elements 
    return render(request, 'blogpost.html', context)
    

def contact(request):
   return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')