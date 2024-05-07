from django.forms import ModelForm
from .models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['projectName','projectImage','projectURL']
        def __init__(self,*args,**kwargs):
            super(ProjectForm,self).__init__(*args,**kwargs)