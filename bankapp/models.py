from django.db import models

# Create your models here.
class Banking(models.Model):
    account_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    amount = models.FloatField()
    address = models.TextField(max_length=100)
    mob_no = models.BigIntegerField()
    
def __str__(self):
    return str(self.account_no )



    
