from django.db import models
from django.db.models.fields import DecimalField

# Create your models here.


class Author(models.Model):
    author_id = models.AutoField(primary_key=True, editable=False)
    author_name = models.CharField(max_length=45, null=False, blank=True)
    author_surname = models.CharField(max_length=45, null=False, blank=True)

    def __str__(self):
        return self.author_name + ' ' + self.author_surname


class CategoryDetails(models.Model):
    category_id = models.AutoField(primary_key=True, editable=False)
    category_name = models.CharField(max_length=45, null=False, blank=True)

    def __str__(self):
        return self.category_name


class BookDetails(models.Model):
    book_id = models.AutoField(primary_key=True, editable=False)
    ISBN = models.CharField(max_length=20, null=True, blank=True)
    book_title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    publication_year = models.IntegerField(null=False, blank=False, default=0)
    language = models.CharField(max_length=30, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity_for_sale = models.IntegerField(null=False, blank=False, default=0)
    autor_id = models.ForeignKey(
        Author, on_delete=models.SET_DEFAULT, null=False, default=0)
    category_id = models.ForeignKey(
        CategoryDetails, on_delete=models.SET_DEFAULT, null=False, default=0)

    def __str__(self):
        return self.book_title
