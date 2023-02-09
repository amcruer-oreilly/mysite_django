from django.contrib import admin

# Register your models here.
#import the Question model from polls/models.py
from .models import Question

# register the Question model with the admin site
admin.site.register(Question)
