from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Tell me your name', max_length=100)
    email = forms.EmailField(label='Enter your email')
    message = forms.CharField(label='Message', max_length=300)