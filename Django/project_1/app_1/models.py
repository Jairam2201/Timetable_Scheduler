from django.db import models


# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    confirm_password=models.CharField(max_length=150)
    class Meta:
        db_table="table_signup"
        
class Date(models.Model):
    date=models.DateField()
    user_id = models.ForeignKey(Signup,on_delete=models.CASCADE)
    class Meta:
        db_table="table_date"


class s(models.Model):
    user_id = models.ForeignKey(Signup,on_delete=models.CASCADE)

    date_field=models.DateField()
    one=models.CharField(max_length=100)
    two=models.CharField(max_length=100)
    three=models.CharField(max_length=100)
    four=models.CharField(max_length=100)
    five=models.CharField(max_length=100)
    six=models.CharField(max_length=100)
    total=models.IntegerField()
    changes=models.IntegerField(null=True)
    class Meta:
        db_table="table_savework"

class Edit(models.Model):
    date_field=models.DateField()
    user_id = models.ForeignKey(Signup,on_delete=models.CASCADE)

   
    class Meta:
        db_table="table_edit"
        
