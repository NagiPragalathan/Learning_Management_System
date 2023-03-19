
import datetime
from django.shortcuts import render
from ..models import Faculty_details, Users
from django.contrib.auth.models import User
from django.shortcuts import render
from .Forms import teacher_forms
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from base import models as QMODEL
from base import models as SMODEL
from .Forms import exam_forms as QFORM


# for showing signup/login button for teacher
def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'teacher/teacherclick.html')


def teacher_signup_view(request):
    userForm = teacher_forms.TeacherUserForm()
    teacherForm = teacher_forms.TeacherForm()
    mydict = {'userForm': userForm, 'teacherForm': teacherForm}
    if request.method == 'POST':
        userForm = teacher_forms.TeacherUserForm(request.POST)
        teacherForm = teacher_forms.TeacherForm(request.POST, request.FILES)
        if userForm.is_valid() and teacherForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            teacher = teacherForm.save(commit=False)
            teacher.user = user
            teacher.save()
            if teacher.role == 'hod':
                add_user = Users(user_name=user.username,
                                 mail_id=user.username, password=user.password, role='2')
                add_user.save()
                current_user = Users.objects.get(mail_id=user.username)
                Fac_del = Faculty_details(user_name=user.username, mail=user.username,
                                          role=current_user, id_number=0, name=str(user.first_name)+" "+str(user.last_name))
                Fac_del.save()
            elif teacher.role == 'staff':
                add_user = Users(user_name=user.username,
                                 mail_id=user.username, password=user.password, role='3')
                add_user.save()
                current_user = Users.objects.get(mail_id=user.username)
                Fac_del = Faculty_details(user_name=user.username, mail=user.username,
                                          role=current_user, id_number=0, name=str(user.first_name)+" "+str(user.last_name))
                Fac_del.save()

            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect('teacherlogin')
    return render(request, 'teacher/teachersignup.html', context=mydict)


def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_dashboard_view(request):
    dict = {

        'total_course': QMODEL.Course.objects.all().count(),
        'total_question': QMODEL.Question.objects.all().count(),
        'total_student': SMODEL.Student.objects.all().count()
    }
    return render(request, 'teacher/teacher_dashboard.html', context=dict)


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_exam_view(request):
    return render(request, 'teacher/teacher_exam.html')


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_exam_view(request):
    courseForm = QFORM.CourseForm()
    if request.method == 'POST':
        courseForm = QFORM.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-exam')
    return render(request, 'teacher/teacher_add_exam.html', {'courseForm': courseForm})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'teacher/teacher_view_exam.html', {'courses': courses})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def delete_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/teacher/teacher-view-exam')


@login_required(login_url='adminlogin')
def teacher_question_view(request):
    return render(request, 'teacher/teacher_question.html')


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_add_question_view(request):
    questionForm = QFORM.QuestionForm()
    if request.method == 'POST':
        questionForm = QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            course = QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course = course
            question.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher/teacher-view-question')
    return render(request, 'teacher/teacher_add_question.html', {'questionForm': questionForm})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_question_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'teacher/teacher_view_question.html', {'courses': courses})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def see_question_view(request, pk):
    questions = QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request, 'teacher/see_question.html', {'questions': questions})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def remove_question_view(request, pk):
    question = QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/teacher/teacher-view-question')


# --------------------------
def Personal_detials(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(mail=usr_obj.username)
    # request and get datas ..............
    role = Users.objects.get(mail_id=usr_obj.username)
    id_number = request.POST.get('idcard')
    name1 = request.POST.get('F_name')
    name2 = request.POST.get('surname')
    name = name1+' '+name2
    designation = request.POST.get('designation')
    department = request.POST.get('department')
    experience = request.POST.get('experience')
    qualififcation = request.POST.get('qualififcation')
    assessment_period = request.POST.get('AP')
    date_of_join = request.POST.get('date')
    bio = request.POST.get('about')
    d = date_of_join.split("-")
    date_formate = datetime.date(int(d[0]), int(d[1]), int(d[2]))
    my_uploaded_file = request.FILES['file_upload']
    print(date_of_join)
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    edit = Faculty_details.objects.get(mail=usr_obj.username)
    print(edit.mail)
    edit.role = role
    edit.name = name
    edit.id_number = id_number
    edit.designation = designation
    edit.department = department
    edit.experience = experience
    edit.qualififcation = qualififcation
    edit.assessment_period = assessment_period
    edit.date_of_join = date_formate
    edit.image = my_uploaded_file
    edit.bio = bio
    edit.save()
    return render(request, "home/index.html", {'user_name': usr_obj.username, 'detials': faculty_details})
