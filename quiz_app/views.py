
from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Question, Result
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, InvalidPage


@login_required(login_url='/user_login')
def student_exam_view(request):
    courses = Course.objects.all()
    return render(request, 'quiz_app/student_exam.html', {'courses': courses})


@login_required(login_url='/user_login')
def take_exam_view(request, pk):
    course = Course.objects.get(id=pk)
    total_questions = Question.objects.all().filter(course=course).count()
    questions = Question.objects.all().filter(course=course)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks
    return render(request, 'quiz_app/take_exam.html', {'course': course, 'total_marks': total_marks, 'total_questions': total_questions})


@login_required(login_url='/user_login')
def start_exam_view(request, pk):
    course = Course.objects.get(id=pk)
    obj = Question.objects.all().filter(course=course).order_by('id')
    paginator = Paginator(obj, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    response = render(request, 'quiz_app/start_exam.html',
                      {'course': course, 'obj': obj, 'questions': questions})
    response.set_cookie('course_id', course.id)
    return response


@csrf_exempt
@login_required(login_url='/user_login')
def calculate_marks_view(request):
    course_id = request.COOKIES.get('course_id')
    course = Course.objects.get(id=course_id)
    total_score = 0
    answers = Question.objects.all().filter(course=course)
    anslist = []
    mrklist = []
    for i in answers:
        anslist.append(i.answer)
        mrklist.append(i.marks)
    for i in range(len(lst)):
        if lst[i] == anslist[i]:
            total_score = total_score + mrklist[i]
    user = request.user
    Result.objects.create(user=user, total_score=total_score)
    return render(request, 'quiz_app/view_result.html', {'total_score': total_score, 'course': course})


lst = []


@csrf_exempt
def save_ans(request):
    ans = request.GET.get('ans', None)
    global lst
    lst.append(ans)
    print(lst)
    return HttpResponse(ans)


@csrf_exempt
def home_page(request):
    if request.user.is_authenticated:
        lst.clear()
        return HttpResponseRedirect('/view-course')
    return render(request, 'quiz_app/index.html')
