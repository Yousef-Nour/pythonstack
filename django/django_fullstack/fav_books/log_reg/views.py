from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    if 'id' in request.session:
        return redirect('/books') #welcome
    return render(request,'index.html')

def register(request):
    errors = models.User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        if request.method == "POST":
            firstname = request.POST['fname']
            lastname = request.POST['lname']
            Email = request.POST['email']
            Password = request.POST['passwd']
            Confirm = request.POST['confpasswd']
            if Password == Confirm:
                password = request.POST['passwd']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user = models.create_user(firstname,lastname,Email,pw_hash)
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                messages.success(request, "successfully registered (or logged in)!")
                return redirect('/books')
        return redirect('/')

def welcome(request):
    if "id" in request.session:
        context = {
            'books' : models.get_all(),  #from model for for_loop in welcome
            'fav_books' : models.get_fav_books(request.session['id'])  #from model for if_statement in welcome #request.session['email'] >> الايميل اللي في السيشين مخزن عشان اعرف اصلا مين هو!!
        }
        return render(request,'welcome.html', context)
    return redirect('/')

def login(request):
    errors = models.User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        print("NO ERRORS")
        if request.method == "POST":
            Email = request.POST['email']
            Password = request.POST['passwd']
            user = models.get_user(Email)
            if user:
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                return redirect('/books')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def add_book(request):
    if request.method == "POST":
        errors= models.Book.objects.validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/books')

        else:
            title = request.POST['title']
            desc = request.POST['description']
            models.create_book(title, desc, request.session['id'])
            return redirect("/")
def book_details(request, book_id):
    context={
        'book': models.get_book_details(book_id)
    }
    return render(request, 'book_details.html', context)

def add_to_fav(request, book_id):
    models.add_to_favour(request.session['id'], book_id)
    return redirect('/books')

def del_book(request, book_id):
    models.delete_book(book_id)
    
    return redirect('/books')

def update_book(request, book_id):
    models.update(book_id=book_id,title=request.POST['title'],description= request.POST['description'])

    return redirect(f'/books/{book_id}')