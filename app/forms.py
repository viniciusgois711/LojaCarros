from django import forms
from . import models


class AppForm(forms.Form):
    class Meta:
        model: models.Usuarios
        fields = '__all__'


class CarrosForm(forms.Form):
    class Meta:
        model: models.Carros
        fields = '__all__'
