from django.shortcuts import render,redirect,get_object_or_404
from .models import Books,Categories
from .forms import BookForm,CatForm
from django.db.models import Sum


def index(request):
    if request.method =="POST":
        add_book=BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_cat=CatForm(request.POST,request.FILES)
        if add_cat.is_valid():
            add_cat.save()

    # Calculate the total price for sold items
    total_price_sold = Books.objects.filter(status='Sold').aggregate(total_price=Sum('sold_price'))['total_price'] or 0

    # Calculate the total cost for borrowed items
    total_cost_borrowed = Books.objects.filter(status='Borrowed').aggregate(total_cost=Sum('total_borrowing'))['total_cost'] or 0

    total_sum = total_cost_borrowed + total_price_sold


    context={

        'books':Books.objects.all(),
        'categories':Categories.objects.all(),
        'form': BookForm(),
        'cat_form': CatForm(),
        'bookcount':Books.objects.all().count(),
        'booksold':Books.objects.filter(status='Sold').count(),
        'bookborrowed':Books.objects.filter(status='Borrowed').count(),
        'bookavailable':Books.objects.filter(status='Available').count(),
        'total_sum':total_sum,
        'total_price_sold':total_price_sold,
        'total_cost_borrowed':total_cost_borrowed,



    }

    return  render(request, "pages/index.html",context)

def books(request):
    search = Books.objects.all()
    bookname = None
    if 'search' in request.GET:
        bookname=request.GET['search']
        if bookname:
            search = search.filter(book_name__icontains=bookname)

    if request.method =="POST":
        add_cat=CatForm(request.POST,request.FILES)
        if add_cat.is_valid():
            add_cat.save()

    context={
        'books':search,
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
