from django.shortcuts import render,HttpResponse

# Create your views here.

def Home(request):
    return render(request,'Home.html')

def test(request):
    return HttpResponse("<H1>Hello World <br> This is My World Wide Web </H1>")

def History(request):
    return render(request,'History.html')

def hny(request):
    return render(request, 'hny.html')