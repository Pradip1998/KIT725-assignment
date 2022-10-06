from django.db import models


# Create your models here.


class Product(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image=models.ImageField(upload_to='pics')
    marked_price=models.PositiveIntegerField()
    selling_price=models.PositiveIntegerField()
    description=models.TextField()
    discount=models.BooleanField(default=False)
    return_policy=models.CharField(max_length=200,null=True,blank=True)
    view_count=models.PositiveIntegerField(default=0)

    def __str__(self):
         return self.title
class order(models.Model):
    cardholdername=models.CharField(max_length=200)
    cardnumber = models.CharField(max_length=200)
    cardtype = models.CharField(max_length=200)
    cardexpiry = models.DateField()
    csv = models.CharField(unique=True, max_length=200)


    def __str__(self):
         return self.cardholdername

