from django import forms
from django.contrib.auth.models import User
from base import models


class TeacherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['address', 'mobile', 'profile_pic', 'role']
    DEPARTMENT_CHOICES = (
        ('none', 'Selected Staff'),
        ('CSE', 'Computer Science and Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('ME', 'Mechanical Engineering'),
        # Add more choices here as needed
    )

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('hod', 'Hod'),
        ('admin', 'Admin'),
    )
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)
