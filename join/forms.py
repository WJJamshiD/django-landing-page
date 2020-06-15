from .models import Join
from django import forms


class JoinForm(forms.ModelForm):
    class Meta:
        model=Join
        fields=['email','first_name','last_name','zip_code']