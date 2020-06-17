from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/user.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html")

def logout_view(request):
      logout(request)
      return render(request, "orders/login.html", {"message": "Logged out."})

def register(request):
    if request.method == 'POST':
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            password_again = request.POST["password_again"]
            email = request.POST["email"]
        except KeyError:
            return render(request, "orders/error.html", {"message": "Please enter all required fields"})
        
        if password != password_again:
            # return render(request, "orders/error.html", {"message": "Passwords must match"})
            raise ValidationError('passwords must match')    

        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)

        return HttpResponseRedirect(reverse("index"))
    else: 
        return render(request, "orders/register.html")