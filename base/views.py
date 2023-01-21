from django.shortcuts import render, redirect
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Faculty_details, Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime


# Create your views here.
def login_page(request):
    return render(request,"login/login.html")

def login_into_home(request):
    user_name = request.POST.get('usr_name')
    password = request.POST.get('password')
    print(user_name,password)
    user = authenticate(username=user_name, password=password)
    print(user)
    if user is not None:
        login(request, user)
        user_detials = Users.objects.get(mail_id = user_name)
        role = user_detials.role
        usr_name = user_detials.user_name
        if role == 3 :
            return redirect('/home')
        elif role == 2:
            return redirect('/home')
        elif role == 1:
            return redirect('/home')
    else:
        return render(request,"login/login.html")

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


#-------------------------
@login_required()
def home(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    name = Users.objects.get(mail_id=usr_obj.username)
    faculty_details = Faculty_details.objects.get(user_name=name.user_name)
    return render(request,"home/index.html",{'user_name':usr_obj.username,'detials':faculty_details})
    

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


# Video chat ....

def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')


def getToken(request):
    appId = "6c195af2970e48579689b47d0debf9ca"
    appCertificate = "acb5f43b05c74985aec64f691cf4311c"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)