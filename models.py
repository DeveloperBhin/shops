from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class sellerpages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class Fashionpages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name



class Industrialproductspages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE) 
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class HealthProductspages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE) 
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class HomeDecorpages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)  
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class Sportspages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)  
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class Entertainmentpages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)  
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class Shoespages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)  
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class LuggageBagspages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)  
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class WatchJewelrypages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)  
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class KidsToyspages(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)  
        Name=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=20)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Email=models.EmailField(max_length=20)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Product_name=models.CharField(max_length=10)
        Price=models.CharField(max_length=20)
        Status=models.CharField(max_length=20)
        Brand=models.CharField(max_length=20)
        Delivery=models.CharField(max_length=20)
        Description=models.CharField(max_length=20)
        
        
def __str__(self):
        return self.Name

class Buyerform(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)  
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Ward=models.CharField(max_length=20)
        Phone=models.CharField(max_length=10)
        Contact_name=models.CharField(max_length=30)
        First_name=models.CharField(max_length=20)
        last_name=models.CharField(max_length=20)
        House_no=models.CharField(max_length=10)
        Email=models.EmailField(max_length=20)
       
        
def __str__(self):
        return self.user.username


class paypage(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)  
        Name=models.CharField(max_length=20)
      
        Image=models.ImageField(upload_to='network/', height_field=None, width_field=None, max_length=None,default=None)
     
        
        
def __str__(self):
        return self.Name





class Cart(models.Model):
      user = models.OneToOneField(User,on_delete=models.CASCADE)
      created_at=models.DateTimeField(auto_now_add=True) 
      
def __str__(self):
  return f"Cart of {self.user.username} " 

class CartItems(models.Model):
  
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Fashion=models.ForeignKey(Fashionpages,on_delete=models.CASCADE)
 
def __str__(self):
        return f"{self.fashion.Name}"



class IndustryItem(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Industry=models.ForeignKey(Industrialproductspages,on_delete=models.CASCADE)
  
def __str__(self):
        return f"{self.fashion.Name}"


class HealthItems(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Health=models.ForeignKey(HealthProductspages,on_delete=models.CASCADE)
  
def __str__(self):
        return f"{self.fashion.Name}"

class HomeItems(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Home=models.ForeignKey(HomeDecorpages,on_delete=models.CASCADE)
  
def __str__(self):
        return f"{self.fashion.Name}"


class SportsItems(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Sports=models.ForeignKey(Sportspages,on_delete=models.CASCADE)
  
def __str__(self):
        return f"{self.fashion.Name}"


class entertainmentItem(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Entertainment=models.ForeignKey(Entertainmentpages,on_delete=models.CASCADE)
  
def __str__(self):
        return f"{self.fashion.Name}"

class LuggageItems(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Luggage=models.ForeignKey(LuggageBagspages,on_delete=models.CASCADE)
  
def __str__(self):
        return f"{self.fashion.Name}"


class ShoesItems(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Shoes=models.ForeignKey(Shoespages,on_delete=models.CASCADE)
  
def __str__(self):
        return f"{self.fashion.Name}"


class KidsItems(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Kids=models.ForeignKey(KidsToyspages,on_delete=models.CASCADE)
  
def __str__(self):
        return f"{self.fashion.Name}"


class WatchItems(models.Model):
  cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
  Watch=models.ForeignKey(WatchJewelrypages,on_delete=models.CASCADE)
  
def __str__(self):
        return f"{self.fashion.Name}"

class Cartdetail(models.Model):
        
        Name=models.CharField(max_length=30)
        Brand=models.CharField(max_length=30)
        Status=models.CharField(max_length=30)
        Price=models.CharField(max_length=30)
        quantity=models.CharField(max_length=30)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
         
def __str__(self):
          return self.Name
  
class CartAdmin(models.Model):
        
        Name=models.CharField(max_length=30)
        Brand=models.CharField(max_length=30)
        Status=models.CharField(max_length=30)
        Price=models.CharField(max_length=30)
        quantity=models.CharField(max_length=30)
        Image=models.ImageField(upload_to='Uploads/', height_field=None, width_field=None, max_length=None,default=None)
        Region=models.CharField(max_length=20)
        District=models.CharField(max_length=20)
        Ward=models.CharField(max_length=20)
        Phone=models.CharField(max_length=50)
        Contact_name=models.CharField(max_length=100)
        First_name=models.CharField(max_length=20)
        last_name=models.CharField(max_length=20)
        House_no=models.CharField(max_length=10)
        Email=models.EmailField(max_length=50) 
        
        
def __str__(self):
          return self.Name