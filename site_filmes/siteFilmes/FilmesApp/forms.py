from django import forms
from .models import Filme
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date 


class FilmeModel2Form(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'nota', 'duracao_em_horas', 'genero', 'data_publicacaolicacao']
        

    def clean_data_publicacaolicacao(self):
        data = self.cleaned_data.get('data_publicacaolicacao')
        if data and data < date(1888, 1, 1):
            raise ValidationError(_('Data de publicação inválida. Deve ser a partir de 1888.'))
        return data
