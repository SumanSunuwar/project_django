from django.urls import path
#from home.views import home_view
from home.views import home_view, add_book, edit_book, delete_book, author_view, add_author, edit_author, delete_author, main_view
app_name = "home"

urlpatterns = [
	path("home/", main_view, name="home"),  #its not working ask?
	path("book_list/", home_view, name="book_list"),
	path("add_book/", add_book, name="add_book"),
	path("edit_book/<int:book_id>/", edit_book, name="edit_book"),
	path("delete_book/<int:book_id>/", delete_book, name="delete_book"),
	path("author_list/", author_view, name="author_list"),
	path("add_author/", add_author, name="add_author"),
	path("edit_author/<int:author_id>/", edit_author, name="edit_author"),
	path("delete_author/<int:author_id>/", delete_author, name="delete_author"),
]
