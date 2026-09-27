from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime

# Create your views here.

def index(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),  # e.g., "Sep 19, 2026"
        "time": strftime("%I:%M %p", gmtime()),   # e.g., "02:06 PM"
    }
    return render(request,'index.html', context)

def time_display(request):
    return redirect ("/")