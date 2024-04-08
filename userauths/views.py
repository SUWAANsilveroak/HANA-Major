from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from userauths.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL


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


# Summary: This code defines a view function for user login.
# It checks if the user is already authenticated, processes the login form data, and handles user authentication. 
# It also includes error messages for invalid login attempts.

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request,f"Hey you are already logged in")
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
            return redirect("userauths:sign-in") # Redirect back to the sign-in page if user does not exist
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("core:index")  # Redirect to the home page after successful login
        else:
            messages.error(request, "Username or password is incorrect")
    
    context = {}
    return render(request, "userauths/sign-in.html", context)

def logout_view(request): 
    logout(request)
    messages.success(request,"logged-out succesfully")

    return redirect("userauths:sign-in")
    