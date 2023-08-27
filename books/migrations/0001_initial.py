# Generated by Django 4.2.4 on 2023-08-27 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('author_name', models.CharField(max_length=50)),
                ('book_photo', models.ImageField(blank=True, null=True, upload_to='book/photos')),
                ('author_avatar', models.ImageField(blank=True, null=True, upload_to='author/avatar')),
                ('page_count', models.PositiveIntegerField(blank=True, null=True)),
                ('sold_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('borrowing_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('borrowing_period', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('status', models.CharField(choices=[('Sold', 'Sold'), ('Borrowed', 'Borrowed'), ('Available', 'Available')], max_length=9)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.categories')),
            ],
        ),
    ]
