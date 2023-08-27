from django.shortcuts import render
from .models import Books,Categories

def index(request):
    context={

        'books':Books.objects.all(),
        'categories':Categories.objects.all(),



    }

    return  render(request, "pages/index.html",context)

def books(request):
    
    return  render(request, "pages/books.html")

def delete(request,id):

    return  render(request, "pages/delete.html")

def update(request,id):

    return  render(request, "pages/update.html")



# Create your views here.
