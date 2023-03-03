from django import forms
from ...models import Ebook,NoteCourse

class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ['title', 'subject', 'course', 'file']

class CourseForm(forms.ModelForm):
    class Meta:
        model = NoteCourse
        fields = ('name', 'description', 'semester', 'course_id')
        labels = {
            'name': 'Course Name',
            'description': 'Course Description',
            'semester': 'Semester',
            'course_id': 'course_id',
        }
