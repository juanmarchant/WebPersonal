from django import forms
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.core.mail import message, send_mail

class ContactPageView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/contact/' + '?ok'


    def get_form(self, form_class=None):
        form = super(ContactPageView, self).get_form()
        # Inputs
        form.fields['name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-3 mt-2', 'placeholder': 'Enter your name'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-3 mt-2', 'placeholder':'Enter your email'})
        form.fields['message'].widget = forms.Textarea(
            attrs={'class': 'form-control mb-3 mt-2', 'cols':'30', 'rows':'5', 'placeholder':'Your message here...'})
        return form


    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        send_mail(name,message,email,['juanmarchantdev@gmail.com'],fail_silently=False)
        return super().form_valid(form)

