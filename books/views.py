from django.shortcuts import render


def index(request):
    

    return  render(request, "pages/index.html")

def books(request):
    
    return  render(request, "pages/books.html")

def delete(request,id):

    return  render(request, "pages/delete.html")

def update(request,id):

    return  render(request, "pages/update.html")



# Create your views here.
