from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models

def login(request):

    return render(request, "pages/login.html")


def gerenciamento(request):

    carros_list = models.Carros.objects.all()
    
    return render(request, "pages/list_veiculo.html", {'carros' : carros_list})


def add_veiculo(request):
    if request.method == 'POST':

        form_carros = forms.CarrosForm(request.POST, request.FILES)

        if form_carros.is_valid():
            form_carros.save()

            return redirect(to='app:gerenciamento')
        
    else:
        form_carros = forms.CarrosForm()

    return render(request, "pages/add_veiculo.html", {'form_carros':form_carros})


def edit_veiculo(request, id):
    try:
        carro = models.Carros.objects.get(id=id)
    except models.Carros.DoesNotExist:
        HttpResponse('Não foi possivel editar')
    
    if request.method == 'POST':
        form_carros = forms.CarrosForm(request.POST, request.FILES, instance=carro)

        if form_carros.is_valid:
            form_carros.save()
            return redirect('app:gerenciamento')
        else:
            HttpResponse('Erro')
    
    else:
        form_carros = forms.CarrosForm(instance=carro)      

    return render(request, "pages/edit_veiculo.html", 
                  {'form_carros':form_carros,
                   'carro':carro})

def remove_veiculo(request, id):

    carro = models.Carros.objects.get(id=id)
    carro.delete()

    return redirect(to='app:gerenciamento')

def detalhes_veiculo(request, id):

    carro = get_object_or_404(models.Carros, pk=id)

    return render(request, "pages/detalhes_veiculo.html", {'carro': carro})
