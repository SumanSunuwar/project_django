from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from home.models import Book, Author
from home.forms import BookForm, AuthorForm

def main_view(request):
	context = {}
	return render(request, "mainPage.html", context)

def home_view(request):
	books = Book.objects.all()
	context = {"books" : books}
	return render(request, "book_list.html", context)

def add_book(request):
	form = BookForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("home:book_list"))
	return render(request, "form.html", {"form" : form})

def edit_book(request, book_id):
	book = get_object_or_404(Book, id=book_id)
	form = BookForm(request.POST or None, request.FILES or None, instance=book)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("home:book_list"))
	return render(request, "form.html", {"form" : form})

def delete_book(request, book_id):	# passing the request and POST from the delete key in indext.html
	book = get_object_or_404(Book, id=book_id) 	# getting the item ready which was requested with POST method
	if request.method == 'POST':	# this POST is confirm button in the delete.html page which passes through request 
		book.delete()	# builtin delete function in django models
		return HttpResponseRedirect(reverse("home:book_list")) # it will redirect to main page of book list after deletion
	return render(request, "delete.html", {"item" : book})	# rendering to delete.html page, helps to go through html here

def author_view(request):
	authors = Author.objects.all()
	context = {"authors" : authors}
	return render(request, "authorList.html", context)

def add_author(request):
	form = AuthorForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("home:author_list"))
	return render(request, "form.html", {"form" : form})


def edit_author(request, author_id): 
	author = get_object_or_404(Author, id=author_id)
	form = AuthorForm(request.POST or None, request.FILES or None, instance=author)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("home:author_list"))
	return render(request, "form.html", {"form" : form})

def delete_author(request, author_id):	# passing the request and POST from the delete key in main listing page
	author = get_object_or_404(Author, id=author_id) 	# getting the item ready which was requested with POST method
	if request.method == 'POST':	# this POST is confirm button in the deleting template page which passes through request 
		author.delete()	# builtin delete function in django models deletes object from model db
		return HttpResponseRedirect(reverse("home:author_list")) # it will redirect to main page of book list after deletion
	return render(request, "delete.html", {"item" : author})	# rendering to delete.html page, helps to go through html here

def author_book_view(request, author_id):

	author = get_object_or_404(Author, id=author_id)
	author_book = author.book_set.all()
	context = {"author_book" : author_book}
	return render(request, "author_book.html", context)