from django import forms
from media.models import Video
from media.videoBLL import VideoBLL


class Formulario(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Formulario, self).__init__(*args, **kwargs)
        self.fields['arquivo'].required = False
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta():
        model = Video
        fields = ['nome',
                  'arquivo'
                  ]

    def save(self, id_item=0):
        data = self.cleaned_data
        obj = VideoBLL()
        saida = obj.cad(data, id_item)
        return saida
