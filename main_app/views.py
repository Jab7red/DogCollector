from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
import uuid
import boto3
from .models import Dog, Toy, Photo

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'cat-collector-jb'

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
    toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', { 'dog': dog, 'feeding_form': feeding_form, 'toys': toys_dog_doesnt_have })

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

 
def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('dog_detail', dog_id=dog_id)



def add_photo(request, dog_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, dog_id=dog_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('dog_detail', dog_id=dog_id)

class DogCreate(CreateView):
    model = Dog
    fields = ('name', 'breed', 'description', 'age')

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


