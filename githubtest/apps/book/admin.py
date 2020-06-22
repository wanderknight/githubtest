from django.contrib import admin
from .models import Book, Author, BookAuthor


class BookAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title',)
    list_filter = ('author_name_str',)
    search_fields = ('title',)


class AwardAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('name_cn',)


class BookAwardAdmin(admin.ModelAdmin):
    list_per_page = 10
    raw_id_fields = ('book', 'award')


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(BookAuthor)
