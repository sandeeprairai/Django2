from django.db import models

# Create your models here.

#model created
class Teacher(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)


    #This object is used for converting object into string
    def __str__(self) -> str:
        return self.Firstname
