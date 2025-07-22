from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    people = [
        {'Name' : 'Akhil', 'Designation': 'Python Developer', 'Age' : 23},
        {'Name' : 'Jay', 'Designation': 'FullStack', 'Age' : 44},
        # {'Name' : 'Ramesh', 'Designation': 'RPA Developer', 'Age' : 32},
        # {'Name' : 'Chirag', 'Designation': 'UI/UX Developer', 'Age' : 25},
        # {'Name' : 'Jayesh', 'Designation': 'React', 'Age' : 49}
    ]
    for peoples in people:
        print(people)

    return render(request, 'index.html', context={'peoples' : people})
    # return HttpResponse("Hello, world!")

def contact(request):
    return render(request,'contact.html')