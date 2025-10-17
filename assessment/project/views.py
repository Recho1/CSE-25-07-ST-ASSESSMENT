from django.shortcuts import render

# Create your views here.
def signupage(request):
    return render(request,"signup.html")


def loginpage(request):
    return render(request,"index.html")

def afterpage(request):
    return render(request,"login.html")