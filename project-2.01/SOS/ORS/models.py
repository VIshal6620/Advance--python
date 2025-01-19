from datetime import datetime

from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginId = models.EmailField()
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20, default='')
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=20, default='')
    mobileNumber = models.CharField(max_length=15, default='')
    roleId = models.IntegerField()
    roleName = models.CharField(max_length=25)

    def get_key(self):
        return self.id

    def get_value(self):
        return self.firstName + '' + self.lastName

    class Meta:
        db_table = 'sos_user'


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.name

    class Meta:
        db_table = 'sos_role'


class Attribute(models.Model):
    display = models.CharField(max_length=50)
    datatype = models.CharField(max_length=50)
    isActive = models.CharField(max_length=40)
    description = models.CharField(max_length=30)

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.datatype

    class Meta:
        db_table = 'sos_attribute'
