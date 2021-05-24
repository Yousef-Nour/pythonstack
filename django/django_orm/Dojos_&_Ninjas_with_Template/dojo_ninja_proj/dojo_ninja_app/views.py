from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index(request):
    context={
        "all_dojos" : models.Dojo.objects.all(),
    }

    return render(request,'index.html',context)

def create(request):
    if request.method == "POST":
        if request.POST['model'] == 'dojo':
            models.Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
        
        if request.POST['model'] == 'ninja':
            models.Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo= models.Dojo.objects.get(id=request.POST['dojo']))
    return redirect('/')




    #     context={
    #     "all_dojo" : models.dojos.Objects.all().values(),
    #     "all_ninja" : models.ninjas.Objects.all(),
    # }
