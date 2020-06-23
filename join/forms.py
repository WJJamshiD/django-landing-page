from .models import Join,Subcriber,Address
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class JoinForm(forms.ModelForm):
    class Meta:
        model=Join
        fields=['email','first_name','last_name','zip_code']


class SubscriberForm(forms.Form):
    email=forms.EmailField(required=True)



class AddressForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address= forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}),
        required=False,
    )
    address2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    remember = forms.BooleanField(required=False)

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method='POST'
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address',
            'address2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'remember',
            Submit('submit', 'Submit')
        )

    class Meta:
        model=Address
        fields=['username','password','address','address2','city','state','zip_code','remember']