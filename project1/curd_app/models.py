from django.db import models


class Doctor(models.Model):
    GENDER = [("Male", 'Male'), ("Female", 'Female')]
    MARITAL_STATUS = [("Married", 'Married'), ("Unmarried", 'Unmarried')]
    patient_name = models.CharField(max_length=20)
    patient_relative_name = models.CharField(max_length=20)
    patient_mobile_number = models.IntegerField()
    patient_email = models.EmailField()
    patient_city = models.CharField(max_length=50)
    health_issue = models.CharField(max_length=30)
    appointment_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS)




