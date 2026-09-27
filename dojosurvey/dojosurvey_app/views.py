from django.shortcuts import render ,redirect
from django.http import HttpResponse,JsonResponse
from .models import*
# Create your views here.
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def some_function(request):
    if request.method == "GET":
        print("A GET request is being made to this route")
        return render(request, "some_template.html")

    if request.method == "POST":
        print("A POST request is being made to this route")
        return redirect("/")