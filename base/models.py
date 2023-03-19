from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=200)
    mail_id = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.IntegerField()   # roles {1,2,3} 1(Admin), 2(HOD), 3(Staff)


class Faculty_details(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=200, unique=True)
    role = models.ForeignKey(Users, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='photo/%Y/%m/%d', default='images/Screenshot_3.png')
    id_number = models.IntegerField()
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200, unique=True)
    designation = models.CharField(max_length=200, default='designation')
    date_of_join = models.DateField(default=timezone.now)
    department = models.CharField(max_length=200, default='department')
    qualififcation = models.CharField(max_length=200, default='qualififcation')
    assessment_period = models.IntegerField(default=0)  # auto update....
    experience = models.IntegerField(default=0)
    bio = models.CharField(max_length=200, default='No Bio yet.')

    # Internal test evaluation


class Subjects(models.Model):
    subject_image = models.CharField(max_length=200)
    subject_name = models.CharField(max_length=200, unique=True)
    subject_code = models.CharField(max_length=200, unique=True)
    semester = models.IntegerField()
    department = models.CharField(max_length=200)
    discription = models.CharField(
        max_length=200, default='No Discription yet.')


class Subject_handled(models.Model):
    faculty_id = models.IntegerField()
    subject_staff = models.ForeignKey(
        Faculty_details, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=200)
    target_pass = models.CharField(max_length=200, default='10')
    actual_pass = models.CharField(max_length=200, default='10')


class Test_evaluation(models.Model):
    # it's can be access to subject.name, subject.code
    subject_detials = models.ForeignKey(
        Subject_handled, on_delete=models.CASCADE)
    test = models.CharField(max_length=200)
    target_pass = models.CharField(max_length=200)
    actual_pass = models.CharField(max_length=200)


class Details(models.Model):
    faculty_id = models.IntegerField()
    image = models.ImageField(
        upload_to='photo/%Y/%m/%d', default='images/user_image.png')
    name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    designation = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    coming_from = models.CharField(max_length=200)
    mail_id = models.CharField(max_length=200)


# chat_room
class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    room = models.CharField(max_length=1000000)
    user = models.CharField(max_length=1000000)


class class_enrolled(models.Model):
    user_id = models.IntegerField()
    mail_id = models.CharField(max_length=200)
    class_id = models.IntegerField(primary_key=True)
    subject_code = models.CharField(max_length=200)


class ClassRooms(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    owner = models.ForeignKey(Faculty_details, on_delete=models.CASCADE)
    class_image = models.CharField(max_length=200)
    class_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=200, unique=True)
    semester = models.IntegerField()
    department = models.CharField(max_length=200)
    discription = models.CharField(
        max_length=200, default='No Discription yet.')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/Student/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    joinned_year = models.DateField(default=timezone.now)
    role_no = models.IntegerField()
    department = models.CharField(max_length=40)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/Teacher/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    role = models.CharField(max_length=20, null=False)
    status = models.BooleanField(default=False)
    department = models.CharField(max_length=40)
    salary = models.PositiveIntegerField(null=True)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    cat = (('Option1', 'Option1'), ('Option2', 'Option2'),
           ('Option3', 'Option3'), ('Option4', 'Option4'))
    answer = models.CharField(max_length=200, choices=cat)


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

# Blog..................................


class blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, default='UnTitled')
    description = models.CharField(
        max_length=200, default="Author not provied any description")
    content = models.CharField(
        max_length=2000, default="Author not provied any description")
    blog_profile_img = models.CharField(
        max_length=2000, default="https://www.equalityhumanrights.com/sites/default/files/styles/listing_image/public/default_images/blog-teaser-default-full_5.jpg?itok=YOsTg-7X")
    categories = models.CharField(max_length=200)
    updated_date = models.DateField(default=timezone.now)


# Gallery.............................

class Gallery(models.Model):
    G_id = models.IntegerField(primary_key=True)
    image = models.ImageField(
        upload_to='Gallery/%Y/%m/%d', default='images/user_image.png')
    categories = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)

# Notes..............................


class NoteCourse(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    course_id = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ebook(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    course = models.ForeignKey(NoteCourse, on_delete=models.CASCADE)
    file = models.FileField(upload_to='ebooks')

    def __str__(self):
        return self.title


class EbookForClass(models.Model):
    id = models.IntegerField(primary_key=True)
    cover_image = models.CharField(max_length=100)
    Class_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    course = models.ForeignKey(NoteCourse, on_delete=models.CASCADE)
    file = models.FileField(upload_to='ebooks')

    def __str__(self):
        return self.title


class Attendees(models.Model):
    id = models.IntegerField(primary_key=True)
    class_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    subject_states = models.CharField(max_length=50)
    Date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

# classRoom ........................

# class ClassRommNotification(models.Model):
#     id = models.IntegerField(primary_key=True)
#     from_ = course=models.ForeignKey(User,on_delete=models.CASCADE)
#     subject = models.CharField(max_length=50)
#     date = models.DateField(default=timezone.now)
#     file = models.FileField(upload_to='ebooks')

#     def __str__(self):
#         return self.from_

# class ClassRoomWorks(models.Model):
#     id = models.IntegerField(primary_key=True)
#     from_ = course=models.ForeignKey(User,on_delete=models.CASCADE)
#     work = models.CharField(max_length=50)
#     date = models.DateField(default=timezone.now)
#     file = models.FileField(upload_to='ebooks')

#     def __str__(self):
#         return self.from_

# class Notes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=100)
#     subject = models.CharField(max_length=50)
#     course = models.ForeignKey(NoteCourse, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='Notes')

#     def __str__(self):
#         return self.title
