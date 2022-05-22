from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def password(request):
    caracteres = list('abcdefghijklmnñopqrstuvwxyz')
    passGenerada = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        caracteres.extend(list('!#$%&'))

    if request.GET.get('numbers'):
        caracteres.extend(list('1234567890'))

    for x in range(length):
        passGenerada += random.choice(caracteres)

    return render(request, 'password.html', {'contraseña':passGenerada})
