from django import forms
from .models import Profile, Projects, Resume

class ProjectsModelForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields ='__all__'

class ResumeModelForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields ='__all__'