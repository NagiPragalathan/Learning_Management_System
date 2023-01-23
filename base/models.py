from django.db import models
from django.utils import timezone
# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name

                            # Faculty_details

class Users(models.Model):
    id          = models.IntegerField(primary_key=True)
    user_name   = models.CharField(max_length = 200)
    mail_id     = models.CharField(max_length=200,unique=True) 
    password    = models.CharField(max_length = 200,unique=True)
    role        = models.IntegerField()   # roles {1,2,3} 1(Admin), 2(HOD), 3(Staff)

class Faculty_details(models.Model):
    id              = models.IntegerField(primary_key=True)
    user_name   = models.CharField(max_length = 200,unique=True)
    role            = models.ForeignKey(Users, on_delete=models.CASCADE)
    image           = models.ImageField(upload_to='photo/%Y/%m/%d',default='images/Screenshot_3.png')
    id_number       = models.IntegerField()
    name            = models.CharField(max_length = 200)
    mail            = models.CharField(max_length = 200,unique=True)
    designation     = models.CharField(max_length = 200,default='designation')
    date_of_join    = models.DateField(default=timezone.now())
    department      = models.CharField(max_length = 200,default='department')
    qualififcation  = models.CharField(max_length = 200,default='qualififcation')
    assessment_period = models.IntegerField(default=0) # auto update....
    experience      = models.IntegerField(default=0)
    bio             = models.CharField(max_length = 200,default='No Bio yet.')


                            # Internal test evaluation 

class Subjects(models.Model):
    subject_image = models.CharField(max_length = 200)
    subject_name  = models.CharField(max_length = 200,unique=True)
    subject_code  = models.CharField(max_length = 200,unique=True)
    semester = models.IntegerField()
    department = models.CharField(max_length = 200)
    discription = models.CharField(max_length = 200,default='No Discription yet.')

class Subject_handled(models.Model):
    faculty_id    = models.IntegerField()
    subject_staff = models.ForeignKey(Faculty_details, on_delete=models.CASCADE)
    subject_name  = models.CharField(max_length = 200)
    subject_code  = models.CharField(max_length = 200)
    target_pass   = models.CharField(max_length = 200,default='10')
    actual_pass   = models.CharField(max_length = 200,default='10')

class Test_evaluation(models.Model):
    subject_detials = models.ForeignKey(Subject_handled, on_delete=models.CASCADE) # it's can be access to subject.name, subject.code
    test            = models.CharField(max_length = 200)
    target_pass     = models.CharField(max_length = 200)
    actual_pass     = models.CharField(max_length = 200)

class Details(models.Model):
    faculty_id = models.IntegerField()
    image = models.ImageField(upload_to='photo/%Y/%m/%d',default='images/user_image.png')
    name = models.CharField(max_length = 200)
    date = models.DateField(default=timezone.now())
    designation = models.CharField(max_length = 200)
    topic = models.CharField(max_length = 200)
    coming_from = models.CharField(max_length = 200)
    mail_id = models.CharField(max_length = 200)




# chat_room
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=timezone.now(), blank=True)
    room = models.CharField(max_length=1000000)
    user = models.CharField(max_length=1000000)

class class_enrolled(models.Model):
    mail_id = models.CharField(max_length = 200)
    class_id = models.IntegerField()
    subject_code  = models.CharField(max_length = 200)


class ClassRooms(models.Model):
    id          = models.IntegerField(primary_key=True)
    class_image = models.CharField(max_length = 200)
    class_name  = models.CharField(max_length = 200)
    subject_code  = models.CharField(max_length = 200,unique=True)
    semester = models.IntegerField()
    department = models.CharField(max_length = 200)
    discription = models.CharField(max_length = 200,default='No Discription yet.')

