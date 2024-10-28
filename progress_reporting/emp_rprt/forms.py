from django import forms
from .models import Products


class UsernameLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)

class UploadFileForm(forms.Form):
    file = forms.FileField()
    
class dataEntryForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["title", "sku", "variant_quantity", "variant_colors", "sp" ,"cp", ]
    # title = forms.CharField(label="title", max_length=100)
    # sku = forms.CharField(label='sku', max_length=7)
    # variant_quantity = forms.IntegerField(label = 'quantity', min_value=0, max_value=1000)
    # sp = forms.IntegerField(label = 'sp', min_value=0, max_value=100000)
    # cp = forms.IntegerField(label = 'cp', min_value=0, max_value=100000)
    # variant_colors = forms.CharField(label='colors',max_length=100) 