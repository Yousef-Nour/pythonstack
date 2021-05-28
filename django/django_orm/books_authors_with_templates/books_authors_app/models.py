from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_app = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #authors=

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField()
    books=models.ManyToManyField(Book, related_name="authors")
    created_app = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#after i define the method addBook in viwes.py 
def addOneBook(title, desc):#I added in the () to pass it 
    new_book = Book.objects.create(title=title, desc=desc)#to added books in Book class #the value from front end
    #new_book i put it in the variable to know what happen or added in model !!
    #It must returend the data to passit to the views
    return new_book

#define the function to view the data in the html for client
def allBooks():
    return Book.objects.all()  #and return list of objects

def getBook(id):  ##I added the Id i () to define id !!
    return Book.objects.get(id=id)

def allAuthors():
    return Author.objects.all()


def addOneAuthor(first_name,last_name):
    new_author = Author.objects.create(first_name=first_name, last_name=last_name)
    return new_author


def getAuthor(id):
    return Author.objects.get(id=id)


def setSpecialBook(id, author_id):
    selectedAuthor = Author.objects.get(id = author_id)
    selectedBook = Book.objects.get(id = id)

    selectedBook.authors.add(selectedAuthor)
    return author_id