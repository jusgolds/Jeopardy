from django.db import models

class CategoryType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    clue = models.CharField(max_length=200)
    correct_ans = models.CharField(max_length=200)

    def __str__(self):
        return self.clue
