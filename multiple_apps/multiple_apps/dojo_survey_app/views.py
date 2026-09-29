from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
#def index(request):
    #return render(request,"index.html")

def show(request):
    if request.method== 'POST':
        name=request.POST['yourname']
        location=request.POST['dojolocation']
        fav_language=request.POST['favlanguage']
        message=request.POST['message']
        request.session['myname']=name

        context = {
            'name': name,
            'location': location,
            'fav_language': fav_language,
            'message': message
        }

    return render(request,'result.html',context)

def temp(request):
    return render (request,'temp.html')


def index(request):
    return HttpResponse("placeholder to display all the surveys created.")


def new(request):
    return HttpResponse("placeholder for users to add a new survey.")

