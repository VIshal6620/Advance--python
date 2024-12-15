from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    loginId = models.EmailField()
    password = models.CharField(max_length=30)
    confirmPassword = models.CharField(max_length=30,default='')
    dob = models.DateField(max_length=30)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,default='')
    mobileNumber = models.CharField(max_length=50,default='')
    roleId = models.IntegerField()
    roleName = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_user'

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = 'sos_role'


class Marksheet(models.Model):
    rollNumber = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()

    class Meta:
        db_table = 'sos_Marksheet'


