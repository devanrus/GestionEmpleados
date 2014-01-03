from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from empleados.apps.login.forms import LoginForm


def loginview(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm (request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login (request,usuario)
                    return HttpResponseRedirect ('/')
                else:
                    mensaje = "El nombre de usuario o password son incorrectos"
        form = LoginForm()
        ctx = {'form' : form , 'mensaje' : mensaje}
        return render_to_response ('login/index.html',ctx,context_instance = RequestContext(request))

def logoutview(request):
    logout (request)
    return HttpResponseRedirect('/')
