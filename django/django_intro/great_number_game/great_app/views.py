import random
from django.shortcuts import redirect, render

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)

    if 'color' in request.session and 'string' in request.session :
        context = {
            'color': request.session['color'],
            'string': request.session['string']
        }
    else :
        context = {
            'color': 'white',
            'string': ""
        }

    return render(request,'index.html', context)

def process(request):
    if request.method == 'POST':
        number = request.session['number']
        guess = int(request.POST['guess'])


        if guess == number:
            request.session['color'] = 'green'
            request.session['string'] = f"{number} was the number!"
            
        elif guess > number:
            request.session['color'] = 'red'
            request.session['string'] = "Too high!"
            

        else:
            request.session['color'] = 'red'
            request.session['string'] = "Too low!"
    
    
    return redirect('/')