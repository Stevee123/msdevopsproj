from django.db import models

# Create your models here.
class Course(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=500)
    Coursetitle = models.CharField(max_length=500)
    Frontcard = models.CharField(max_length=500)
    Backcard = models.CharField(max_length=500)