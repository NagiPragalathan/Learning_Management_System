from django import forms
from django.contrib.auth.models import User
from ... import models


class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class StudentForm(forms.ModelForm):
    DEPARTMENT_CHOICES = (
        ('CSE', 'Computer Science and Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('ME', 'Mechanical Engineering'),
        # Add more choices here as needed
    )

    joinned_year = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    role_no = forms.IntegerField()
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)

    class Meta:
        model = models.Student
        fields = ['address', 'mobile', 'profile_pic',
                  'joinned_year', 'role_no', 'department']
