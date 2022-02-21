from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    hiredate = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.role)



class Register(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)