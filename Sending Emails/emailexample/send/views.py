from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hello',
              'Hi, this is an automated message',
              'muskan124.jassal@gmail.com',
              ['dejade4341@vy89.com'],
              fail_silently=False)
    return render(request, 'send/index.html')