from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def hello(request, name):
    return render(request, "hello.html", {"name": name})

def saveToDb(request, name):
    Person.objects.create(name=name)

    count = Person.objects.count()
    return HttpResponse("<h2>You have inserted a name successfully</h2> <br> count = " + str(count))


def index(request):
    return HttpResponse("<h2>You have reached the homepage</h2>")
