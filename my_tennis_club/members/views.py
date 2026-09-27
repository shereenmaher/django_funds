from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# def members(request):
#     return render(request, 'myfirst.html')

def members(request):
    context={
        'mymembers': Member.objects.all()
    }
    return render(request,'all_members.html',context)

def details(request, id):
    mymember = Member.objects.get(id=id)

    context = {
        'mymember': mymember
    }

    return render(request, 'details.html', context)
  