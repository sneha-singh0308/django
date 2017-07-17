from django import forms
from models import user
class SignUpForm(forms.ModelForm):
  class Meta:
    model = user
    fields=['phone','name','age']