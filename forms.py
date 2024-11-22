from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class sellepageForm(forms.ModelForm):
    class Meta:
        model=sellerpages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class FashionForm(forms.ModelForm):
    class Meta:
        model=Fashionpages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class IndustrialproductsForm(forms.ModelForm):
    class Meta:
        model=Industrialproductspages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class HealthProductsForm(forms.ModelForm):
    class Meta:
        model=HealthProductspages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class SportsForm(forms.ModelForm):
    class Meta:
        model=Sportspages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class EntertainmentForm(forms.ModelForm):
    class Meta:
        model=Entertainmentpages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class ShoesForm(forms.ModelForm):
    class Meta:
        model=Shoespages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class LuggageBagsForm(forms.ModelForm):
    class Meta:
        model=LuggageBagspages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class WatchJewelryForm(forms.ModelForm):
    class Meta:
        model=WatchJewelrypages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class KidsToysForm(forms.ModelForm):
    class Meta:
        model=KidsToyspages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class HomeDecorForm(forms.ModelForm):
    class Meta:
        model=HomeDecorpages
        fields=('Name','Phone','Contact_name','Region','District','Email','Product_name','Image','Price','Status','Brand','Delivery','Description')
        
class Buyer(forms.ModelForm):
    class Meta:
        model=Buyerform
        fields=('Phone','Contact_name','Region','District','Ward','First_name','last_name','House_no','Email')
        
class payForm(forms.ModelForm):
    class Meta:
        model=paypage
        fields=('Name','Image')
        
class RegistrationForm(UserCreationForm):
   class Meta:
        model = User
        fields = ('username','password1','password2')
        
        def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
        # Remove help texts for password fields
         self.fields['password1'].help_text = None
         self.fields['password2'].help_text = None
     
        
        


class LoginsForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    


    

     