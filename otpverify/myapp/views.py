from django.shortcuts import render
from .forms import *
from .models import *
import requests
import random


# Create your views here.
otp = 0
def index(request):
    if request.method=='POST':
        newuser=user_signup(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User is succefuly add")
            # return redirect('signin')
        #OTP Sending Code
            global otp
            otp=random.randint(1111,9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"gWMAeKq0ExoPnDvUiHGbj1OJsF9aC8yB7dR6L254hVcXrfNmQTc1NKT34eJrdkRYMFqlHwSsLAfmCZ70","variables_values":f"{otp}","route":"otp","numbers":f"{request.POST['mobile']}"}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            print("Your OTP is:",otp)
        else:
            print("User is not add")
    
    return render(request,'index.html')
