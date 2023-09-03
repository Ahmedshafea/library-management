from django import forms
from .models import Books,Categories


class CatForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields =[
            'cat_name',
                ]
        widgets ={
            'cat_name': forms.TextInput(attrs={'class':'form-control'}),
                }


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields =[
                'book_name',
                'author_name',
                'book_photo',
                'author_avatar',
                'page_count',
                'sold_price',
                'borrowing_cost',
                'borrowing_period',
                'status',
                'categories',
                ]
        widgets ={
                'book_name': forms.TextInput(attrs={'class':'form-control'}),
                'author_name': forms.TextInput(attrs={'class':'form-control'}),
                'book_photo': forms.FileInput(attrs={'class':'form-control'}),
                'author_avatar': forms.FileInput(attrs={'class':'form-control'}),
                'page_count': forms.NumberInput(attrs={'class':'form-control'}),
                'sold_price': forms.NumberInput(attrs={'class':'form-control'}),
                'borrowing_cost': forms.NumberInput(attrs={'class':'form-control'}),
                'borrowing_period': forms.Select(attrs={'class':'form-control'}),
                'status': forms.Select(attrs={'class':'form-control'}),
                'categories': forms.Select(attrs={'class':'form-control'}),

                

                }


