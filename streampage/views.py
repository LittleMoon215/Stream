from django.shortcuts import render
from Stream import settings

def get(request):
    print(settings.STATIC_URL)
    print(settings.STATIC_ROOT)
    return render(request, 'main.html')
