from django.contrib import admin
from Student.models import Student_model
# Register your models here.
@admin.register(Student_model)
class Student_modelAdmin(admin.ModelAdmin):
    list_display=['s_name','s_class','s_address','s_school','s_email']