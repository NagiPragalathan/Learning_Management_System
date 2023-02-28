from django.shortcuts import render
from ..models import Faculty_details, Users
from django.contrib.auth.models import User
from django.shortcuts import render


def add_faculty(request):
    facultys = Faculty_details.objects.all()
    for i in facultys:
        print(i.name)
    return render(request,"admin/Admin_page_to_add_Facuilty.html",{'users':facultys})

def add_usr(request):
    usr_name = request.POST.get('user_name')
    password = request.POST.get('mail')
    role = request.POST.get('roles')
    mail = request.POST.get('password')

    facultys = Faculty_details.objects.all()
    for i in facultys:
        print(i.name)
    try:
        add_user = Users(user_name=usr_name,mail_id=mail,password=password,role=role)
        add_user.save()
        current_user = Users.objects.get(mail_id=mail)
        Fac_del = Faculty_details(user_name=usr_name,mail=mail,role=current_user, id_number=0, name=add_user.user_name)
        Fac_del.save()
        user = User.objects.create_user(mail, usr_name, password)
        user.save()
    except:
        print("unique are missed....")
    return render(request,"admin/Admin_page_to_add_Facuilty.html",{'users':facultys})

def add_facu(request):
    facultys = Faculty_details.objects.all()
    for i in facultys:
        print(i.name)
    return render(request,"dashboard/tables.html",{'users':facultys})
