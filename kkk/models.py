from django.db import models

class Grade(models.Model):
    g_name = models.CharField(max_length=200)

class Student(models.Model):
    s_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    age = models.IntegerField()
    zhiwei = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    g = models.ForeignKey(Grade,on_delete=True)
