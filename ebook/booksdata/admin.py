from django.contrib import admin
from . models import Books,Review,Types

# Register your models here.

admin.site.register(Books)
admin.site.register(Review)
admin.site.register(Types)
