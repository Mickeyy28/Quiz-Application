
from django.contrib import admin
from django.urls import path, include
from quiz_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authenticate.urls', namespace='authenticate')),
    path('teacher/', include('teacher.urls', namespace='teacher')),
    path('', views.home_page, name='home-page'),
    path('view-course', views.student_exam_view, name='view-course'),
    path('take-exam/<int:pk>', views.take_exam_view, name='take-exam'),
    path('start-exam/<int:pk>', views.start_exam_view, name='start-exam'),
    path('calculate-marks', views.calculate_marks_view, name='calculate-marks'),
    path('save_ans', views.save_ans, name="save_ans"),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
