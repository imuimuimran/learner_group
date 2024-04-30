from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Python Programmers'},
    {'id': 2, 'name': 'Java Programmers'},
    {'id': 3, 'name': 'C++ Programmers'},
]

def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')