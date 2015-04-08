from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    file = forms.FileField()
