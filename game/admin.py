from django.contrib import admin

from .models import CategoryType, Category, Question

myModels = [CategoryType, Category, Question]

admin.site.register(myModels)
