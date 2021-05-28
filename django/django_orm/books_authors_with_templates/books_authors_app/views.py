from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index(request):
    context = {
        'books' : models.allBooks()    #cant be read without context !#go and bring the all books to view them

    }

    return render(request, "books.html", context) #render the HTML & return the data 

def addBook(request):
    if request.method == 'POST':
        title = request.POST ['title']
        desc = request.POST ['desc']
        #Now go to the database
        newly_created_book = models.addOneBook(title, desc) #iam the view i take the data from models and take it for fron end
        return redirect('/')

#I define the new method to forbidden the re-submission and added with anew name
# def welcomeUser(request):
#     return render(request, 'welcome.html')


def showBook(request, id):
    context = {
    'this_book' : models.getBook(id),
    'allAuthors' : models.allAuthors(), #returned from model in the same context because we are in the same html
    }
    return render(request, 'showBook.html', context)


def addAuthorToBook(request,book_id):
    selected_author_id = request.POST ['selected_author']
    selected_author = models.Author.objects.get(id=selected_author_id)
    this_book = models.Book.objects.get(id=book_id)
    this_book.authors.add(selected_author)
    return redirect(f'/books/{book_id}')
    

def authorHome(request):
    context ={
        'author' : models.allAuthors()
    }
    
    return render(request,'authorHome.html', context)

def addAuthor(request):
    if request.method == 'POST':
        first_name = request.POST ['first_name']
        last_name = request.POST ['last_name']
        new_author = models.addOneAuthor(first_name, last_name)
        return redirect ('/authors')




def showAuthor(request, id):
    context = {
        'this_author' : models.getAuthor(id),
        'all_books' :models.allBooks()

    }
    return render (request,'showAuthor.html',context)


def addAuthortoBook(request,author_id):
    book = request.POST['authors']

    auth = models.setSpecialBook(book, author_id)
    return redirect('/authors/'+str(auth))


