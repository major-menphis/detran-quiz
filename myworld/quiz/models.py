from django.db import models

# Create your models here.
class Members(models.Model):
    fullName = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    points = models.FloatField()
    quizResolved = models.IntegerField()
    questionsResolved = models.IntegerField()
    registrationDate = models.DateField(auto_now_add=True)