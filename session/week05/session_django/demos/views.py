from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloBabyLion(request): # request 받아서
    return render(request, 'crazyDjango.html')
    # 이렇게 응답해줄거다