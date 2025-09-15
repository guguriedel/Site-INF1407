from django import forms
from .models import Filme
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class FilmeModel2Form(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'nota', 'duracao_em_segundos', 'genero', 'data_publicacao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracao_em_segundos': forms.NumberInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_data_publicacao(self):
        data = self.cleaned_data.get('data_publicacao')
        if data and data < date(1888, 1, 1):
            raise ValidationError(_('Data de publicação inválida. Deve ser a partir de 1888.'))
        return data
    def clean_ano_lancamento(self):
        ano = self.cleaned_data.get('ano_lancamento')
        if ano < 1888 or ano > 2100:
            raise ValidationError(_('Ano de lançamento inválido. Deve estar entre 1888 e 2100.'))
        return ano

    def clean_avaliacao(self):
        avaliacao = self.cleaned_data.get('avaliacao')
        if avaliacao < 1 or avaliacao > 10:
            raise ValidationError(_('Avaliação deve estar entre 1 e 10.'))
        return avaliacao

