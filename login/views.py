from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponseRedirect
# Create your views here

def home(request):
	return render_to_response("home.html",locals(), context_instance=RequestContext(request))

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'home.html', c)

def auth_view(request):
    username = request.POST.get('emailLogin', '')
    password = request.POST.get('senhaLogin', '')
    if(username is not None and password is not None):
       return HttpResponseRedirect('inicio.html')
    else:
       return HttpResponseRedirect('vazio.html')
    """user = auth.authenticate(username = username, password = password)      

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/templates/vazio')
    else:
        return HttpResponseRedirect('/templates/vazio')"""
	
