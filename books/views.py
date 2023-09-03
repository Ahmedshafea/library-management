from django.shortcuts import render,redirect,get_object_or_404
from .models import Books,Categories
from .forms import BookForm,CatForm

def index(request):
    if request.method =="POST":
        add_book=BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_cat=CatForm(request.POST,request.FILES)
        if add_cat.is_valid():
            add_cat.save()


    context={

        'books':Books.objects.all(),
        'categories':Categories.objects.all(),
        'form': BookForm(),
        'cat_form': CatForm(),

    }

    return  render(request, "pages/index.html",context)

def books(request):

    if request.method =="POST":
        add_cat=CatForm(request.POST,request.FILES)
        if add_cat.is_valid():
            add_cat.save()

    context={
        'books':Books.objects.all(),
        'categories':Categories.objects.all(),
        'cat_form': CatForm(),


        }    
    return  render(request, "pages/books.html",context)

def delete(request,id):
    book_id=get_object_or_404(Books,id=id)
    if request.method== "POST":
        book_id.delete()
        return redirect('/')



    return  render(request, "pages/delete.html")

def update(request,id):
    book_id=Books.objects.get(id=id)
    if request.method== "POST":
        book_update = BookForm(request.POST, request.FILES,instance=book_id)
        if book_update.is_valid():
            book_update.save()
            return redirect('/')
    else:
        book_update = BookForm(instance=book_id)

    context={
        'form':book_update,
        
        }    

    return  render(request, "pages/update.html", context)



# Create your views here.
