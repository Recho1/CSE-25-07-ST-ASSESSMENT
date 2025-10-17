from django.shortcuts import render,redirect
from project.models import Signup

# Create your views here.
def signupage(request):
    if request.method == "POST":
        form_data = request.POST
        sent_fullname = form_data.get('fullname')
        sent_email = form_data.get('email')
        sent_phonenumber = form_data.get('phonenumber')
        sent_password = form_data.get('password')
        

        new_account = Signup()
        new_account.fullname = sent_fullname
        new_account.email = sent_email
        new_account.phonenumber = sent_phonenumber
        new_account.password = sent_password
        
        new_account.save()
    return render(request,"signup.html")


def loginpage(request):
    return render(request,"index.html")

def afterpage(request):
    return render(request,"login.html")