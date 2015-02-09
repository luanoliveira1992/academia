from django import forms
from models import *

class AparelhoForm(forms.ModelForm):
    
    class Meta:
        model = Aparelho
        
class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = CategoriaAparelho
        
class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio