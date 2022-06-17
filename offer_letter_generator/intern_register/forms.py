from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Intern

class InternForm(ModelForm):
    class Meta:
        model = Intern
        fields = ('i_name','i_email_address','i_mob_num','i_address','i_job_position','i_stipend','i_join_date','i_description','hr_name','hr_email')

        labels = {
            'i_name': '',
            'i_email_address': '',
            'i_mob_num': '',
            'i_address': '',
            'i_job_position': '',
            'i_stipend': '',
            'i_join_date': 'Join Date of Intern',
            'i_description': '',
            'hr_name': 'HR Name',
            'hr_email': ''

        }

        widgets = {
            'i_name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Intern Name'}),
            'i_email_address': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Intern Email Address'}),
            'i_mob_num': forms.TextInput(attrs={'class':'form-control','placeholder': 'Intern Mobile Number'}),
            'i_address': forms.TextInput(attrs={'class':'form-control','placeholder': 'Intern Address'}),
            'i_job_position': forms.TextInput(attrs={'class':'form-control','placeholder': 'Job Position'}),
            'i_stipend': forms.TextInput(attrs={'class':'form-control','placeholder': 'Stipend'}),
            'i_join_date': forms.DateInput(attrs={'type':'date','class':'form-control','placeholder': 'Joining Date'}),
            'i_description': forms.Textarea(attrs={'rows':2,'class':'form-control','placeholder': 'Description'}),
            'hr_name': forms.Select(attrs={'class':'form-control','placeholder': 'HR Name'}),
            'hr_email': forms.EmailInput(attrs={'class':'form-control','placeholder': 'HR Email'})
        }


