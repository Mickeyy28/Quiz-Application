from django.shortcuts import render, redirect
from .forms import TeacherUserForm, TeacherForm
from django.http import HttpResponseRedirect
from quiz_app.models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from quiz_app.forms import CourseForm, QuestionForm


def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('teacherlogin')
    return render(request, 'teacher/teacherclick.html')


def teacher_signup(request):
    user_form = TeacherUserForm()
    teach_form = TeacherForm()
    if request.method == 'POST':
        user_form = TeacherUserForm(request.POST)
        teach_form = TeacherForm(request.POST, request.FILES)
        if user_form.is_valid() and teach_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            teacher = teach_form.save(commit=False)
            teacher.user = user
            teacher.save()
        return HttpResponseRedirect('teacherlogin')

    return render(request, 'teacher/teachersignup.html', {'user_form': user_form, 'teach_form': teach_form})


def logout_view(request):
    logout(request)
    return redirect('/teacher/teacherclick')


@login_required(login_url='teacherlogin')
def teacher_exam_view(request):
    return render(request, 'teacher/teacher_exam.html')


@login_required(login_url='teacherlogin')
def teacher_add_exam_view(request):
    courseform = CourseForm()
    if request.method == 'POST':
        courseform = CourseForm(request.POST)
        if courseform.is_valid():
            courseform.save()
        else:
            print('invalid course form')
        return HttpResponseRedirect('/teacher/teacher-view-exam')
    return render(request, 'teacher/teacher_add_exam.html', {'courseform': courseform})


@login_required(login_url='teacherlogin')
def teacher_view_exam_view(request):
    courses = Course.objects.all()
    return render(request, 'teacher/teacher_view_exam.html', {'courses': courses})


@login_required(login_url='teacherlogin')
def delete_exam_view(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/teacher/teacher-view-exam')


@login_required(login_url='admin')
def teacher_question_view(request):
    return render(request, 'teacher/teacher_question.html')


@login_required(login_url='teacherlogin')
def teacher_add_question(request):
    questionform = QuestionForm()
    if request.method == 'POST':
        questionform = QuestionForm(request.POST)
        if questionform.is_valid():
            question = questionform.save(commit=False)
            course = Course.objects.get(id=request.POST.get('courseID'))
            question.course = course
            question.save()
        else:
            print("invalid question form")
        return HttpResponseRedirect('/teacher/teacher-view-question')
    return render(request, 'teacher/teacher_add_ques.html', {'questionform': questionform})


@login_required(login_url='teacherlogin')
def teacher_view_question_view(request):
    courses = Course.objects.all()
    return render(request, 'teacher/teacher_view_question.html', {'courses': courses})


@login_required(login_url='teacherlogin')
def see_question_view(request, pk):
    questions = Question.objects.all().filter(course_id=pk)
    return render(request, 'teacher/see_question.html', {'questions': questions})


@login_required(login_url='teacherlogin')
def remove_question_view(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/teacher/teacher-view-question')
