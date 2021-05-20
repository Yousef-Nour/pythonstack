from django.shortcuts import redirect, render
from .models import User

def index(request):
    context = {
        "users": User.objects.all(),
    }
    print(context['users'].__dict__)
    return render(request, "index.html", context)

def addUser(request):
    User.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'], email= request.POST['email'], age = request.POST['age'])
    return redirect('/')