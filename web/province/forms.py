from django import forms
from orm.models import Province

class ProvinceForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    nama = forms.CharField(max_length=100)

    class Meta:
        model =  Province
