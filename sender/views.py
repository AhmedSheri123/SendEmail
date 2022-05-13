from django.shortcuts import render
from django.http import HttpResponse
from .sendEmail import send_email
# Create your views here.

def sender(request):
    if request.method == "GET":
        content = request.GET['content']
        Subject = request.GET['Subject']
        receiver = request.GET['receiver']
        send_email(receiver, "Ahmed Sheri", content, Subject)
    return HttpResponse("")