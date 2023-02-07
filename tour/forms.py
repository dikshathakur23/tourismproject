from django import forms
from .models import Blog,ContactUs


class blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"