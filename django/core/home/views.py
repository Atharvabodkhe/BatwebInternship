from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        en = Student(
            name = name,
            age = age,
            email = email,
            phone = phone,
            address = address
        )
        en.save()
        return HttpResponse('Form submitted successfully!')
    
    return render(request, "form.html")