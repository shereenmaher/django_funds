from django.shortcuts import render , HttpResponse,redirect
from .models import *
from django.contrib import messages
# Create your views here.


def register(request):
    
def index(request):
    return render (request,"index.html")

def create_participant(request):
    if request.method == "POST":
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        phonenumber = request.POST["phonenumber"]
        startdate = request.POST["start_date"]
        enddate = request.POST["end_date"]
        print(firstname)
        context = {
                "firstname": first_name,
                "lastname": last_name,
            }
        return render(request, "show.html", context)
         
    
    else : 
        return HttpResponse("error")
 