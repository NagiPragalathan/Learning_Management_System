import random, time, json

from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from ..models import Faculty_details, Users, Room, Message, RoomMember, Gallery
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .Tool.blogTool import get_images


# def login_page(request):
#     return render(request,"login/login.html")

# def login_into_home(request):
#     user_name = request.POST.get('usr_name')
#     password = request.POST.get('password')
#     print(user_name,password)
#     user = authenticate(username=user_name, password=password)
#     print(user)
#     for i  in Users.objects.all():
#         print(i.user_name,i.mail_id)
#     if user is not None:
#         # login(request, user)
#         user_detials = Users.objects.get(user_name = user_name)
#         role = user_detials.role
#         if role == 3 :
#             return redirect('/home')
#         elif role == 2:
#             return redirect('/home')
#         elif role == 1:
#             return redirect('/home')
#         if role == 4 :
#             return redirect('/home')
#     else:
#         return render(request,"login/login.html")


def student_home(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    name = Users.objects.get(user_name=usr_obj.username)
    # faculty_details = Faculty_details.objects.get(user_name=name.user_name)
    faculty_details=""
    return render(request,"home/index.html",{'user_name':usr_obj.username,'detials':faculty_details})

@login_required()
def staff_home(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    name = Users.objects.get(user_name=usr_obj.username)
    faculty_details = Faculty_details.objects.get(user_name=name.user_name)
    faculty_details=""
    return render(request,"home/index.html",{'user_name':usr_obj.username,'detials':faculty_details})


# Video Chat.....
def lobby(request):
    return render(request, 'base/lobby.html')

def video_chat_room(request):
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


# ....... room chating


def chat_home(request):
    return render(request, 'chat_room/home.html')

def chat_room(request, room):
    username = request.GET.get('username') # henry
    room_details = Room.objects.get(name=room)
    return render(request, 'chat_room/room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/chat'+'/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat'+'/'+room+'/?username='+username)

def Ncheckview(request):
    room = request.GET['room_name']
    username = request.GET['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/chat'+'/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat'+'/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    print(message,username,room_id)
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()



def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})

def chatgetMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})


#...............gallery.......................................
def gallery(request):
    item = get_images()
    return render(request,"Gallery/gallery.html",{"categories":item[0],"images":item[1]})
#............................................................
# upload image...............................................
def upload_image(request):
    categories = request.POST.get("Category")
    image = request.FILES["image_file"]
    update = Gallery(image=image,categories=categories)
    update.save()
    return render(request,"about_us/team.html")

def delete_image(request):
    id = request.POST.get("id")
    image = Gallery.objects.get(G_id=id)
    image.delete()
    return render(request,"about_us/team.html")
#..............................................................
def image_upload_page_gallery(request):
    item = get_images()
    return render(request,"Gallery/empty.html",{"categories":item[0],"images":item[1]})
