from django.shortcuts import render
from django.views.generic import ListView

from .models import Usuario

class IndexView(ListView):
	template_name= 'index.html'
	model = Usuario