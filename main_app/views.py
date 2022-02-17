from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog, Toy, Feeding
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def dog_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', { 'dog': dog, 'feeding_form': feeding_form })

def toys_index(request):
    toys = Toy.objects.all()
    return render(request, 'toys/index.html', { 'toys': toys })

def toy_detail(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    return render(request, 'toys/detail.html', { 'toy': toy })


def add_feeding(request, dog_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('dog_detail', dog_id=dog_id)

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogUpdate(UpdateView):
    model = Dog
    fields = '__all__'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'


