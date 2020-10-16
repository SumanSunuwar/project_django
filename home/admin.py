from django.contrib import admin
from home.models import Book

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
	list_display = ("name", "isbn", "price", "created", "modified")
	list_filter = ("price",)
	search_fields = ("name", "isbn")