from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 0

    return render(request, 'counter.html')

def add_two(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 0

    return redirect('/')

def increment(request):
    if request.method == 'POST':
        increment_value = int(request.POST['inc_val'])

        if 'count' in request.session:
            request.session['count'] += increment_value-1
        else:
            request.session['count'] = increment_value

    return redirect('/')

def destroy_session(request):
    del request.session['count']
    return redirect('/')