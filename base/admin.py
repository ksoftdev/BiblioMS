from django.contrib import admin
from .models import BookDetails, CategoryDetails, Author

# Register your models here.
admin.site.register(BookDetails)
admin.site.register(CategoryDetails)
admin.site.register(Author)