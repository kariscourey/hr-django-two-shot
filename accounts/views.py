from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def signup(request):
    # POST
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # UserCreationForm saves username and password to db
            user = form.save()
            # # Get user credentials
            # username = request.POST.get("username")
            # password = request.POST.get("password1")
            # user = User.objects.create_user(
            #     username=username, password=password
            # )
            # Login
            login(request, user)
            # Redirect somewhere
            return redirect("registration_list")
    # GET
    else:
        form = UserCreationForm()

    context = {
        "form": form,
    }

    return render(request, "registration/signup.html", context)
