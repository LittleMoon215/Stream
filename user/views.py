from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from user.forms import RegistrationForm
from streampage.views import index


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            username = form.data["username"]
            password = form.data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next is not None:
                    return redirect("index")
                else:
                    return redirect("index")
            else:
                return render(request, "main.html", {"message": "Неверный логин или пароль"})
    else:
        return redirect("main")

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, 'register.html', context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")