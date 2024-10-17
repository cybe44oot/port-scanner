from django import forms
from .models import Request, Result
class RequestForm(forms.ModelForm):
    class Meta:
       model = Request
       fields= ['ip','start_port','end_port']
    
class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields='__all__'
        