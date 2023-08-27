from django.db import models

# Create your models here.

class Categories(models.Model):
    cat_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.cat_name


class Books(models.Model):
    status_options = [
        ("Sold", "Sold"),
        ("Borrowed", "Borrowed"),
        ("Available", "Available"),
    ]

    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    book_photo = models.ImageField(upload_to='book/photos',null=True,blank=True)
    author_avatar = models.ImageField(upload_to='author/avatar',null=True,blank=True)
    page_count= models.PositiveIntegerField(null=True,blank=True)
    sold_price= models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    borrowing_cost= models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    borrowing_period= models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    status= models.CharField(max_length=9, choices=status_options)
    categories= models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name