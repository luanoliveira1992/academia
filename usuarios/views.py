from django.shortcuts import render,render_to_response
from django.views.generic import ListView
from .models import Usuario
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('home.html',c)

@csrf_exempt
def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

@csrf_exempt    
def loggedin(request):
    return render_to_response('inicio.html',
                              {'full_name': request.user.username})
@csrf_exempt
def invalid_login(request):
    return render_to_response('home.html')

@csrf_exempt
def logout(request):
    auth.logout(request)
    return render_to_response('home.html')


class IndexView(ListView):
	template_name= 'index.html'
	model = Usuario
    

    
