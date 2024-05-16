from django import forms
from core.models import Artigo, Arquivo

class MultipleFileInput(forms.ClearableFileInput):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs['multiple'] = True

class ArtigoForms(forms.ModelForm):
    arquivos = forms.FileField(widget=MultipleFileInput())

    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo', 'arquivos', 'tipo']

    def save(self, commit=True):

        artigo = super(ArtigoForms, self).save(commit=False)
        if commit:
            artigo.save()

        files = self.cleaned_data['arquivos']
        print(files)
        for file in files:
            arquivo = Arquivo.objects.create(
                file=file
            )

            artigo.arquivos.add(arquivo)
            artigo.save()

        return artigo
