from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        'variable1':"this is sent",
        'variable2':"Nilesh is great"
    }
    return render(request,'index.html', context)
 # return HttpResponse("This is home page")


def about(request):
    return HttpResponse("this is about page")
def login(request):
    return render(request,'login.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def services(request):
    return HttpResponse("this is services page")

  
    
