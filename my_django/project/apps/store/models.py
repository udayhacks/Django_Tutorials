from django.db import models


class collection (models.Model):
    title = models.CharField(max_length=255)


class product (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # also their is float field but rounding issues
    price =models.DecimalField(max_digits=12,decimal_places=3)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)


class Order(models.Model):
    cp = 'p'
    cc='c'
    cf ='f'
    choice_P= {
        
        cp :'pending',
        cc :'completed',
        cf :'failed'
    }
    placed_date = models.DateTimeField(auto_created=True,auto_now_add=True)
    payment_status = models.CharField(max_length=2,choices=choice_P, default=cp)
    
    
    
    
class customer (models.Model):
    MEMBERSHIP_CHOICES = {
        'B':'Bronze',
        'S':'Sliver',
        'G':'Gold'
    }
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default='B')
    
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    

    
class Address (models.Model):
    street = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    customer= models.OneToOneField(customer,on_delete=models.CASCADE,primary_key=True)
    
    
class Orderitems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(product,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    
    
class cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class cartitems(models.Model):
    cart = models.ForeignKey(cart,on_delete=models.CASCADE)
    product= models.ForeignKey(product ,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()    

