from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import*
import random
# Create your views here.
def index(request):
    request.session.setdefault("gold",0)
    request.session.setdefault("history",[])
    return render(request,"ninjagold_app/index.html",{"gold":request.session["gold"],"history":request.session["history"]})

def gold_counter(request):
    if request.method == "POST":
        request.session.setdefault("gold",0)
        request.session.setdefault("history",[])
        place=request.POST.get("place")
        if place == "farm":
            earned_gold=random.randint(10,20)
            request.session["gold"]+=earned_gold
            message=f"you earned{earned_gold} from {place}"
        elif place == "cave":
            earned_gold=random.randint(10,20)
            request.session["gold"]+=earned_gold
            message=f"you earned{earned_gold} from {place}"
        
        elif place == "house":
            earned_gold=random.randint(10,20)
            request.session["gold"]+=earned_gold
            message=f"you earned{earned_gold} from {place}"
        
        elif place == "quest":
            earned_gold=random.randint(-50,50)
            request.session["gold"]+=earned_gold
            message=f"you earned{earned_gold} from {place}"

        request.session["history"].append({"text":message})
        request.session.modified=True
    return redirect("/")
        
        
