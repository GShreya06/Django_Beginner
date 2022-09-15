from multiprocessing import context
from django.shortcuts import render , HttpResponse
context={
        "variable":"This is variable"
}
# Create your views here.
def index(request):
    return render(request,'index.html',context)
    #return HttpResponse("This is homePage")
def about(request):
    return render(request,'about.html',context)
    #return HttpResponse("This is About Page")

def services(request):
    return render(request,'services.html',context)
    #return HttpResponse("This is services Page")

def contact(request):
    return render(request,'contact.html',context)
    #return HttpResponse("This is Contact Page")

