from django.shortcuts import render
from .models import Dog
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def dog_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', { 'dog': dog })


