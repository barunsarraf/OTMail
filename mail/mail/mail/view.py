from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings



def index(request):
    return render(request, 'index.html')


def Send(request):
    if request.method == 'POST':
        subject = 'This is subject'
        message = 'this is msg part'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['barunsaraf1@gmail.com', ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        return HttpResponse('/thanks/')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')
