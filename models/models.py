from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=25)
    number = models.PositiveSmallIntegerField(unique=True)
    about = models.TextField(blank=True)
    email = models.EmailField()
    register_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.number}"
