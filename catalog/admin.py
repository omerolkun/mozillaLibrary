from django.contrib import admin
#name omergenc
#mail omergenc@gmail.com
#password Cc717343
# Register your models here.
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','date_of_death')
admin.site.register(Author, AuthorAdmin)
