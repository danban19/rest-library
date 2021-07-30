from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name, self.surname, self.birth

class Book(models.Model):
    pass
