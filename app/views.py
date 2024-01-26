from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from . import models

def login(request):
    if request.method == 'POST':

        form = forms.AppForm(request.POST)

        if form.is_valid():
            form.save()        
        return redirect('.')

    return render(request, "pages/login.html")


def gerenciamento(request):

    carros_list = models.Carros.objects.all()
    
    return render(request, "pages/gerenciamento.html", {'carros' : carros_list})


def add_veiculo(request):

    return render(request, "pages/add_veiculo.html")