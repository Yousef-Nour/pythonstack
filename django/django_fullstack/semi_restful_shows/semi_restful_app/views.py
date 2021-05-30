from semi_restful_app.models import Series
from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index(request):
    return redirect ('/shows')

def shows(request):
    context={
        'all_series': models.Series.objects.all()
    }
    return render(request,"show.html",context)

def create(request):
    return render (request, 'create.html') 


def create_object(request):
    if request.method == "POST":
        title = request.POST ['title']
        network = request.POST ['network']
        release_date = request.POST ['release_date']
        desc = request.POST ['desc']

        series_id=models.add_new(title,network,release_date,desc)

        return redirect('/shows/'+str(series_id))

def render_create(request, id):
    all_series = models.Series.objects.get(id = id)

    context = {
            'id':all_series.id,
            'title': all_series.title,
            'network':all_series.network,
            'release_date': all_series.release_date,
            'desc':all_series.desc
        }
    return render(request, 'sucsses.html', context)


def edit (request, id):
    show_to_update = shows.objects.get(id=id)
    context={ "show" : show_to_update}
    if request.method == "POST":
            title = request.POST ['title']
            network = request.POST ['network']
            release_date = request.POST ['release_date']
            desc = request.POST ['desc']

        
    
    return render(request,"edit.html", context)


     