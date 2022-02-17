from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })

class Dog:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Baby', 'chihuahua', 'foul little demon', 20),
  Dog('Rolo', 'bull mastiff', 'really bid', 2),
  Dog('Odin', 'minnie aussie', '3 legged cat', 2)
]
