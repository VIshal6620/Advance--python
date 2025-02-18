from datetime import datetime
from django.db import models
from django.db.models import DateField


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


class Initiative(models.Model):
    initiativeName = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    startDate = models.DateField(max_length=25)
    version = models.IntegerField()

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.initiativeName

    class Meta:
        db_table = 'sos_initiative'


class Employee(models.Model):
    fullName = models.CharField(max_length=50)
    userName = models.EmailField()
    password = models.CharField(max_length=50)
    birthDate = models.DateField(max_length=30)
    contactNumber = models.CharField(max_length=15, default='')

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.fullName

    class Meta:
        db_table = 'sos_employee'


class Client(models.Model):
    fullName = models.CharField(max_length=50)
    appointmentDate = models.DateField(max_length=40)
    phone = models.CharField(max_length=15, default='')
    illness = models.CharField(max_length=50)

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.fullName

    class Meta:
        db_table = 'sos_Client'


class Physician(models.Model):
    fullName = models.CharField(max_length=30)
    birthDate = models.DateField(max_length=20)
    phone = models.CharField(max_length=13, default='')
    specialization = models.CharField(max_length=50)

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.fullName

    class Meta:
        db_table = 'sos_Physician'


class Medication(models.Model):
    fullName = models.CharField(max_length=30)
    illness = models.CharField(max_length=50)
    prescriptionDate = models.DateField(max_length=20)
    dosage = models.CharField(max_length=8)

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.fullName

    class Meta:
        db_table = 'sos_Medication'


class Follow_Up(models.Model):
    client = models.CharField(max_length=30)
    physician = models.CharField(max_length=30)
    appointmentDate = models.DateField(max_length=15)
    charges = models.CharField(max_length=30)

    def get_key(self):
        return str(self.id)

    def get_value(self):
        return self.client + '' + self.physician

    class Meta:
        db_table = 'sos_Follow_Up'


class Staff_Member(models.Model):
    fullName = models.CharField(max_length=50)
    joiningDate = models.DateField(max_length=15)
    division = models.CharField(max_length=30)
    previousEmployer = models.CharField(max_length=50)

    def get_key(self):
        return (self.id)

    def geet_value(self):
        return self.division

    class Meta:
        db_table = 'sos_Staff_Member'


class Position(models.Model):
    designation = models.CharField(max_length=50)
    openingDate = models.DateField(max_length=12)
    requiredExperience = models.CharField(max_length=30)
    condition = models.CharField(max_length=15)

    def get_key(self):
        return (self.id)

    def get_value(self):
        return self.condition

    class Meta:
        db_table = 'sos_Position'


class Customer(models.Model):
    clientName = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=15)
    importance = models.CharField(max_length=30)

    def get_key(self):
        return (self.id)

    def get_value(self):
        return self.clientName

    class Meta:
        db_table = 'sos_Customer'


class Compensation(models.Model):
    staffMember = models.CharField(max_length=30)
    paymentAmount = models.CharField(max_length=20)
    dateApplied = models.DateField(max_length=15)
    state = models.CharField(max_length=20)

    def get_key(self):
        return (self.id)

    def get_value(self):
        return self.staffMember + '' + self.state

    class Meta:
        db_table = 'sos_Compensation'
