from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length = 100)
    salary = models.FloatField()

    def __str__(self):
        return self.ename

    #pycharm testing git concept
    #this code from server
