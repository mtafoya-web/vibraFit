#render->returns HTML page with context data
#redirect->sends the browser to another url
#authenticate-> checks credentials
#login->stores the user in the session (logs them in)
#logout->clears the session
#messages->lets you attach messages like invalid password and show
#           them in html
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm #custom class

# Create your views here.
#request contains the incoming request data(GET/POST, cookies, user, session)
def login_view(request):
    ### request.user exist because of auth middleware ###
    ### .is_authenticated is True if user is logged in ###
    ### prevents logged in users from seeing the login screen again ###
    if request.user.is_authenticated:
        return redirect("dashboard")
    ### if the request is POST contains submitted form data ###
    ### if the request is GET request.POST is empty, so none ###
    form = LoginForm(request.POST or None)
    ### only authenticate when they submit the form ###
    if request.method == "POST":
        #runs form validation (required fields, max length, etc) ###
        #if invalid, re-render template and show errors
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                ### remember me line ####
                ### session ID is stored in a cookie in the browser ###
                ### future requests will have request.user set automatically ###
                login(request, user)

                next_url = request.GET.get("next") or request.POST.get("next")
                return redirect(next_url or "/dashboard/")
                ### if user tried to access a protected page ###
                ### django redirectsthem to /login/?next=/that-page/ ###
                ###request.GET.get("next") reads that value Redirect back to it if it exists; otherwise go to dashboard
            else:
                ### Always returns the login page for GET, or for failed login attempts.###
                messages.error(request, "Invalid username or password")
                ### Sends form into the template so you can render inputs. ###
                return render(request, "login/login.html", {"form":form})
        else:
            messages.error(request, "Please enter both username and password")
            
    return render(request, "login/login.html",{"form":form})

def logout_view(request):
    ### clears session data ###
    logout(request)
    ### redirect back to the login page ###
    return redirect("login")

def home_redirect(request):
    return redirect("login")

@login_required
def dashboard(request):
    return render(request, "login/dashboard.html")
            