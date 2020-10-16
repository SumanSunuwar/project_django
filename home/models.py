from django.db import models


# Create your models here.


# Book
# name, isbn, price, image

class Author(models.Model):
	name = models.CharField(max_length=255)
	contact =  models.CharField(max_length=255, null=True, blank=True)
	address = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name



class Book(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	isbn = models.CharField(max_length=255, null=True, blank=True)
	price = models.CharField(max_length=255)
	book_image = models.ImageField(upload_to="upload/book", blank=True, null=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name