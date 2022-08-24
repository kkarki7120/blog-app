from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'base.html')

def blog(request):
    return render(request, 'blog.html')
    
def blogpost(request, slug):
    slug = slug
    print(slug)
    context = {
        'slug' : slug
    }
    return render(request, 'blogpost.html', context)

def contact(request):
   return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')