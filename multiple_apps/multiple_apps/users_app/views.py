from django.shortcuts import render,redirect,HttpResponse
from . import models

# Create your views here.
def createuser(request):
    if request.method == 'POST':
        models.create_newuser(request.POST)
        return redirect('/viewuser')
    else:
        context = {
            "users": models.get_users()
        }
        return render(request, "users.html", context)
      
    
def viewuser(request):
    context={
        "users":models.get_users()
    }
    return render(request,"users.html",context)

def delete_user(request, user_id):
    user = models.User.objects.get(id=user_id)
    user.delete()

    return redirect("/")

def register(request):
    return HttpResponse("placeholder for users to create a new user record.")


def login(request):
    return HttpResponse("placeholder for users to log in.")


def index(request):
    return HttpResponse("placeholder to display all the list of users later.")