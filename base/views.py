from django.shortcuts import render, redirect
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Faculty_details, Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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
        user_detials = Users.objects.get(user_name = user_name)
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


#-------------------------

def home(request):
    return render(request,"home/index.html")
    

def add_faculty(request):
    return render(request,"admin/Admin_page_to_add_Facuilty.html")

def add_usr(request):
    usr_name = request.POST.get('user_name')
    password = request.POST.get('mail')
    role = request.POST.get('roles')
    mail = request.POST.get('password')

    facultys = Faculty_details.objects.all()
    for i in facultys:
        print(i.name)
        
    add_user = Users(user_name=usr_name,mail_id=mail,password=password,role=role)
    add_user.save()
    current_user = Users.objects.get(mail_id=mail)
    Fac_del = Faculty_details(user_name=usr_name,role=current_user, id_number=0, name=add_user.user_name)
    Fac_del.save()
    user = User.objects.create_user(usr_name, mail, password)
    user.save()
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