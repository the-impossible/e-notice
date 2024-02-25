# My Django imports
from django import forms

# My app imports
from ONB_auth.models import Accounts

class AccountCreationForm(forms.ModelForm):
    fullname = forms.CharField(required=True, help_text='Please enter your Fullname',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'autofocus':'',
            'placeholder':'Enter your Full name',
        }
    ))

    username = forms.CharField(required=True,help_text='Please enter your username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter your username',
        }
    ))

    password = forms.CharField(required=True, help_text='Password must contain at least 6 characters',
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password ',
            'type':'Password',
        }
    ))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError('Password too short, should be at least 6 characters!')

        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        num = len(username)

        if Accounts.objects.filter(username=username).exists():
            raise forms.ValidationError('Username Already exist!')

        return username

    class Meta:
        model = Accounts
        fields = ('fullname', 'username', 'password')

class AccountEditForm(forms.ModelForm):
    fullname = forms.CharField(required=True, help_text='Please enter your Fullname',widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'autofocus':'',
            'placeholder':'Enter your Full name',
        }
    ))

    username = forms.CharField(required=True,help_text='Please enter your username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter your username',
        }
    ))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        check = Accounts.objects.filter(username=username)
        if self.instance:
            check = check.exclude(pk=self.instance.pk)
        if check.exists():
            raise forms.ValidationError('Username Already taken!')

        return username

    class Meta:
        model = Accounts
        fields = ('fullname', 'username',)