from django import http
from django.template.loader import get_template
from django.template import Context
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
import cgi
from datetime import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from empleados.apps.empleados.forms import NuevoEmpleado, EditarEmpleado, RangoForm
from empleados.apps.empleados.models import Empleado
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request):
    mes = datetime.now().month
    verifica_status(Empleado.objects.filter (fecha_fin__month = mes,vencido=1)) #Funcion para verificar el status
    empleados = Empleado.objects.filter (fecha_fin__month = mes).order_by('fecha_fin')
    return render_to_response ('index.html',{'empleados' : empleados},context_instance=RequestContext(request))


@login_required(login_url='/login')
def nuevo_empleado(request):
    if request.method == "POST":
        formempleado = NuevoEmpleado(request.POST)
        if formempleado.is_valid():
            formempleado.save()
            return render_to_response('empleados/agregado.html', context_instance=RequestContext(request))
    else:
        formempleado = NuevoEmpleado()
    context = {'formempleado':formempleado}
    return render_to_response ('empleados/nuevo.html',context,context_instance=RequestContext(request))


@login_required(login_url='/login')
def editar_empleado (request, id_empleado):
    empleado = Empleado.objects.get(pk=id_empleado)
    if request.method == "POST":
        formedit = EditarEmpleado(request.POST, instance=empleado)
        if formedit.is_valid():
            formedit.save()
            return HttpResponseRedirect('/')

    formedit = EditarEmpleado(instance=empleado)
    return render_to_response('empleados/editar.html',{'formempleado' : formedit}, context_instance=RequestContext(request))


def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            mimetype='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))

@login_required(login_url='/login')
def generar_pdf(request):
    if request.method == "POST":
        formbusqueda = RangoForm(request.POST)
        if formbusqueda.is_valid():
            fecha_in = formbusqueda.cleaned_data['fecha_i']
            fecha_fi = formbusqueda.cleaned_data['fecha_f']
            rango = Empleado.objects.filter(fecha_fin__range=(fecha_in, fecha_fi)).order_by('nombre')
            return write_pdf ('empleados/pdf.html',{'pagesize' : 'legal', 'rango' : rango})
            #return render_to_response ('empleados/test.html',{'rango':rango},context_instance=RequestContext(request))
        else:
            error = "Hay un error en las fechas proporcionadas"
            return render_to_response('empleados/reporte_pdf.html', {'error': error}, context_instance=RequestContext(request))

    return render_to_response('empleados/reporte_pdf.html', {'rangoform': RangoForm()}, context_instance=RequestContext(request))

"""
    CADA VEZ QUE EL USUARIO INGRESE EL INICIO DE LA PAGINA, ESTA FUNCION SE ENCARGA DE VERIFICAR
    LOS USUARIOS QUE VENCEN AL DIA ACTUAL.
"""
def verifica_status(datos):
    hoy = date.today()
    for array in datos:
        if array.fecha_fin <= hoy:
            array.vencido = 0
            array.save()
