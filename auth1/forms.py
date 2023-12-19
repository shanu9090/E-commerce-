from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm,AuthenticationForm,AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from application.models import Customer
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']
        # user=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
        # email=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))





class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['user','password']
    # user=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    # password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
   

class MyPasswordChange(PasswordChangeForm):
    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']
    old_password=forms.CharField(label='old_password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label='new_password1',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label='new_password2',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):   
    class Meta:
        model = Customer
        fields= ['city','state','zipcode','locality']
    # name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    city=forms.CharField(label='City',widget=forms.TextInput(attrs={'class':'form-control'}))
    # state=forms.ChoiceField(label='State',widget=forms.TextInput(attrs={'class':'form-control'}))
    locality=forms.CharField(label='Locality',widget=forms.TextInput(attrs={'class':'form-control'}))
    zipcode=forms.IntegerField(label='PinCode',widget=forms.NumberInput(attrs={'class':'form-control'}))

# class CustomerProfileForm(forms.ModelForm):   
    # class Meta:
        # model = Customer
        # fields= "__all__"
    # name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    # city=forms.CharField(label='City',widget=forms.TextInput(attrs={'class':'form-control'}))
    # state=forms.ChoiceField(label='State',widget=forms.TextInput(attrs={'class':'form-control'}))
    # locality=forms.CharField(label='Locality',widget=forms.TextInput(attrs={'class':'form-control'}))
    # zipcode=forms.IntegerField(label='PinCode',widget=forms.NumberInput(attrs={'class':'form-control'}))
