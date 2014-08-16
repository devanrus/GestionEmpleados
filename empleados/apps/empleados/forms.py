from django import forms
from empleados.apps.empleados.models import Empleado


class NuevoEmpleado (forms.ModelForm):

    class Meta:
        model = Empleado
        exclude = {'vencido',}

    def __init__(self, *args, **kwargs):
        super(NuevoEmpleado, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
        self.fields['apellido_paterno'].widget.attrs.update({'class' : 'form-control'})
        self.fields['apellido_materno'].widget.attrs.update({'class' : 'form-control'})
        self.fields['cargo'].widget.attrs.update({'class' : 'form-control'})
        self.fields['fecha_ingreso'].widget.attrs.update({'class' : 'form-control','id':'datepicker','placeholder': 'Ejemplo: 12/06/2013'})
        self.fields['fecha_fin'].widget.attrs.update({'class' : 'form-control','id':'datepicker2','placeholder': 'Ejemplo: 25/02/2014'})

    observaciones = forms.CharField (widget=forms.Textarea(attrs={'rows':4,'class':'form-control input-xlarge'}))


class EditarEmpleado (NuevoEmpleado):

    pass


class RangoForm (forms.Form):
    fecha_i = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'datepicker'}))
    fecha_f = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'datepicker2'}))
