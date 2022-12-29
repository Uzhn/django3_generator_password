from django.shortcuts import render
import random


def home(request):
    template = 'generator/home.html'
    return render(request, template)


def password(request):
    template = 'generator/password.html'
    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=-'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    context = {
        'password': thepassword,
    }
    return render(request, template, context)


def about(request):
    template = 'generator/about.html'
    return render(request, template)
