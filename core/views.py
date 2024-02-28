from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import *
import datetime
import bcrypt

# Create your views here.

def encrypt(password):
    salt = bcrypt.gensalt(rounds=12)

    password = str.encode(password)

    xpass = bcrypt.hashpw(password, salt)

    new = xpass.decode()

    return new


def passwordCheck(password, saved):
    x = str.encode(saved)

    salt = bcrypt.gensalt(rounds=12)

    xpass = bcrypt.hashpw(password, salt)

    same = bcrypt.checkpw(password, x)


def index(request):
    return JsonResponse({"hello": True})


def apiSignup(request):
    name = request.GET.get("name")
    email = request.GET.get("email")
    password = request.GET.get("password")
    dob = request.GET.get("dob")

    try:
        inst = Users.objects.get(email=email)
        return JsonResponse({"message":"User with this email already exists."})

    except:
        x = dob.split("-")
        date = datetime.datetime(year=int(x[0]), month=int(x[1]), day=int(x[2]))
        Users(name=name, email=email, password=encrypt(password), dob=date).save()

        return JsonResponse({"message":"You have signed up successfully."})


    return HttpResponse(True)

