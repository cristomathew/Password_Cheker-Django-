from django.shortcuts import render
from . import checker123 as ck
# Create your views here.
def home(request):
    return render(request,'home.html')
def check(request):
    if request.method == 'POST':
        password = request.POST['password']
        r,a = ck.check(password)
        context = {
            'result': r,
            'c': a
        }
        return render(request,'home.html',context)
def handler404(request,*args, **argv):
    return render(request, '404.html', status=404)