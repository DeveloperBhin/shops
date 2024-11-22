from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

from django.http import HttpResponse
# Create your views here.
    
def Registerpage(request):
    if request.method=='POST':
      form=RegistrationForm(request.POST)
      if form.is_valid():
          form.save()
          user=form.cleaned_data.get('username')
    
          return redirect('loginpage')
      else:
          return render(request, 'login.html',{'form':form})
     
      
    else: 
     form = RegistrationForm()
    
    context={
        'form':form
    }
    
    return render(request,'register.html',context)

    
  



def loginpage(request):
    if request.method == 'POST':
        form = LoginsForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
      
            login(request, user)
            if user.username=='norbeth559@gmail.com':
              return redirect('Adminhomepage')
            else:
              return redirect('index')
    else:
        form = LoginsForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def index(request):
    if request.method=='GET':
      sel=WatchJewelrypages.objects.last()
      sel1=KidsToyspages.objects.last()
      sel2=Fashionpages.objects.last()
      sel3=Industrialproductspages.objects.last()
      sel4=HealthProductspages.objects.last()
      sel5=HomeDecorpages.objects.last()
      sel6=Sportspages.objects.last()
      sel7=Entertainmentpages.objects.last()
      sel8=Shoespages.objects.last()
      sel9=LuggageBagspages.objects.last()
      sels=sellerpages.objects.first()
      sels1=KidsToyspages.objects.first()
      sels2=Fashionpages.objects.first()
      sels3=Industrialproductspages.objects.first()
      sels4=HealthProductspages.objects.first()
      sels5=HomeDecorpages.objects.first()
      sels6=Sportspages.objects.first()
      sels7=Entertainmentpages.objects.first()
      sels8=Shoespages.objects.first()
      sels9=LuggageBagspages.objects.first()
      qs=Fashionpages.objects.all()
      sal1 = qs[2] if qs.count() > 2 else None 
      qs=WatchJewelrypages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
      qs=LuggageBagspages.objects.all()
      sal3 = qs[2] if qs.count() > 2 else None 
      qs=Shoespages.objects.all()
      sal4 = qs[2] if qs.count() > 2 else None 
      qs=Entertainmentpages.objects.all()
      sal5 = qs[2] if qs.count() > 2 else None 
      qs=Sportspages.objects.all()
      sal6 = qs[2] if qs.count() > 2 else None 
      qs=HomeDecorpages.objects.all()
      sal7 = qs[2] if qs.count() > 2 else None 
      qs=HealthProductspages.objects.all()
      sal8 = qs[2] if qs.count() > 2 else None 
      qs=Industrialproductspages.objects.all()
      sal9 = qs[2] if qs.count() > 2 else None 
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')
     
    context={
        'sel':sel,
        'sel1':sel1,
        'sel2':sel2,
        'sel3':sel3,
        'sel4':sel4,
        'sel5':sel5,
        'sel6':sel6,
        'sel7':sel7,
        'sel8':sel8,
        'sel9':sel9,
         'sels':sels,
        'sels1':sels1,
        'sels2':sels2,
        'sels3':sels3,
        'sels4':sels4,
        'sels5':sels5,
        'sels6':sels6,
        'sels7':sels7,
        'sels8':sels8,
        'sels9':sels9,
        'sal1':sal1,
        'sal2':sal2,
        'sal3':sal3,
        'sal4':sal4,
        'sal5':sal5,
        'sal6':sal6,
        'sal7':sal7,
        'sal8':sal8,
        'sal9':sal9,
        'image1':image1,
        'image0':image0,
        
    }    
    return render(request,'index.html',context)

@login_required

def Fashionpage(request):
    if request.method=='POST':
      form=FashionForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      
      return redirect('Fashionconfirm')
    else: 
     form = FashionForm()
    
    
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'form':form,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'Fashionpage.html',context)
  
def Fashionconfirm(request):
 
    sel=Fashionpages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'Fashionconfirm.html',context)



def Industrialproductspage(request):
    if request.method=='POST':
      form=IndustrialproductsForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('Industrialproductsconfirm')
    else: 
     form = IndustrialproductsForm()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    
    context={
        'form':form,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'Industrialproducts.html',context)

  
def Industrialproductsconfirm(request):
 
    if request.method=='GET':
      sel=Industrialproductspages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'Industrialproductsconfirm.html',context)



 
def HealthProductspage(request):
    if request.method=='POST':
      form=HealthProductsForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('HealthProductsconfirm')
    else: 
     form = HealthProductsForm()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    
    context={
        'form':form,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'HealthProducts.html',context)
  
def HealthProductsconfirm(request):
 
    if request.method=='GET':
      sel=HealthProductspages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'HealthProductsconfirm.html',context)




def HomeDecorpage(request):
    if request.method=='POST':
      form=HomeDecorForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('HomeDecorconfirm')
    else: 
     form = HomeDecorForm()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile') 
    
    context={
        'form':form,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'HomeDecor.html',context)
   
def HomeDecorconfirm(request):
 
    if request.method=='GET':
      sel=HomeDecorpages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image0':image0,
        'image1':image1
    }    
    
    return render(request,'HomeDecorconfirm.html',context)




def Sportspage(request):
    if request.method=='POST':
      form=SportsForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('Sportsconfirm')
    else: 
     form = SportsForm()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    
    context={
        'form':form,
        'image0':image0,
        'image1':image1
        
    }
    
    return render(request,'Sports.html',context)
     
def Sportsconfirm(request):
 
    if request.method=='GET':
      sel=Sportspages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'sel':sel,
        'image1':image1,
        'iamge0':image0
    }    
    
    return render(request,'sportsconfirm.html',context)




def Entertainmentpage(request):
    if request.method=='POST':
      form=EntertainmentForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('Entertainmentconfirm')
    else: 
     form = EntertainmentForm()
     image1 = get_object_or_404(paypage, Name='shop')
     image2 = get_object_or_404(paypage, Name='profile')
    
    context={
        'form':form,
        'image1':image1,
        'image2':image2
    }
    
    return render(request,'Entertainment.html',context)
  
def Entertainmentconfirm(request):
 
    if request.method=='GET':
      sel=Entertainmentpages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'Entertainmentconfirm.html',context)




def LuggageBagspage(request):
    if request.method=='POST':
      form=LuggageBagsForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('LuggageBagsconfirm')
    else: 
     form = LuggageBagsForm()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile') 
    
    context={
        'form':form,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'LuggageBags.html',context)
    
def LuggageBagsconfirm(request):
 
    if request.method=='GET':
      sel=LuggageBagspages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'LuggageBagsconfirm.html',context)



def Shoespage(request):
    if request.method=='POST':
      form=ShoesForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('Shoesconfirm')
    else: 
     form = ShoesForm()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile') 
    
    context={
        'form':form,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'Shoes.html',context)
    
def Shoesconfirm(request):
 
    if request.method=='GET':
      sel=Shoespages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'Shoesconfirm.html',context)



 
def WatchJewelrypage(request):
    if request.method=='POST':
      form=WatchJewelryForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('WatchJewelryconfirm')
    else: 
     form = WatchJewelryForm()
    
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'form':form,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'WatchJewel.html',context)
     
def WatchJewelryconfirm(request):
 
    if request.method=='GET':
      sel=WatchJewelrypages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'WatchJewelconfirm.html',context)




def KidsToyspage(request):
    if request.method=='POST':
      form1=KidsToysForm(request.POST,request.FILES)
      instance = form1.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('KidsToysconfirm')
       
    else: 
       form1 = KidsToysForm()
     
    
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'form1':form1,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'KidsToys.html',context)
    
def KidsToysconfirm(request):
 
    if request.method=='GET':
      sel=KidsToyspages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'KidsToysconfirm.html',context)



def sellerpage(request):
    if request.method=='POST':
      form=sellepageForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('sellerconfirm')
    else: 
     form = sellepageForm()
    
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'form':form,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'sellerpage.html',context)
   
def sellerconfirm(request):
 
    if request.method=='GET':
      sel=Fashionpages.objects.last()
      sel1=Industrialproductspages.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'sel1':sel1,
        'image1':image1,
        'image0':image0
    }   
    
    return render(request,'sellerconfirm.html',context)



def Fashionp(request):
 
    sel1=Fashionpages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel1':sel1,
        'image1':image1,
        'image0':image0
    }     
    
    return render(request,'Fashionp.html',context)

def Industrialpage (request):
 
    if request.method=='GET':
      sel=Industrialproductspages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'Industrialpage.html',context)

def Healthpage(request):
 
    if request.method=='GET':
      sel=HealthProductspages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }     
    
    return render(request,'Healthpage.html',context)

def Homepage(request):
 
    if request.method=='GET':
      
      sel=HomeDecorpages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'Homepage.html',context)

def Sportpage(request):
 
    if request.method=='GET':
      sel=Sportspages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }  
    return render(request,'Sportpage.html',context)

def Enterpage(request):
 
    if request.method=='GET':
      sel1=Entertainmentpages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel1':sel1,
        'image1':image1,
        'image0':image0
    }     
    
    return render(request,'Enterpage.html',context)

def Shoepage(request):
 
    if request.method=='GET':
      sel=Shoespages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }     
    
    return render(request,'Shoepage.html',context)
 
def Luggagepage(request):
 
    if request.method=='GET':
      sel=LuggageBagspages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }  
    return render(request,'Luggagepage.html',context)

def Watchpage(request):
 
    if request.method=='GET':
      sel=WatchJewelrypages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'Watchpage.html',context)

def Kidspage(request):
 
    if request.method=='GET':
      sel=KidsToyspages.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }    
    
    return render(request,'kidspage.html',context)

def productdetail(request,id=id):
 
   
      sel=get_object_or_404(Fashionpages,id=id)
      sal=Fashionpages.objects.first()
      sel1=Fashionpages.objects.last()
      qs=Fashionpages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
        'sel':sel,
        'image1':image1,
        'image0':image0,
   
        'sal':sal,
        'sel1':sel1,
        'sal2':sal2
    }    
    
      return render(request,'productdetail.html',context)

def cart_detail(request):
    cart=Cart.objects.all()
    cart_items=CartItems.objects.filter() 
    buyer=Buyerform.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
 
     
    return render(request,'cart_detail.html',{'cart':cart,'buyer':buyer,'cart_items':cart_items,'image1':image1,'image0':image0})

def industrydetail(request,id=id):
 
    if request.method=='GET':
      sel1=get_object_or_404(Industrialproductspages,id=id)
      sal=Industrialproductspages.objects.first()
      sal1=Industrialproductspages.objects.last()
      qs=Industrialproductspages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
       
        'image1':image1,
        'image0':image0,
   
        'sel1':sel1,
        'sal':sal,
        'sal1':sal1,
        'sal2':sal2
    }    
    
    return render(request,'industrydetail.html',context)

def Healthdetail(request,id=id):
 
    if request.method=='GET':
      sel1=get_object_or_404(HealthProductspages,id=id)
      sal=HealthProductspages.objects.first()
      sal1=HealthProductspages.objects.last()
      qs=HealthProductspages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
      
        'image1':image1,
        'image0':image0,
  
        'sel1':sel1,
        'sal':sal,
        'sal1':sal1,
        'sal2':sal2
    }    
    
    return render(request,'Healthdetail.html',context)

def sportdetail(request,id=id):
 
    if request.method=='GET':
      sel1=get_object_or_404(Sportspages,id=id)
      sal=Sportspages.objects.first()
      sal1=Sportspages.objects.last()
      qs=Sportspages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        
        'image1':image1,
        'image0':image0,
       'sel1':sel1,
        'sal':sal,
        'sal1':sal1,
        'sal2':sal2
    }    
    
    return render(request,'sportdetail.html',context)

def enterdetail(request,id=id):
 
    if request.method=='GET':
      sel1=get_object_or_404(Entertainmentpages,id=id)
      sal=Entertainmentpages.objects.first()
      sal1=Entertainmentpages.objects.last()
      qs=Entertainmentpages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        
        'image1':image1,
        'image0':image0,
   
        'sel1':sel1,
        'sal':sal,
        'sal1':sal1,
        'sal2':sal2
        
    }    
    
    return render(request,'enterdetail.html',context)

def shoedetail(request,id=id):
 
    if request.method=='GET':
      sel1=get_object_or_404(Shoespages,id=id)
      sal=Shoespages.objects.first()
      sal1=Shoespages.objects.last()
      qs=Shoespages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
       
        'image1':image1,
        'image0':image0,
        'sel1':sel1,
        'sal':sal,
        'sal1':sal1,
        'sal2':sal2
    }    
    
    return render(request,'shoedetail.html',context)


def luggagedetail(request,id=id):
 
    if request.method=='GET':
      sel1=get_object_or_404(LuggageBagspages,id=id)
      sal=LuggageBagspages.objects.first()
      sal1=LuggageBagspages.objects.last()
      qs=LuggageBagspages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        
        'image1':image1,
        'image0':image0,
   
        'sel1':sel1,
        'sal':sal,
        'sal1':sal1,
        'sal2':sal2
    }    
    
    return render(request,'luggagedetail.html',context)

def jeweldetail(request,id=id):
 
    if request.method=='GET':
      sel1=get_object_or_404(WatchJewelrypages,id=id)
      sal=WatchJewelrypages.objects.first()
      sal1=WatchJewelrypages.objects.last()
      qs=WatchJewelrypages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
       
        'image1':image1,
        'image0':image0,
   
        'sel1':sel1,
        'sal':sal,
        'sal1':sal1,
        'sal2':sal2
    }    
    
    return render(request,'jeweldetail.html',context)

def kidsdetail(request,id=id):
 
    if request.method=='GET':
      sel1=get_object_or_404(KidsToyspages,id=id)
      sal=KidsToyspages.objects.first()
      sal1=KidsToyspages.objects.last()
      qs=KidsToyspages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        
        'image1':image1,
        'image0':image0,

        'sel1':sel1,
        'sal':sal,
        'sal1':sal1,
        'sal2':sal2
    }    
    
    return render(request,'Kidsdetail.html',context)

def Homedetail(request,id=id):
 
    if request.method=='GET':
      sel1=get_object_or_404(HomeDecorpages,id=id)
      sal=HomeDecorpages.objects.first()
      sal1=HomeDecorpages.objects.last()
      qs=HomeDecorpages.objects.all()
      sal2 = qs[2] if qs.count() > 2 else None 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        
        'image1':image1,
        'image0':image0,
  
        'sel1':sel1,
        'sal':sal,
        'sal1':sal1,
        'sal2':sal2
    }    
    
    return render(request,'Homedetail.html',context)



def buyform(request):
    if request.method == 'POST':
        form = Buyer(request.POST)
          # Ensure the form is valid
        instance = form.save(commit=False)  # Use commit=False here
        instance.user = request.user  # Assign the user to the instance
        instance.save()  # Save the instance without any arguments
        return redirect('delivery')  # Redirect to the desired URL
    else:
        form = Buyer()  # Create a new form instance
    if request.method=='GET':
      
      sel1=Cartdetail.objects.last()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'sel1':sel1,
        'form':form,
        'image1':image1,
        'image0':image0
    }
    return render(request, 'Buyer.html', context)


def paymentform(request):
    if request.method=='POST':
      form=payForm(request.POST,request.FILES)
      instance = form.save(commit=False)
      instance.user = request.user  # Assign the logged-in user
      instance.save()
      return redirect('sellerconfirm')
    else: 
     form = payForm()
    
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')
    context={
        'form':form,
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'payment.html',context)


 
def networkform(request):
    if request.method=='GET':
     image1 = get_object_or_404(paypage, Name='Vodacom')
     image2 = get_object_or_404(paypage, Name='Tigo')
     image3 = get_object_or_404(paypage, Name='Aitel')
     image4 = get_object_or_404(paypage, Name='Halotel')
    image = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
       
        'image':image,
        'image0':image0,
   
         'image1': image1,
         'image2': image2,
         'image3': image3,
         'image4': image4,
        
    }
     

    return render(request,'network.html',context)


def vodacompay(request):
    if request.method=='GET':
     image1 = get_object_or_404(paypage, Name='shop')
     image0 = get_object_or_404(paypage, Name='profile')
     context={
    
        'image1':image1,
        'image0':image0
    }
    return render(request,'vodacompay.html',context)

  
def airtelpay(request):
    if request.method=='GET':
     image1 = get_object_or_404(paypage, Name='shop')
     image0 = get_object_or_404(paypage, Name='profile')
     context={
      
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'airtelpay.html',context)

      
def tigopay(request):
    if request.method=='GET':
     image1 = get_object_or_404(paypage, Name='shop')
     image0 = get_object_or_404(paypage, Name='profile')
     context={
      
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'tigopay.html',context)

       
def halotelpay(request):
    if request.method=='GET':
     image1 = get_object_or_404(paypage, Name='shop')
     image0 = get_object_or_404(paypage, Name='profile')
    context={
       
        'image1':image1,
        'image0':image0
    }
    
    return render(request,'halotelpay.html',context)

  
def Adminhomepage(request):
    if request.method=='GET':
     image7 = get_object_or_404(paypage, Name='Buyer')
     image5 = get_object_or_404(paypage, Name='Seller')
     image6 = get_object_or_404(paypage, Name='User')
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
       
        'image1':image1,
        'image0':image0,
    
         'image7': image7,
         'image5': image5,
         'image6': image6,
         
        
    }
    return render(request,'Adminhomepage.html',context)  
       
 
    




def logout(request):
   
    return redirect('loginpage')
    
  
 
def Fashionbuyer(request,fashion_id):
      sel=get_object_or_404(Fashionpages,id=fashion_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=CartItems.objects.get_or_create(cart=cart,Fashion=sel)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
    
    
      context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }  

      
      return render(request,'buyer.html',context) 
  
  
def Industrybuyer(request,industry_id):
      sel1=get_object_or_404(Industrialproductspages,id=industry_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=IndustryItem.objects.get_or_create(cart=cart,Industry=sel1)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
        'sel1':sel1,
        'image1':image1,
        'image0':image0
    }  
      return render(request,'buyer.html',context)
     
def Healthbuyer(request,health_id):
      sel=get_object_or_404(HealthProductspages,id=health_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=HealthItems.objects.get_or_create(cart=cart,Health=sel)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }  
      
      return render(request,'buyer.html',context)

def Homebuyer(request,home_id):
      sel1=get_object_or_404(HomeDecorpages,id=home_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=HomeItems.objects.get_or_create(cart=cart,Home=sel1)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
        'sel1':sel1,
        'image1':image1,
        'image0':image0
    }  
      return render(request,'buyer.html',context)

def Sportsbuyer(request,sports_id):
      sel1=get_object_or_404(Sportspages,id=sports_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=SportsItems.objects.get_or_create(cart=cart,Sports=sel1)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
        'sel1':sel1,
        'image1':image1,
        'image0':image0
    }  

      return render(request,'buyer.html',context)


def Entertainmentbuyer(request,entertainment_id):
      sel1=get_object_or_404(Entertainmentpages,id=entertainment_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=entertainmentItem.objects.get_or_create(cart=cart,Entertainment=sel1)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
          'sel1':sel1,
          'image1':image1,
          'image0':image0
    }  
      return render(request,'buyer.html',context)
  
  
def Luggagebuyer(request,luggage_id):
      sel1=get_object_or_404(LuggageBagspages,id=luggage_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=LuggageItems.objects.get_or_create(cart=cart,Luggage=sel1)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
        'sel1':sel1,
        'image1':image1,
        'image0':image0
    }  
      return render(request,'buyer.html',context)

def Shoesbuyer(request,shoes_id):
      sel1=get_object_or_404(Shoespages,id=shoes_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=ShoesItems.objects.get_or_create(cart=cart,Shoes=sel1)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
        'sel1':sel1,
        'image1':image1,
        'image0':image0
    }  
      return render(request,'buyer.html',context)
  

def Kidsbuyer(request,kids_id):
      sel1=get_object_or_404(KidsToyspages,id=kids_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=KidsItems.objects.get_or_create(cart=cart,Kids=sel1)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
        'sel1':sel1,
        'image1':image1,
        'image0':image0
    }  
      
      return render(request,'buyer.html',context)


def Watchbuyer(request,watch_id):
      sel=get_object_or_404(WatchJewelrypages,id=watch_id)
     
     
      cart,created=Cart.objects.get_or_create(user=request.user)
      cart_item,created=WatchItems.objects.get_or_create(cart=cart,Watch=sel)
      if not created:
         cart_item.save()
         return redirect('buyform')
     
    
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
          'sel':sel,
          'image1':image1,
         'image0':image0
    }        
      return render(request,'buyer.html',context)                                       
    
def Buyerdetail(request):
 
    if request.method=='GET':
      sel=Buyerform.objects.all()
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
    context={
        'sel':sel,
        'image1':image1,
        'image0':image0
    }  
    
    
    return render(request,'buyerdetail.html',context)
        
        
def industrybuyer(request):
    cart=Cart.objects.all()
    cart_items=IndustryItem.objects.filter() 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
        
      
        
   
    
     
    return render(request,'industrybuyer.html',{'cart':cart,'cart_items':cart_items,'image1':image1,
        'image0':image0})
     
def healthbuyer(request):
    cart=Cart.objects.all()
    cart_items=HealthItems.objects.filter() 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
       
    
     
    return render(request,'healthbuyer.html',{'cart':cart,'cart_items':cart_items,'image1':image1,
        'image0':image0})
     
       

def homebuyer(request):
    cart=Cart.objects.all()
    cart_items=HomeItems.objects.filter() 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
      
     
    return render(request,'homebuyer.html',{'cart':cart,'cart_items':cart_items,'image1':image1,
        'image0':image0})
     

def sportbuyer(request):
    cart=Cart.objects.all()
    cart_items=SportsItems.objects.filter() 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
      
     
    return render(request,'sportbuyer.html',{'cart':cart,'cart_items':cart_items,'image1':image1,
        'image0':image0})
     

def entertainbuyer(request):
    cart=Cart.objects.all()
    cart_items=entertainmentItem.objects.filter() 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
      
     
    return render(request,'entertainbuyer.html',{'cart':cart,'cart_items':cart_items,'image1':image1,
        'image0':image0})
     

def luggagebuyer(request):
    cart=Cart.objects.all()
    cart_items=LuggageItems.objects.filter() 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
      
     
    return render(request,'luggagebuyer.html',{'cart':cart,'cart_items':cart_items,'image1':image1,
        'image0':image0})
     

def shoebuyer(request):
    cart=Cart.objects.all()
    cart_items=ShoesItems.objects.filter() 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
       
     
    return render(request,'shoebuyer.html',{'cart':cart,'cart_items':cart_items,'image1':image1,
        'image0':image0})
     
               

def kidsbuyer(request):
    cart=Cart.objects.all()
    cart_items=KidsItems.objects.filter() 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
       
     
    return render(request,'kidsbuyer.html',{'cart':cart,'cart_items':cart_items,'image1':image1,
        'image0':image0})
     

def watchbuyer(request):
    cart=Cart.objects.all()
    cart_items=WatchItems.objects.filter() 
    image1 = get_object_or_404(paypage, Name='shop')
    image0 = get_object_or_404(paypage, Name='profile')  
       
     
    return render(request,'watchbuyer.html',{'cart':cart,'cart_items':cart_items,'image1':image1,'image0':image0})
     

def Fashionseller(request):
   
   qs=Fashionpages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')     
     
   return render(request,'Fashionseller.html',{'qs':qs,'image1':image1,
        'image0':image0})
     


def Fashionseller(request):
   
   qs=Fashionpages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'Fashionseller.html',{'qs':qs,'image1':image1,
        'image0':image0})
     


def Industryseller(request):
   
   qs=Industrialproductspages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'industryseller.html',{'qs':qs,'image1':image1,
        'image0':image0})
     

def Healthseller(request):
   
   qs=HealthProductspages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'healthseller.html',{'qs':qs,'image1':image1,
        'image0':image0})
     

def Homeseller(request):
   
   qs=HomeDecorpages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'homeseller.html',{'qs':qs,'image1':image1,
        'image0':image0})
     

def Sportsseller(request):
   
   qs=Sportspages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'sportseller.html',{'qs':qs,'image1':image1,
        'image0':image0})
     

def Shoeseller(request):
   
   qs=Shoespages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'shoeseller.html',{'qs':qs,'image1':image1,'image0':image0})
     

def Entertainmentseller(request):
   
   qs=Entertainmentpages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'entertainmentseller.html',{'qs':qs,'image1':image1,
        'image0':image0})
     

def Luggageseller(request):
   
   qs=LuggageBagspages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'luggageseller.html',{'qs':qs,'image1':image1,
        'image0':image0})
     

def Kidsseller(request):
   
   qs=KidsToyspages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'kidsseller.html',{'qs':qs,'image1':image1,
        'image0':image0})
     

def Watchseller(request):
   
   qs=WatchJewelrypages.objects.all() 
   image1 = get_object_or_404(paypage, Name='shop')
   image0 = get_object_or_404(paypage, Name='profile')   
     
   return render(request,'watchseller.html',{'qs':qs,'image1':image1,
        'image0':image0})


def deletefashion(request, id):
    qs=get_object_or_404(CartAdmin, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html')



     
def deletefashionsells(request, id):
    qs=get_object_or_404(Fashionpages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html')
def deleteindustrysells(request, id):
    qs=get_object_or_404(Industrialproductspages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html')


def deletehealthsells(request, id):
    qs=get_object_or_404(HealthProductspages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html')
def deletehomesells(request, id):
    qs=get_object_or_404(HomeDecorpages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html')

def deletesportsells(request, id):
    qs=get_object_or_404(Sportspages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html')
def deleteluggagesells(request, id):
    qs=get_object_or_404(LuggageBagspages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html') 


def deleteshoessells(request, id):
    qs=get_object_or_404(Shoespages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html')
def deleteentertainmentsells(request, id):
    qs=get_object_or_404(Entertainmentpages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html') 


def deletekidssells(request, id):
    qs=get_object_or_404(KidsToyspages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html')
def deletewatchsells(request, id):
    qs=get_object_or_404(WatchJewelrypages, id=id)
    
    if request.method=='POST':
      qs.delete()
      return redirect('Adminhomepage')
    
     
    return render(request,'delete.html') 


 
def buyersite(request):
    if request.method=='GET':
     image9 = get_object_or_404(paypage, Name='fashion')
     image10 = get_object_or_404(paypage, Name='industry')
     image11 = get_object_or_404(paypage, Name='health')
     image12 = get_object_or_404(paypage, Name='home')
     image13 = get_object_or_404(paypage, Name='sports')
     image14 = get_object_or_404(paypage, Name='shoes')
     image15 = get_object_or_404(paypage, Name='entertainment')
     image16 = get_object_or_404(paypage, Name='luggage')
     image17 = get_object_or_404(paypage, Name='watch')
     image18 = get_object_or_404(paypage, Name='kids')
     image18 = get_object_or_404(paypage, Name='kids')
     image1 = get_object_or_404(paypage, Name='shop')
     image0 = get_object_or_404(paypage, Name='profile')  
     context={
       
        'image1':image1,
        'image0':image0,
   
         'image9': image9,
         'image10': image10,
         'image11': image11,
         'image12': image12,
         'image13': image13,
         'image14': image14,
         'image15': image15,
         'image16': image16,
         'image17': image17,
         'image18': image18,
        
    }
     

    return render(request,'buyersite.html',context)  
        
   
def sellersite(request):
    if request.method=='GET':
     image9 = get_object_or_404(paypage, Name='fashion')
     image10 = get_object_or_404(paypage, Name='industry')
     image11 = get_object_or_404(paypage, Name='health')
     image12 = get_object_or_404(paypage, Name='home')
     image13 = get_object_or_404(paypage, Name='sports')
     image14 = get_object_or_404(paypage, Name='shoes')
     image15 = get_object_or_404(paypage, Name='entertainment')
     image16 = get_object_or_404(paypage, Name='luggage')
     image17 = get_object_or_404(paypage, Name='watch')
     image18 = get_object_or_404(paypage, Name='kids')
     image1 = get_object_or_404(paypage, Name='shop')
     image0 = get_object_or_404(paypage, Name='profile')  
     context={
       
        'image1':image1,
        'image0':image0,
   
         'image9': image9,
         'image10': image10,
         'image11': image11,
         'image12': image12,
         'image13': image13,
         'image14': image14,
         'image15': image15,
         'image16': image16,
         'image17': image17,
         'image18': image18,
        
    }
     

    return render(request,'sellersite.html',context)  


def profile(request,p_id):
    if request.method=='GET':
       pr=get_object_or_404(User,id=p_id)
    
       context={
        'pr':pr
        
    }
    return render(request,'profile.html',context)
    
def fashionbrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=Fashionpages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'fashionbrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,})
    
    
def industrybrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=Industrialproductspages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'industrybrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,})

def healthbrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=HealthProductspages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'healthbrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,})        


def Homebrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=HomeDecorpages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'homebrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,})


def sportsbrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=Sportspages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'sportsbrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,})


def entertainmentbrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=Entertainmentpages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'entertainmentbrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,})


def shoesbrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=Shoespages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'shoesbrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,})


def luggagebrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=LuggageBagspages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'luggagebrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,}) 


def watchbrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=WatchJewelrypages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'watchbrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,})


def kidsbrand(request):
    if request.method=='POST':
        searched = request.POST['searched']
        
                                                                                                                                                                                                                                                                                                                 
        fashion=KidsToyspages.objects.filter(Brand__icontains=searched)
        image1 = get_object_or_404(paypage, Name='shop')
        image0 = get_object_or_404(paypage, Name='profile')  
    
       
       
      
    return render(request,'kidsbrand.html',{'searched':searched,'fashion':fashion, 'image1':image1,
        'image0':image0,})
                               
                          
def Cartdetails(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       
       Cart=Cartdetail.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image)
       Cart.save()
       return redirect('Cartdetailed')
   
    else:
     return render(request,'productdetail.html')


def Cartdetailed(request):
 
    if request.method=='GET':
      sel1=Cartdetail.objects.last()
      qs=Fashionpages.objects.all()
      sal4 = qs[2] if qs.count() > 2 else None 
      qs=Entertainmentpages.objects.all()
      sal5 = qs[2] if qs.count() > 2 else None 
      qs=Sportspages.objects.all()
      sal6 = qs[2] if qs.count() > 2 else None 
      qs=HomeDecorpages.objects.all()
      sal7 = qs[2] if qs.count() > 2 else None 
      qs=HealthProductspages.objects.all()
      sal8 = qs[2] if qs.count() > 2 else None 
      qs=Industrialproductspages.objects.all()
      sal9 = qs[2] if qs.count() > 2 else None 
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
      context={
       
        'sel1':sel1,
        'sal4':sal4,
        'sal5':sal5,
        'sal6':sal6,
        'sal7':sal7,
        'sal8':sal8,
        'sal9':sal9,             
        'image1':image1,
        'image0':image0
    }   
    
    return render(request,'Cartdetail.html',context)

def delivery(request):
    if request.method=='GET':
      
      sel1=Cartdetail.objects.last()
      sel=Buyerform.objects.last()
      image1 = get_object_or_404(paypage, Name='shop')
      image0 = get_object_or_404(paypage, Name='profile')  
    context={
       
        
        'image1':image1,
        'image0':image0,
    
        'sel1':sel1,
        'sel':sel,
    }  
    return render(request,'deliver.html',context)


def Cartdetails(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       
       Cart=Cartdetail.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image)
       Cart.save()
       return redirect('Cartdetailed')
   
    else:
     return render(request,'enterdetail.html')
 
def Cartdetails(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       
       Cart=Cartdetail.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image)
       Cart.save()
       return redirect('Cartdetailed')
   
    else:
     return render(request,'Healthdetail.html')
 
 
def Cartdetails(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       
       Cart=Cartdetail.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image)
       Cart.save()
       return redirect('Cartdetailed')
   
    else:
     return render(request,'Homedetail.html')
 
 
def Cartdetails(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       
       Cart=Cartdetail.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image)
       Cart.save()
       return redirect('Cartdetailed')
   
    else:
     return render(request,'industrydetail.html')
 
 
def Cartdetails(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       
       Cart=Cartdetail.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image)
       Cart.save()
       return redirect('Cartdetailed')
   
    else:
     return render(request,'jeweldetail.html')
 
def Cartdetails(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       
       Cart=Cartdetail.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image)
       Cart.save()
       return redirect('Cartdetailed')
   
    else:
     return render(request,'Kidsdetail.html')
 
def Cartdetails(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       
       Cart=Cartdetail.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image)
       Cart.save()
       return redirect('Cartdetailed')
   
    else:
     return render(request,'luggagedetail.html')
 
def Cartdetails(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       
       Cart=Cartdetail.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image)
       Cart.save()
       return redirect('Cartdetailed')
   
    else:
     return render(request,'shoedetail.html')
 
def CartAdminsite(request):
    if request.method=='POST':
       Name = request.POST['Name'] 
       Brand = request.POST['Brand']
       Status = request.POST['Status']
       Price = request.POST['Price'] 
       quantity = request.POST['quantity'] 
       Image= request.POST['Image'] 
       Region = request.POST['Region'] 
       District = request.POST['District']
       Ward = request.POST['Ward']
       Phone = request.POST['Phone'] 
       Contact_name=request.POST['Contact_name']
       First_name = request.POST['First_name'] 
       last_name= request.POST['last_name'] 
       House_no = request.POST['House_no'] 
       Email= request.POST['Email'] 
       
       Cart=CartAdmin.objects.create(Name=Name,Brand=Brand,Status=Status,Price=Price,quantity=quantity,Image=Image,Region=Region,District=District,Ward=Ward,Phone=Phone,Contact_name=Contact_name,First_name=First_name,last_name=last_name,House_no=House_no,Email=Email)
       Cart.save()
       return redirect('networkform')
   
    else:
     return render(request,'deliver.html') 
 

 
 
def CartAdminshow(request):
    if request.method=='GET':
      
      sel1=CartAdmin.objects.all().order_by('-id')
    context={
       'sel1':sel1
       
    }  
    return render(request,'show.html',context)

def userdetail(request):
    if request.method=='GET':
        user=User.objects.all().order_by('-id')
    return render(request,'user.html',{'user':user})