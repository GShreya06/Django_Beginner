from multiprocessing import context
from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    context={
        "variable":"This is variable"
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is homePage")
def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is services Page")

def contact(request):
    return HttpResponse("This is Contact Page")

