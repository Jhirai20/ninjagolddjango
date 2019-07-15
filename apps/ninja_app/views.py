from django.shortcuts import render, redirect, HttpResponse
import random
# IF YOU USE SESSION YOU NEED TO MIGRATE YOUR OTHER METHODS!!!!!
# Create your views here.
def index(request):
    score=request.session.get('score',0)
    request.session['score']=score
    return render(request,'ninja_app/index.html')
def process_gold(request):
    if request.POST['whichbutton'] == 'farm':
        request.session['score']+=(int(random.randint(10, 20)))
    if request.POST['whichbutton'] == 'cave':
        request.session['score']+=(int(random.randint(5, 10)))
    if request.POST['whichbutton'] == 'house':
        request.session['score']+=(int(random.randint(2, 5)))
    if request.POST['whichbutton'] == 'casino':
        request.session['score']+=(int(random.randint(-50, 50)))
    return redirect('/')