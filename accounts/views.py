from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as mylogin
from django.contrib.auth.decorators import login_required


def userlogin(request):
  if request.method=='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      mylogin(request, user)
      return redirect('registration:college')
  context = {}
  return render(request, 'registration/login.html', context)