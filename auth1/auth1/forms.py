from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class LogInForm(AuthenticationForm):
    # class Meta:
    #     model = User
    #     fields = []
    pass
