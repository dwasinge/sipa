from django.db import models


class SipaUser(models.Model):

    STUDENT = 'STUDENT'
    INSTRUCTOR = 'INSTRUCTOR'
    ADMIN = 'ADMIN'

    USER_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (INSTRUCTOR, 'Instructor'),
        (ADMIN, "Administrator"),
    ]

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dob = models.DateField()
    rank = models.CharField(max_length=25)
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    # STUDENT, INSTRUCTOR, ADMIN
