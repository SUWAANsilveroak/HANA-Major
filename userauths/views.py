from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from userauths.forms import UserRegisterForm

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            # Authenticate the new user
            new_user = authenticate(username=email, password=password)
            if new_user:
                # Login the user
                login(request, new_user)
                messages.success(request, f"Hey {new_user.username}, your account was created successfully")
                # Redirect to the desired URL after successful login
                return redirect("core:index")
            else:
                messages.error(request, "Failed to authenticate. Please try logging in.")
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, "userauths/sign-up.html", context)
