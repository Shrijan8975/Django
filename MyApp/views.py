from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("Hello World")

def demoHtml(request):
    return render(request,"demo.html",{})

def loginDemo(request):
    return render(request,"login.html",{})

def verifyData(request):
    
    uname = request.GET["uname"]
    pwd = request.GET["pwd"]
    if(uname == "Shrijan" and pwd == "Chavan123"):
        return HttpResponse("login successful...")
    else:
        return HttpResponse("login failed...")

def demodata(request):
    uname = "shrijan"
    return render(request,"welcome.html", {"username":uname})

def demoData1(request):
    uname = "shrijan"
    location = "pune"
    age = 26
    return render(request,"display.html", {"uname":uname,"location":location,"age":age})