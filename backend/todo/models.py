from django.db import models
from list_of_users.models import Users


class Project(models.Model):
    name = models.CharField(max_length=64)
    link_to_repo = models.CharField(max_length=255, blank=True)
    users = models.ManyToManyField(Users)

    def __str__(self):
        return self.name


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    create_time = models.TimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    update_time = models.TimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
