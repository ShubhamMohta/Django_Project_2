from django.shortcuts import render
from django.core.mail import EmailMessage


def index_mail(request):


    email= EmailMessage('contact form', 'Hello' , 'shubhammohta09@gmail.com',['keshavmohta09@gmail.com'])
    email.send()
    return render(request,'index_mail.html')