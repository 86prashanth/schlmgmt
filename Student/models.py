from django.db import models

# Create Student models here.
class Student_model(models.Model):
    s_name=models.CharField(max_length=50)
    s_class=models.CharField(max_length=50)
    s_address=models.CharField(max_length=50)
    s_school=models.CharField(max_length=50)
    s_email=models.EmailField(max_length=50)