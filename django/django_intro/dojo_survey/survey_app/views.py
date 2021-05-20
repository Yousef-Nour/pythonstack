from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    context = {
        'name' : request.POST['name'],
        'dojo_location' : request.POST['dojo_location'],
        'favorite_language' : request.POST['favorite_language'],
        'comment' : request.POST['comment'],
     }
    return render(request, "index2.html", context)
