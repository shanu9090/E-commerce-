
# from application.models import Customer
# from django import forms

# class CustomerProfileForm(forms.ModelForm):   
    # class Meta:
        # model = Customer
        # fields = ['name','locality','city','state','zipcode']

from django import forms
from .models import ItemModel

class PaymentForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = ['name','amount']
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))   
    amount=forms.CharField(label='Amount',widget=forms.TextInput(attrs={'class':'form-control'}))   

     
