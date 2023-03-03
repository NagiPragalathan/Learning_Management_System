from django.shortcuts import render, redirect, get_object_or_404
from ..models import NoteCourse, Ebook
from .Forms.Notes_form import EbookForm, CourseForm

def course_list(request):
    courses = NoteCourse.objects.all()
    for i in courses:
        print(i.name)
    return render(request, 'notes/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(NoteCourse, pk=pk)
    return render(request, 'notes/course_detail.html', {'course': course})

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    context = {'form': form}
    return render(request, 'notes/course_add.html', context)

def course_edit(request, pk):
    course = NoteCourse.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'notes/course_edit.html', {'form': form, 'course': course})

def course_delete(request, pk):
    course = get_object_or_404(NoteCourse, pk=pk)
    course.delete()
    return redirect('course_list')

def ebook_add(request):
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = EbookForm()
    return render(request, 'notes/ebook_add.html', {'form': form})

def ebook_edit(request, pk):
    ebook = get_object_or_404(Ebook, pk=pk)
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES, instance=ebook)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = EbookForm(instance=ebook)
    return render(request, 'notes/ebook_edit.html', {'form': form})

def ebook_delete(request, pk):
    ebook = get_object_or_404(Ebook, pk=pk)
    ebook.delete()
    return redirect('course_list')

def book_list(request):
    books = Ebook.objects.all()
    return render(request, 'notes/ebook_list.html', {'books': books})
