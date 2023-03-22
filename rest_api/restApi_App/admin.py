from django.contrib import admin
from .models import *

# Register your models here.
all_models = [Item]

for md in all_models:
    admin.site.register(md)
