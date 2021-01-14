from django.shortcuts import render, redirect
from .user_decorators import unauthenticated_user
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


@unauthenticated_user
def user_login(request):
    return render(request, 'users/login.html')


def process_login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        try:
            auth_user = authenticate(username=uname, password=pwd)
        except Exception as e:
            messages.error(request, "Invalid Crendentials")
            return redirect("users:user_login")
        try:
            login(request, auth_user)
            return redirect("booker:dashboard")
        except Exception as e:
            messages.error(request, "Invalid Crendentials")
            return redirect("users:user_login")

    return HttpResponse("Glass Nkoaa!!!")


def sign_out(request):
    logout(request)
    return redirect("users:user_login")