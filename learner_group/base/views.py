from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Python Programmers'},
    {'id': 2, 'name': 'Java Programmers'},
    {'id': 3, 'name': 'C++ Programmers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')