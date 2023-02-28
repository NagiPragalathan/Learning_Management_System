
import datetime
from django.shortcuts import render
from ..models import Faculty_details, Users
from django.contrib.auth.models import User
from django.shortcuts import render




#--------------------------
def Personal_detials(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(mail=usr_obj.username)
    # request and get datas ..............
    role = Users.objects.get(mail_id = usr_obj.username)
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
    edit.role=role
    edit.name=name
    edit.id_number=id_number
    edit.designation=designation
    edit.department=department
    edit.experience=experience
    edit.qualififcation=qualififcation
    edit.assessment_period=assessment_period
    edit.date_of_join=date_formate
    edit.image = my_uploaded_file
    edit.bio=bio
    edit.save()
    return render(request,"home/index.html",{'user_name':usr_obj.username,'detials':faculty_details})
