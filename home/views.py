from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1':"this is sent",
        'variable2':"Nilesh is great"
    }
    return render(request,'index.html', context)
 # return HttpResponse("This is home page")


def about(request):
    return HttpResponse("this is contact page")

def contact(request):
    return render(request,'/form/index.html')

def services(request):
    return HttpResponse("this is services page")

  
    
