from django.shortcuts import render, redirect
from .models import *
from .forms import *
import requests
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def backend(request):
    return render(request,'backend.html')

def frontend(request):
    return render(request,'frontend.html')

def programing(request):
    return render(request,'programing.html')

def both(request):
    return render(request,'both.html')

otp=0
def signup(request):
    if request.method=='POST':
        newuser=signupfrom(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            
            # OTP Sending Code
            global otp
            otp=random.randint(1111,9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"gWMAeKq0ExoPnDvUiHGbj1OJsF9aC8yB7dR6L254hVcXrfNmQTc1NKT34eJrdkRYMFqlHwSsLAfmCZ70","variables_values":f"{otp}","route":"otp","numbers":f"{request.POST['Phone']}"}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            print("Your OTP is:",otp)
            return redirect('OTP')
            
        else:
            print("User is not add")
        
    return render(request,'signup.html')

def signin(request):
    return render(request,'Signin.html')

def videos(request):
    return render(request,'video.html')

def OTP(request):
    global otp
    msg=""
    print("Your OTP is:",otp)
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            print("otp verify successfully!")
            return redirect('signup')
        else:
            print("Verification faild..Try again!")
    return render(request,'OTP.html')