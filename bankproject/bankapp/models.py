from django.db import models


# class genderone(models.Model):
#     STATUS_CHOICES = (('m', 'male'), ('f', 'femlae'))
    # gender=models.CharField(max_length=20,choices=STATUS_CHOICES)
class registration(models.Model):
    STATUS_CHOICES = (('m', 'male'), ('f', 'femlae'))
    name=models.CharField(max_length=250)
    dob=models.DateField()
    ph=models.IntegerField()
    email=models.CharField(max_length=50)
    # gender = models.ForeignKey(genderone,on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,choices=STATUS_CHOICES)
    address=models.TextField()
    actype=models.CharField(max_length=50,null=True)
    material=models.CharField(max_length=50,null=True)
    state=models.TextField(null=True,max_length=10)
    district=models.TextField(null=True,max_length=10)
    branch=models.TextField(null=True,max_length=10)



def __str__(self):
        return self.name

