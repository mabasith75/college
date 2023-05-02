import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from . models import Order
# Create your views here.



def details(request):
    return render(request, 'order.html')

def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        courses = request.POST.get('courses')
        purpose = request.POST.get('purpose')
        materials = request.POST.get('material')
        place_order = Order(name=name, dob=dob, age=age, gender=gender, phone_number=phone_number, email=email, address=address, department=department, courses=courses, purpose=purpose, materials=materials)
        place_order.save()
        return redirect('/')

    return render(request, 'order.html')



