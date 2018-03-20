from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForms, LoginForm, RegisterForm


def home_page(request):

    #print(request.session.get("first_name","Unknown"))
    context={
        "start" : "You have just learnt about contexts.",
    }
    if request.user.is_authenticated:
        context["premium_content"]="You are seeing the premium content."
    return render(request,"home_page.html",context)

def about_page(request):
    context={
        "start": "You just learnt more about contexts"
    }
    return render(request,"home_page.html",context)

def contact_page(request):
    contact_form= ContactForms()
    context={
        "title": "Contact",
        "start":"We will make form here and yeah you are awesome.",
        "form": contact_form
    }
    if request.method=="POST":
        print(request.POST)
    return render(request,"contact/view.html",context)


def login_page(request):
    form= LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.user.is_authenticated)
        if user is not None:
                print(request.user.is_authenticated)
                login(request, user)
                #context['form'] = LoginForm
                return redirect("/login")
        else:
                print("Error")
    return render(request,"auth/login.html",context)



User= get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        new_user  = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/register.html", context)



html_=""""<!DOCTYPE html>
<html>
<body>

<p>This is a paragraph.</p>
<p>This is another paragraph.</p> skfjsoifjpoijfposjfspofsajfpsf
Heyya! I wanna be closer to you.

</body>
</html>"""

def home_page_old(request):
    return HttpResponse(html_)

