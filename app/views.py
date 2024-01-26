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
    if request.method == 'POST':

        form_carros = forms.CarrosForm(request.POST, request.FILES)

        if form_carros.is_valid():
            form_carros.save()

            return redirect(to='app:gerenciamento')
        
    else:
        form_carros = forms.CarrosForm()

    return render(request, "pages/add_veiculo.html", {'form_carros':form_carros})