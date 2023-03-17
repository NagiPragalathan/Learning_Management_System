import os

from django.shortcuts import render
from ..models import Faculty_details, Users, Room,ClassRooms, class_enrolled
from django.shortcuts import render
from bing_image_downloader import downloader
from LMS.settings import BASE_DIR
from .Tool.Tools import get_user_mail,get_user_name,get_user_role,get_user_obj

def nave_home_classroom(request,pk,class_id):
    if pk == "join":
            
            # print(get_user_mail(request))
            try:
                if class_enrolled.objects.filter(mail_id=get_user_mail(request),subject_code = class_id).exists():
                    print("connection passed...")
                else:
                    class_en = class_enrolled(mail_id = get_user_mail(request),subject_code = class_id )
                    class_en.save()
            except:
                if class_enrolled.objects.filter(mail_id=request.user.email,subject_code = class_id).exists():
                    print("connection passed...")
                else:
                    class_en = class_enrolled(mail_id = request.user.email,subject_code = class_id )
                    class_en.save()
            peoples=[]
            people = class_enrolled.objects.filter(subject_code = class_id)
            for i in people:
                print(i.class_id,i.mail_id)
                person_obj = Users.objects.get(mail_id=i.mail_id)
                peoples.append(person_obj)
            detials = ClassRooms.objects.get(subject_code = class_id)

            # create new chat room..........

            if Room.objects.filter(name=class_id).exists():
                return render(request, 'class_room/classroom.html',{'people':peoples,"detail":detials})
            else:
                new_room = Room.objects.create(name=class_id)
                new_room.save()
                return render(request, 'class_room/classroom.html',{'people':peoples,"detail":detials})
    elif pk == "attendes":
            peoples=[]
            people = class_enrolled.objects.filter(subject_code = class_id)
            for i in people:
                print(i.class_id,i.mail_id)
                person_obj = Users.objects.get(mail_id=i.mail_id)
                peoples.append(person_obj)
            detials = ClassRooms.objects.get(subject_code = class_id)
            return render(request, 'class_room/attendes.html',{'people':peoples,"detail":detials})
    else :
        peoples=[]
        people = class_enrolled.objects.filter(subject_code = class_id)
        test = class_enrolled.objects.all()
        detials = ClassRooms.objects.get(subject_code = class_id)

        for i in test:
            print(i.class_id,i.mail_id,i.subject_code)
        for i in people:
            print(i.class_id,i.mail_id,i.subject_code)
            person_obj = Users.objects.get(mail_id=i.mail_id)
            peoples.append(person_obj)
        if Room.objects.filter(name=class_id).exists():
            return render(request, 'class_room/classroom.html',{'people':peoples,"detail":detials})
        else:
            new_room = Room.objects.create(name=class_id)
            new_room.save()
            return render(request, 'class_room/classroom.html',{'people':peoples,"detail":detials})


def home_classroom(request):
    classes = []
    img = {}
    dep = []
    sem = [1,2,3,4,5,6,7,8]
    try:
        enroll_classes = class_enrolled.objects.filter(mail_id=get_user_mail(request))
    except:
        enroll_classes = class_enrolled.objects.filter(mail_id=request.user.email)

    for i in enroll_classes:
        classrooms = ClassRooms.objects.filter(subject_code=i.subject_code)
        print(i.class_id)
        print(classrooms)
        for i in classrooms:
            print(i.id,i.class_name)
            classes.append(i)
            if i.department not in dep:
                dep.append(i.department)
            try:
                item = os.listdir(i.class_image)
            except:
                item=['nofiles.jpg','']
            if len(item)!=0:
                path = "..\\static\\" + i.class_image.split('static\\')[1] + "\\" + item[0]
                print(path,item)
                img[i.subject_code] = path
    try:
        return render(request, 'class_room/class_room_home.html',{'classes':classes,'img':img,'sem_':sem,'dep':dep,"user_name":get_user_name(request),"User_role":get_user_role(request),"usr_img":get_user_obj(request)})
    except:
        return render(request, 'class_room/class_room_home.html',{'classes':classes,'img':img,'sem_':sem,'dep':dep,"user_name":request.user.username})

def add_class(request):
    return render(request, 'class_room/new_add.html')

def save_add_class(request):
    class_name = request.POST.get('class_name')
    subject_code = request.POST.get('subject_code')
    department = request.POST.get('department')
    semester = request.POST.get('semester')
    discription = request.POST.get('discription')
    
    out=os.path.join(os.path.join(BASE_DIR, 'static'),'classroom_pics')
    class_room = ClassRooms(class_image=os.path.join(os.path.join(os.path.join(BASE_DIR, 'static'),'classroom_pics'),"_".join(class_name.split(' '))+"_logos"),class_name=class_name,subject_code=subject_code,department=department,semester=semester,discription=discription,owner=Faculty_details.objects.get(mail=get_user_mail(request)))
    class_room.save()
    class_id = ClassRooms.objects.get(subject_code=subject_code)
    enroll_class = class_enrolled(mail_id=get_user_mail(request),subject_code = subject_code,class_id=class_id.id)
    enroll_class.save()
    downloader.download(str("_".join(class_name.split(' ')))+"_logos", limit=2, output_dir=out, adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

    return render(request, 'class_room/new_add.html')

def attendes(request):
    return render(request,'class_room/attendes.html')