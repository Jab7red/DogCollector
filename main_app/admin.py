from django.contrib import admin

# Register your models here.
from .models import Dog, Toy, Feeding, Photo

admin.site.register(Dog)
admin.site.register(Toy)
admin.site.register(Feeding)
admin.site.register(Photo)