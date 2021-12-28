from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    marks = models.PositiveIntegerField()

    def __str__(self):
        return self.question


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user}"
