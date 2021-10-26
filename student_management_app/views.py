from django.contrib.auth import login, logout
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from .EmailBackEnd import EmailBackEnd
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages



# Create your views here.
def showDemo(request):
    return render(request, 'hod_template/home_content.html')

def ShowLogin(request):
    return render(request, 'login_page.html')

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2> Method is not allowed </h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request,user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse("home_admin"))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "4":
                return HttpResponse("Hello School admn")
            elif user.user_type == "5":
                return HttpResponseRedirect(reverse("deo_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
            #return HttpResponse("Email: " +request.POST.get("email")+ "Password: "+request.POST.get("password"))
        else:
            messages.error(request, "Wrong Username or Password")
            return HttpResponseRedirect('/')

def getuserDetails(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+ " usertype: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")