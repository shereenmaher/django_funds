from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "name" : "shereen",
        "fav_color": "violet",
        "pets":["Bruce","Fitz","dogo"]
    }
    return render(request,'index.html',context)
