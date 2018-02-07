from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import ContactForms, LoginForm


def home_page(request):
    context={
        "start" : "You have just learnt about contexts."
    }
    return render(request,"home_page.html",context)

def about_page(request):
    context={
        "start": "You just learnt more about contexts"
    }
    return render(request,"home_page.html",context)

def contact_page(request):
    contact_form= ContactForms()
    context={
        "start":"We will make form here and yeah you are awesome.",
        "form": contact_form
    }
    if request.method=="POST":
        print(request.POST)
    return render(request,"contact/view.html",context)


def login_page(request):
    form = LoginForm(request.POST or None)
    print("User logged in")
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
    context={
        "form": form
    }
    return render(request,"auth/login.html",context)






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

