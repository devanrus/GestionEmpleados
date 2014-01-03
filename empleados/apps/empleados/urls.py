from django.conf.urls import patterns, url


urlpatterns = patterns ('empleados.apps.empleados.views',
    url (r'^$','home', name ='vista_principal'),
    url (r'^empleados/nuevo/$','nuevo_empleado', name = 'vista_nuevoempleado'),
    url (r'^empleados/generar_reporte/$','generar_pdf', name = 'vista_generarpdf'),
    url (r'^empleados/editar/(?P<id_empleado>.*)/$', 'editar_empleado', name = 'vista_editarempleado'),
)
