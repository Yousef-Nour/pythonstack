import random
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if 'gold' not in request.session: 
        request.session['gold'] = 0   #gold=0
    
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    # context = {
    #     'gold': request.session['gold']
    # }
    return render(request,'index.html')

def process(request):

    
    if request.POST['place'] == 'Farm':
        num = random.randint(10, 20)
        s = f"Earned {num} from the farm"
        request.session['gold'] += num
        request.session['activities'].append(s)
    
    if request.POST['place'] == 'Cave':
        num = random.randint(5, 10)
        s = f"Earned {num} from the Cave"
        request.session['gold'] += num
        request.session['activities'].append(s)

    if request.POST['place'] == 'House':
        num = random.randint(2, 5)
        s = f"Earned {num} from the House"
        request.session['gold'] += num
        request.session['activities'].append(s)

    if request.POST['place'] == 'Casino':
        num = random.randint(-50, 50)
        request.session['gold'] += num
        if num > 0:
            s = f"Entered a Casino and earned {num} golds"
        elif num < 0 :
            s = f"Entered a Casino and lost {num} golds"
        else:
            s = f"Entered a Casino and left with the same amount of golds"

        request.session['activities'].append(s)



    return redirect('/')

    



