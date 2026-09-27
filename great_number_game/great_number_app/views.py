from django.shortcuts import render,HttpResponse,redirect
import random

def index(request):
    return render(request,'index.html')


def guess(request):
    if request.method == 'POST':
       #if there's no random in the session create one
        if 'mynumber' not in request.session:
            true_number=random.randint(1,100)
            request.session["mynumber"]=true_number
        else:
            #get the existing random from the session
            true_number=(request.session["mynumber"])

        guess_number=int(request.POST['number'])

        if guess_number == true_number:
            message=f"{guess_number} was the number!"
            gameover=True

        elif guess_number > true_number:
            message="Too high!"
            gameover=False

        else:
            message="Too low!"
            gameover=False

        return render(request, 'index.html', {
            'message': message,
            'gameover': gameover
        })

    return redirect("/")

def playagain(request):
    del request.session['mynumber']
    return redirect('/')
