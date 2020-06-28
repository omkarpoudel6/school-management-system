from django.db import models

#Create your models here.
class Student_info(models.Model):
    student_id = models.IntegerField(unique=True)
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    grade = models.IntegerField()
    fathername = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    #image=models.FileField(upload_to='studentpicture')

    def __str__(self):
        return self.firstname

class Results(models.Model):
    student_id=models.IntegerField()
    term=models.IntegerField()
    grade=models.IntegerField()
    english=models.IntegerField()
    nepali = models.IntegerField()
    math = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    ehp = models.IntegerField(blank=True)
    optionali = models.IntegerField(blank=True)
    optionalii = models.IntegerField(blank=True)
    grammar=models.IntegerField(blank=True)
    optionalmath = models.IntegerField(blank=True)
    computer = models.IntegerField(blank=True)
    gk = models.IntegerField(blank=True)
    drawing = models.IntegerField(blank=True)
    totalfullmark=models.IntegerField(default=500)
    totalpassmark=models.IntegerField(default=200)
    marksobtained=models.IntegerField()
    percentage=models.FloatField(default=0)
    division=models.TextField(default="fail")

    def __int__(self):
        return self.student_id

class Bill(models.Model):
    student_id=models.IntegerField()
    admission=models.IntegerField()
    baisakh=models.IntegerField(blank=True)
    jestha=models.IntegerField(blank=True)
    ashad=models.IntegerField(blank=True)
    shrawan=models.IntegerField(blank=True)
    bhadra=models.IntegerField(blank=True)
    aswin=models.IntegerField(blank=True)
    kartik=models.IntegerField(blank=True)
    mangsir=models.IntegerField(blank=True)
    poush=models.IntegerField(blank=True)
    magh=models.IntegerField(blank=True)
    falgun=models.IntegerField(blank=True)
    chaitra=models.IntegerField(blank=True)

    def __int__(self):
        return self.student_id

class Transaction(models.Model):
    sid=models.IntegerField()
    amount=models.IntegerField()
    remarks=models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.sid









