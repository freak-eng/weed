from django import forms
from crudproject1.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'emailIBO']