from django.shortcuts import render
from Stream import settings
from user import utils

def index(request):
    key = utils.create_key('K1ug4r4W','ws://90.188.92.68:3333/app/moony','signature', 'policy', '{\"url_expire\":1604377520178}' )

    return render(request, 'main.html', context={"key": key})
