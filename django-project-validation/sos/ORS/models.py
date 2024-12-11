from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginId = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    dob = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_user'