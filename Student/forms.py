from django import forms 


# create student forms 
class Student_form(forms.Form):
    s_name=forms.CharField(max_length=50,label="Student Name",label_suffix=' ',widget=forms.TextInput)
    s_class=forms.CharField(max_length=50,label="Student Class",label_suffix=' ')
    s_address=forms.CharField(max_length=50,label="Student Address",label_suffix=' ',widget=forms.TextInput)
    s_school=forms.CharField(max_length=50,label="Student School",label_suffix=' ',widget=forms.TextInput)
    s_email=forms.EmailField(max_length=50,label="Student email",label_suffix=' ',widget=forms.EmailInput)
    
class Searchform(forms.Form):
    s_name=forms.CharField(max_length=30,label="Student name",label_suffix=' ')
    