from django.contrib import admin
from .models import Location, Category, Image

# Register your models here.
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)

