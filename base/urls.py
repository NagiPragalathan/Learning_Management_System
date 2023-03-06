from django.urls import path
from LMS import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView,LoginView

from .Routes.common import *
from .Routes.tool import *
from .Routes.staff import *
from .Routes.students import *
from .Routes.study import *
from .Routes.notes import *
from .Routes.exam import *
from .Routes.blog import *
from .Routes.admin_page import *


#Initilizes........................

urlpatterns = []
def Make_Join(Componets):
    OutComponets = []
    for i in Componets:
        for j in i:
            OutComponets.append(j)
    return OutComponets

# Urls............................

tools = [
     path('trans',translate_),
     path('convert_text',convert_text),
     path('wikipedia_summary',wikipedia_summary),
     path('convert_docx_to_pdf',convert_docx_to_pdf),
     path('convert_pdf_to_docx',convert_pdf_to_docx),
     path('convert_pdf_to_excel',convert_pdf_to_excel),
     path('convert_excel_to_pdf',convert_excel_to_pdf),
     path('convert_jpg_to_pdf',convert_jpg_to_pdf),
     path('convert_jpg_to_word',convert_jpg_to_word),
     path('calculator',calculator),
     path('cgpa_calculator',cgpa_calculator),
     path('handwriting_converter',handwriting_converter),
     path('keyword_to_image',keyword_to_image),
     path('video_meeting',video_meeting),

     path('gpa_calculator',gpa_calculator),
     path('get_subject',get_subject),
]

common = [
    path('home', home),
    path('login_',login_page),
    path('login_to_home',login_into_home),
    path('personal_detials',Personal_detials),

]

admin = [
    path('add_Faculty',add_faculty),
    path('add_usr',add_usr),
]


videochat = [
    path('chat_lobby', lobby),
    path('room/', video_chat_room),
    path('get_token/', getToken),

    path('create_member/', createMember),
    path('get_member/', getMember),
    path('delete_member/', deleteMember),
]


chatroom = [
    path('chat_home/', chat_home),
    path('chat/<str:room>/', chat_room, name="chat_room"), # problem...................
    path('chat_home/checkview', checkview, name="checkview"),
    path('send', send, name="send"),
    path('getMessages/<str:room>/', getMessages, name="getMessages"),
]


classroom = [
    path('class_room',home_classroom),
    path('message/<str:room>/',chatgetMessages, name="message"),
    path('<str:pk>/<str:class_id>',nave_home_classroom),
    path('add_class',add_class),
    path("save_added_class",save_add_class),
]

studet = [
    path('student/studentclick', studentclick_view),
    path('student/studentlogin', LoginView.as_view(template_name='student/studentlogin.html'),name='studentlogin'),
    path('student/studentsignup', student_signup_view,name='studentsignup'),
    path('student/student-dashboard', student_dashboard_view,name='student-dashboard'),
    path('student/student-exam', student_exam_view,name='student-exam'),
    path('student/take-exam/<int:pk>', take_exam_view,name='take-exam'),
    path('student/start-exam/<int:pk>', start_exam_view,name='start-exam'),
    path('student/calculate-marks', calculate_marks_view,name='calculate-marks'),
    path('student/view-result', view_result_view,name='view-result'),
    path('student/check-marks/<int:pk>', check_marks_view,name='check-marks'),
    path('student/student-marks', student_marks_view,name='student-marks'),
]

teacher = [
    path('teacher/teacherclick', teacherclick_view),
    path('teacher/teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
    path('teacher/teachersignup', teacher_signup_view,name='teachersignup'),
    path('teacher/teacher-dashboard', teacher_dashboard_view,name='teacher-dashboard'),
    path('teacher/teacher-exam', teacher_exam_view,name='teacher-exam'),
    path('teacher/teacher-add-exam', teacher_add_exam_view,name='teacher-add-exam'),
    path('teacher/teacher-view-exam', teacher_view_exam_view,name='teacher-view-exam'),
    path('teacher/delete-exam/<int:pk>', delete_exam_view,name='delete-exam'),
    path('teacher/teacher-question', teacher_question_view,name='teacher-question'),
    path('teacher/teacher-add-question', teacher_add_question_view,name='teacher-add-question'),
    path('teacher/teacher-view-question', teacher_view_question_view,name='teacher-view-question'),
    path('teacher/see-question/<int:pk>', see_question_view,name='see-question'),
    path('teacher/remove-question/<int:pk>', remove_question_view,name='remove-question'),
]

exam = [

    path('', home_view,name=''),
    path('logout', LogoutView.as_view(template_name='exam/logout.html'),name='logout'),
    path('contactus',  contactus_view),
    path('afterlogin',  afterlogin_view,name='afterlogin'),
    path('adminclick',  adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='exam/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard',  admin_dashboard_view,name='admin-dashboard'),
    path('admin-teacher',  admin_teacher_view,name='admin-teacher'),
    path('admin-view-teacher',  admin_view_teacher_view,name='admin-view-teacher'),
    path('update-teacher/<int:pk>',  update_teacher_view,name='update-teacher'),
    path('delete-teacher/<int:pk>',  delete_teacher_view,name='delete-teacher'),
    path('admin-view-pending-teacher',  admin_view_pending_teacher_view,name='admin-view-pending-teacher'),
    path('admin-view-teacher-salary',  admin_view_teacher_salary_view,name='admin-view-teacher-salary'),
    path('approve-teacher/<int:pk>',  approve_teacher_view,name='approve-teacher'),
    path('reject-teacher/<int:pk>',  reject_teacher_view,name='reject-teacher'),

    path('admin-student',  admin_student_view,name='admin-student'),
    path('admin-view-student',  admin_view_student_view,name='admin-view-student'),
    path('admin-view-student-marks',  admin_view_student_marks_view,name='admin-view-student-marks'),
    path('admin-view-marks/<int:pk>',  admin_view_marks_view,name='admin-view-marks'),
    path('admin-check-marks/<int:pk>',  admin_check_marks_view,name='admin-check-marks'),
    path('update-student/<int:pk>',  update_student_view,name='update-student'),
    path('delete-student/<int:pk>',  delete_student_view,name='delete-student'),

    path('admin-course',  admin_course_view,name='admin-course'),
    path('admin-add-course',  admin_add_course_view,name='admin-add-course'),
    path('admin-view-course',  admin_view_course_view,name='admin-view-course'),
    path('delete-course/<int:pk>',  delete_course_view,name='delete-course'),

    path('admin-question',  admin_question_view,name='admin-question'),
    path('admin-add-question',  admin_add_question_view,name='admin-add-question'),
    path('admin-view-question',  admin_view_question_view,name='admin-view-question'),
    path('view-question/<int:pk>',  view_question_view,name='view-question'),
    path('delete-question/<int:pk>',  delete_question_view,name='delete-question'),


]


blog_url = [
    path('list_blog',list_blog),
    path('list_edit_blog',list_edit_blog),
    path('view_blog/<str:pk>',view_blog),
    path('edit_blog/<str:pk>',edit_blog),
    path('create_blog',blog_edit),
    path('save_blog',save_blog),
    path('delete_blog',delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>',save_edit_blog),

]

gallery_ = [

    path("gallery",gallery),
    path('image_upload_page_gallery',image_upload_page_gallery),
    path('upload_image',upload_image),
    path('delete_image',delete_image),
    
]


note = [
    path('', course_list, name='course_list'),
    path('course/course_edit/<int:pk>', course_detail, name='course_detail'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course/add/', course_add, name='course_add'),

    path('ebook/book_list/', book_list, name='book_list'),
    path('ebook/add/', ebook_add, name='ebook_add'),
    path('ebook/<int:pk>/edit/', ebook_edit, name='ebook_edit'),
    path('ebook/<int:pk>/delete/', ebook_delete, name='ebook_delete'),
]


urlpatterns.extend(Make_Join([tools,note,gallery_,blog_url,common,admin,chatroom,classroom,videochat,studet,teacher,exam]))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)