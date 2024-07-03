from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from carint import settings
import random
import requests


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

otp=0

def signup(request):
    msg=""
    if request.method=='POST':
        newuser=user(request.POST)
        if newuser.is_valid():
            Email=newuser.cleaned_data.get('Email')
            try:
                newUser.objects.get(Email=Email)
                msg="Username is Already exist!"
            except newUser.DoesNotExist:
                newuser.save()
                msg="Signup SuccessFully"
    # OTP Verification
    global otp
    otp=random.randint(1111,9999)
    
    import requests

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"eKq0ExoPnDvUiHGbj1OJsF9aC8yB7dR6L254hVcXrfNmQTc1NKT34eJrdkRYMFqlHwSsLAfmCZ70","variables_values":f"{otp}","route":"otp","numbers":f"{request.POST['Mobile']}"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return render(request,'signup.html')