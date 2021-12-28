# Quiz-Application
task to build a quiz application

Functions
Admin
- Create Admin account using command
```
python manage.py createsuperuser
```
Teacher
- Create account Then Login.
- After Login, can see Total Number Of Student, Course, Questions.
- Can Add, View, Delete Course/Exams.
- Can Add Questions To Respective Courses With Options, Correct Answer, And Marks.
- Can View And Delete Questions Too.

Student
- Create account.
- After Login, Can See How Many Courses/Exam And Questions.
- Can Give Exam Any Time, There Is No Limit On Number Of Attempt.
- Can View Marks and exam
- Question Pattern Is MCQ With 4 Options And 1 Correct Answer.
---
#third party package install:
   pip install django-widget-tweaks
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```
