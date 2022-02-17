from django.contrib import admin

# Register your models here.
from .models import Dog, Toy, Feeding

admin.site.register(Dog)
admin.site.register(Toy)
admin.site.register(Feeding)