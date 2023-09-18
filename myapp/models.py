from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta :
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=Category, related_name='category', on_delete=models.CASCADE)

    class Meta :
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.name