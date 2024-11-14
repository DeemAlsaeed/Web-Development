from django.db import models
from django.contrib.auth.models import User
from  core.models import Product
from django.db.models.signals import post_save


class ShippingAdress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name=models.CharField(max_length=255)
    shipping_email=models.CharField(max_length=255)
    shipping_address1=models.CharField(max_length=255)
    shipping_address2=models.CharField(max_length=255,null=True,blank=True)
    shipping_city=models.CharField(max_length=255)
    shipping_zipcode=models.CharField(max_length=255,null=True,blank=True)
    shipping_state=models.CharField(max_length=255,null=True,blank=True)
    shipping_country=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural="Shipping Adress"

    def __str__(self):
        return f'Shipping Adress - {str(self.id)}'
    
def create_shipping(sender,instance, created,**kwargs):
    if created :
        user_shipping=ShippingAdress(user=instance)
        user_shipping.save()

post_save.connect(create_shipping,sender=User)


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    shipping_address=models.TextField(max_length=1500000)
    amount_paid=models.DecimalField(max_digits=7,decimal_places=2)
    date_ordered=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'order - {str(self.id)}'
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    quantity = models.PositiveBigIntegerField(default=1)
    price=models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return f'order item - {str(self.id)}'

