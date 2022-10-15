from django import forms
from contact.models import contact
from django.contrib.auth import get_user_model#??????????????

"""class ContactForm(forms.Form):
    name = forms.CharField(label = 'Name', widget = forms.TextInput(attrs = {
        'class':'input-text',
        'placeholder':'Your Name'
    }))

    email = forms.CharField(label = 'email_address', widget = forms.TextInput(attrs = {
        'class':'input-text',
        'placeholder':'Email'
    }))

    company = forms.CharField(label = 'Company', widget = forms.TextInput(attrs = {
        'class':'input-text',
        'placeholder':'Company'
    }))

    telephone = forms.CharField(label = 'Telephone', widget = forms.TextInput(attrs = {
        'class':'input-text',
        'placeholder':'Telephone'
    }))

    address = forms.CharField(label = 'Address', widget = forms.TextInput(attrs = {
        'class':'input-text',
        'placeholder':'Address'
    }))

    comment = forms.CharField(label = 'Address', widget = forms.TextInput(attrs = {
        'class':'input-text',
        'placeholder':'Comment'
    }))
"""

class ContactForm(forms.ModelForm):
    # again_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = contact
        fields  = "__all__"

        widgets = {
            'first_name': forms.TextInput(attrs={
                # 'placeholder':'Your Name',
                'class':'input-text'
            }),
            'email_adress':forms.EmailInput(attrs={
                'placeholder':'Your Email',
                'class':'input-text'
            }),
            'company':forms.TextInput(attrs={
                'class':'input-text',
                'placeholder':'Company',
            }),
            'telephone':forms.TextInput(attrs={
                'placeholder':'Telephone',
                'class':'input-text'
            }),

            'address':forms.TextInput(attrs={
                'placeholder':'Address',
                'class':'input-text'
            }),

            'comments':forms.Textarea(attrs={
                'placeholder':'comment',
                'class':'input-text'
            })
        }
