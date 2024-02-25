# My Django imports
from django import forms

# My app imports
from ONB_auth.models import Accounts
from ONB_admin.models import (Notification, Comment)

class CreateNotificationForm(forms.ModelForm):

    title = forms.CharField(max_length=1000, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter the Title of the post ',
            'type':'text',
        }
    ))

    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={
            'class':'form-control',
            'type':'file',
            'accept':'image/png, image/jpeg'
        }
    ))


    description = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Enter the description of the post ',
            'type':'text',
        }
    ))


    class Meta:
        model = Notification
        fields = ('image', 'title', 'description')

class AddCommentForm(forms.ModelForm):

    comment = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Enter your comment ',
            'type':'text',
            'cols':'30',
            'rows':'10',
        }
    ))


    class Meta:
        model = Comment
        fields = ('comment',)
