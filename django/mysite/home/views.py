from ast import Name
from datetime import datetime
from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# context={
#         "variable":"This is variable"
# }
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is homePage")
def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is About Page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is services Page")

def contact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email= email , phone =phone , desc =desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Thanks For Filling Out the form!')
    return render(request,'contact.html')
    #return HttpResponse("This is Contact Page")

