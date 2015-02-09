# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from form import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.generic.list import ListView 
from aparelhos.models import Aparelho

# Create your views here.

def create(request):
    if request.POST:
        form = AparelhoForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('inicio.html','')
        else:
            messages.error(request, 'É preciso Informar todos os campos')
            
    else:
        form = AparelhoForm()
        
    return redirecionaComArgumento(request,form, 
                                   'Aparelho',
                                   'Para Cadastrar um aparelho você deve informar uma descrição e uma categoria',
                                   '/aparelho/create/',
                                   '/aparelho/create/',
                                   '/aparelho/create/',
                                   'novoAparelho.html')

def createCategoria(request):
    if request.POST:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('inicio.html','')
        else:
            messages.error(request, 'É preciso Informar todos os campos')
            
    else:
        form = CategoriaForm()
        
    return redirecionaComArgumento(request,form, 
                                   'Categoria',
                                   'Informe todos os Campos',
                                   '/categoria/create/',
                                   '/categoria/create/',
                                   '/categoria/create/',
                                   'novaCategoria.html')

def createExercicio(request):
    if request.POST:
        form = ExercicioForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('inicio.html','')
        else:
            messages.error(request, 'É preciso Informar todos os campos')
            
    else:
        form = ExercicioForm()
        
    return redirecionaComArgumento(request,form, 
                                   'Exercício',
                                   'Informe os dados necessários para o execício',
                                   '/exercicio/create/',
                                   '/exercicio/create/',
                                   '/exercicio/create/',
                                   'novaCategoria.html')

class listarAparelho(ListView):
    queryset = Aparelho.objects.all()
    template_name = 'aparelhos.html'
    model = Aparelho
    




def redirecionaComArgumento(request,form, model, epigrafo, acaopost, acaosalvar,acaovoltar,html):
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    args['model'] = model
    args['epigrafo'] = epigrafo
    args['acapost'] = acaopost
    args['acaosalvar'] = acaosalvar
    args['acaovoltar'] = acaovoltar
    
    return render_to_response(html,args)
    
    

