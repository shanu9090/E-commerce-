from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# class AdminDB(models.Model):
    # Fname=models.CharField(max_length=100)
    # Email=models.EmailField(max_length=100)
    # Password=models.CharField(max_length=10)
    # def __str__(self):
        # return self.Fname

#    def __str__(self) -> str:
    #   return self.user
# def __str__(self):
        # return f'{self.user.username} Profile'
# 
class Woman_item(models.Model):
    Name=models.CharField(max_length=200)
    Category=models.CharField(max_length=100)
    image=models.ImageField(upload_to="Woman_item")
    Price=models.FloatField()
    Quantity=models.IntegerField()
   

class Man_item(models.Model):
    Name=models.CharField(max_length=200,default="")
    Category=models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to="Man_item")
    Price=models.FloatField()
    Quantity=models.IntegerField()
    Available=models.BooleanField(default=True)

class Kids_item(models.Model):
    Name=models.CharField(max_length=200,default="")
    Category=models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to="Man_item")
    Price=models.FloatField()
    Quantity=models.IntegerField()
    Available=models.BooleanField(default=True)

class Transaction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cat=models.CharField(max_length=50)
    cat_id=models.IntegerField()
    purchased_quan=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)

def __str__(self):
 return self.name  



class Customer(models.Model):
    STATE_CHOICES=(
     ('Bhopal', 'Bhopal'),
     ('Jabalpur', 'Jabalpur'),
     ('Uttar Pradesh', 'Uttar Pradesh'),
     ('West Bengal', 'West Bengal'),
)   
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,default="")    
    locality=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100,default="")
    def __str__(self) -> str:
     return self.name  

status_choices=(
    ('accepted','accepted'),
    ('Delivered','Delivered'),
    ('packed','packed'),
    ('cancel','cancel'),
    ('on the way','on the way'),
    
)
class Orderplace(models.Model):
    user  =   models.ForeignKey(User,on_delete=models.CASCADE)                                          
    customer=  models.ForeignKey(Customer,on_delete=models.CASCADE) 
    product=   models.ForeignKey(Woman_item,on_delete=models.CASCADE)  
    quantity= models.PositiveIntegerField()
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=status_choices,max_length=50,default='Pending')

    def __str__(self): 
       return self.user 
   

class ItemModel(models.Model):
    name = models.CharField(max_length = 100)
    amount = models.IntegerField()
    order_id = models.CharField(max_length = 100)
    razorpay_payment_id = models.CharField(max_length = 100,blank=True)
    paid = models.BooleanField(default=False)
    def _str_(self): 
        return self.name 
    
    # 
class Profile(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,default=1 )
   name=models.CharField(max_length=50)
   email=models.EmailField(max_length=20)
   age=models.IntegerField()
   image=models.ImageField(upload_to="profile_image",null=True,default="")
   mobilenumber=models.IntegerField()    
    # 