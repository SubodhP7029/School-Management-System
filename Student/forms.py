from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        birthdate = forms.DateField(
            widget=forms.DateInput(format='%d-%m-%Y'),
            input_formats=('%d-%m-%Y', )
        )
        admission_date = forms.DateField(
            widget=forms.DateInput(format='%d-%m-%Y'),
            input_formats=('%d-%m-%Y', )
        )
        labels = {
            "general_register_number": "General Register Number",
            "student_name": "Student Name",
            "birthdate": "Birth Date",
            "father_name": "Father's Name",
            "mother_name": "Mother's Name",
            "caste": "Caste",
            "birth_place":"Place of birth",
            "admission_date":"Date of Admission",
            "standard":"Standard",
            "division":"Division"
        }
        fields = "__all__"


