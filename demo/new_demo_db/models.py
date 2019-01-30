from django.db import models

# Create your models here.
class catagory_P(models.Model):
    catagory_id= models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=20)
    ctype=models.CharField(max_length=20)
    desc=models.CharField(max_length=70)

    def __str__(self):
        return '%s' % self.cname

class products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    pname =  models.IntegerField(foreing_key=catagory_P.catagory_id)
    p_catagory = models.CharField(max_length=20,)
    desc = models.CharField(max_length=70)
    image=models.FileField()
    price=models.IntegerField(null=False, Blank=False)