from django.contrib import admin
from .models import Person, Counter

admin.site.register(Person)
admin.site.register(Counter)