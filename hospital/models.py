from django.db import models

# Create your models here.

class Basic(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    class Meta:
        abstract = True

class Docter(Basic):
    special = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Patient(Basic):
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Docter,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name