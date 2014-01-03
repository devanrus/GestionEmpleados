from django.conf.urls import patterns, url

urlpatterns = patterns ('empleados.apps.login.views',
    url (r'^login/$','loginview', name ='vista_login'),
    url(r'^logout/$','logoutview',name='vista_logout'),
)
