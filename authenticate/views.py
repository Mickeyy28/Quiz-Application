from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            message = {'error': 'invalid credentials'}
            context = message
            return render(request, 'authenticate/login.html', context)
    return render(request, 'authenticate/login.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print('error')
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    print('email already exits...')
                    return redirect('user_register')
                else:
                    user = User(username=username,
                                password=password, email=email)
                    user.set_password(password)
                    user.save()
                    return redirect('/user_login')
        else:
            print('error')
            return redirect('user_register')
    return render(request, 'authenticate/register.html')


def user_logout(request):
    logout(request)
    return redirect('/')
