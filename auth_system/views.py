from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("reviews-list")
    else:
        form = UserCreationForm()

        context = {
            "form": form
        }

    return render(
        request,
        "auth_system/register-form.html",
        context
    )
            