from django.db import models

# Create your models here.

class Projects(models.Model):
    
    projectName = models.CharField(max_length=100,verbose_name="Project Name")
    projectImage = models.FileField(upload_to="Project Cover", blank=True,null=True,verbose_name="Project Cover")
    projectURL = models.TextField(max_length=1000,verbose_name="Project Link")
    
    def __str__(self):
        return self.projectName