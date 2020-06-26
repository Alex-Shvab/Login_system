import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from login import models
from .forms import TelNumberForm, FirstUserRegForm, NewUserRegForm


__otp_passwort = 0

def otp_pas():
    r = random.randint(1000, 10000)
    global __otp_passwort
    __otp_passwort = r
    return r


def tel_number(request):
    if request.method == 'POST':
        v = otp_pas()
        print(v)
        if not models.User.objects.all().count():
            return redirect('first_user')
        elif not models.User.objects.get(tel_number=tel_number):
            return redirect('new_user')

    else:
        form = TelNumberForm()
    return render(request, 'login/tel_number.html', {'form': form})


def first_user(request):
    if request.method == 'POST':
        form = FirstUserRegForm(request.POST)
        if form.is_valid():
            taken_otp = int(request.POST.get('otp_pas'))
            print(taken_otp)
            if taken_otp == __otp_passwort:
                print("Yes")
                form.save()
                print("save")
                return redirect('tel_login')
            else:
                return redirect('tel_login')
        else:
            print("NO")

    else:
        form = FirstUserRegForm()
        return render(request, 'login/first_user.html', {'form': form})


def new_user(request):
    if request.method == 'POST':
        form = NewUserRegForm(request.POST)
        if form.is_valid():
            taken_otp = int(request.POST.get('otp_pas'))
            print(taken_otp)
            if taken_otp == __otp_passwort:
                print("Yes")
                form.save()
                print("save")
                return redirect('tel_login')
            else:
                return redirect('tel_login')
        else:
            print("NO")

    else:
        form = NewUserRegForm()
        return render(request, 'login/new_user.html', {'form': form})
