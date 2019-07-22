from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
import pdb
import json
from . import db
# from .models import Login,UserData,Admin
from .  import models
from django.contrib import auth
from django.core import serializers
import os
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import random
import string
import boto3

@csrf_exempt
def registerhtml(request):
    return render(request,'basicapp/register.html')

@csrf_exempt
def save_user(request):
	pdb.set_trace()
	print(request.POST)
	print(request.body)
	try:
		data = json.loads(request.body.decode('utf-8'))
	except Exception as e:
		data = request.POST  
	first_name=data.get('name')
	email=data.get('email')
	dob=data.get('dob')
	password=data.get('password')
	phone_no=data.get('phone_no')


        

	if(first_name  and email and dob and password and phone_no):

		user_exist=db.check_if_user_exist(email)
		if type(user_exist)==dict:
			UserDetails=db.createuser(first_name,email,dob,phone_no,password)
                # ------ Create User Directory ---------
          

			return JsonResponse({"status":"1","message":"User successfully created"},status=200)                
            
		else:
			return JsonResponse({"status":"0","message":"User already exist"},status=400)

        
	else:
		return JsonResponse({"status":"0","message":"fill all the details"},status=400)




def randomStringDigits2(stringLength):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def sendsms(phnno):
    print("Yes11")
    genrandomnumber=randomStringDigits2(4)
    msg=genrandomnumber
    phno=phnno
    sendmsg(msg,phno)
    return msg

@csrf_exempt
def verifymobile(request):
	# pdb.set_trace()
	try:
		data = json.loads(request.body.decode('utf-8'))
	except Exception as e:
		data = request.POST  
	phno=data.get('phone')
	phnno=str(phno)
	otp=sendsms(phnno)
	if sendsms:
		return JsonResponse({"status":"1","message":" successfully ","OTP":otp},status=200)
	return JsonResponse({"status":"0","message":"unsuccessful"},status=400)  

def sendmsg(msg,phno):
	client = boto3.client(
    "sns",
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name=""
)

#Send your sms message.
	client.publish(
	    PhoneNumber='91'+phno,
	    Message=msg
	)
   

