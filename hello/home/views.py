from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.


def index(request):

    return render(request, 'index.html')
    # return HttpResponse('this is the home page')


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('this is the about page')


def services(request):
    return render(request, 'services.html')
    # return HttpResponse('this is the services page')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        about = request.POST.get('about')
        contact = Contact(name=name, email=email, phone=phone,
                          about=about, date=datetime.today())
        contact.save()
        messages.success(request, 'YOUR FORM IS UPLODED.')
    return render(request,'contact.html')
    # return HttpResponse('this is the contact page')
