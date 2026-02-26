from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    cgpa = models.FloatField()

    def __str__(self):
        return self.user.username

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    eligibility_cgpa = models.FloatField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Placement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_selected = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.company.name}"


# Create your models here.
