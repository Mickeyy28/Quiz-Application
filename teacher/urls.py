from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'teacher'

urlpatterns = [
    path('teacherclick', views.teacherclick_view, name="teacherclick"),
    path('teacherlogin', LoginView.as_view(
        template_name='teacher/teacherlogin.html'), name='teacherlogin'),
    path('teachersignup', views.teacher_signup, name='teachersignup'),
    path('logout', views.logout_view, name='logout'),
    path('teacher-exam', views.teacher_exam_view, name='teacher-exam'),
    path('teacher-add-exam', views.teacher_add_exam_view, name='teacher-add-exam'),
    path('teacher-view-exam', views.teacher_view_exam_view,
         name='teacher-view-exam'),
    path('delete_exam/<int:pk>', views.delete_exam_view, name='delete_exam'),
    path('teacher-question', views.teacher_question_view, name='teacher-question'),
    path('teacher-add-question', views.teacher_add_question,
         name='teacher-add-question'),
    path('teacher-view-question', views.teacher_view_question_view,
         name='teacher-view-question'),
    path('see-question/<int:pk>', views.see_question_view, name='see-question'),
    path('remove-question/<int:pk>',
         views.remove_question_view, name='remove-question'),

]
