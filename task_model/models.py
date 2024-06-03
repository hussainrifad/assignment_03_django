from django.db import models
from task_category.models import TaskCategoryModel

class TaskModel(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField(max_length=400)
    task_category = models.ManyToManyField(TaskCategoryModel)
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.task_title
