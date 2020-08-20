from django import forms
from android.models import allview,videomodel

class DocumentForm(forms.ModelForm):
    class Meta:
        model = allview
        fields = ('gameimg', 'title','desc' )


class videoform(forms.ModelForm):
    class Meta:
        model=videomodel
        fields = '__all__'
