from django.shortcuts import render, redirect

# Create your views here.
def count(request):
    if 'count' not in request.session:
            request.session['count'] = 1
    else:
        request.session['count'] += 1
    
    return render (request,'index.html')

def destroy(request):
    request.session.clear()
    # del request.session['count']
    return redirect('/')

def increment(request):
    request.session['count'] +=1
    return redirect('/')
    # return HttpResponse("increment")      , HttpResponse
    # return redirect(request,'index.html')

def incrementByNum(request):
    if request.method=='POST':
        number= int(request.POST['buttonNum'])
        request.session['count'] +=number-1
        return redirect('/')
