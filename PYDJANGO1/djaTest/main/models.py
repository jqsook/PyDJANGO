from django.db import models

# Create your models here.


class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

# To update main go to terminal and type in python3 manage.py makemigrations main
# To make the actual changes type in python3 manage.py migrate that creates a new file in the migrations that creates the actual database models.
