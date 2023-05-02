from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('courses:details'))
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['password1']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
            return redirect('register')
    return render(request, 'register.html')





