from django.shortcuts import render ,redirect
from .models import *
from .forms import * 
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
import json
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAdress


# Create your views here.
def frontpage(request):
    products=Product.objects.all()
    dates=imgaes.objects.all()
    return render(request, 'core/frontpage.html',{'products':products,'dates':dates})

def aboutPage(request):
    return render(request, 'core/aboutpage.html')

def yourDates(request):
    dateposts=imgaes.objects.all()
    return render(request, 'core/yourDates.html',{'dateposts':dateposts})

def img(request):
    if request.method == 'POST':
        form = DateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return redirect('yourDates')  # Redirect to the 'yourDates' URL
    else:
        form = DateForm()
    img = imgaes.objects.all()
    return redirect('yourDates')  # Redirect to the 'yourDates' URL

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            current_user=Profile.objects.get(user__id=request.user.id)
            saved_cart=current_user.old_cart
            if saved_cart:
                converted_cart=json.loads(saved_cart)
                cart=Cart(request)
                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value)
            messages.success(request, ("You have been logged in."))
            return redirect('frontpage')
        else:
             messages.success(request,("There was an error."))
             return redirect('login')
    else:
        return render(request,'core/login.html',{})

    return render(request, 'core/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out. See you later!"))
    return redirect('frontpage')

from django.db.models import Q
def products(request):
    if 'search' in request.GET:
        Mdate=Q(Q(name__icontains=date)| Q(description__icontains=date))
        products=Product.objects.filter(Mdate)
       
    else:
        products=Product.objects.all()
    return render(request, 'core/products.html',{'products':products})


def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form= UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request,current_user)
            messages.success(request,"Your information has been updated successfully.")
            return redirect('frontpage')
        return render(request,"core/updateProfile.html",{'user_form':user_form})
    else:
        messages.success(request, "Please log in first.")
        return redirect('frontpage')

    return render(request, 'core/updateProfile.html',{})


def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method == 'POST':
           form = ChangePasswordForm(current_user,request.POST)
           if form.is_valid():
               form.save()
               messages.success(request,"Your password has been changed.")
               login(request,current_user)
               return redirect('update_user')
           else:
               for error in list(form.errors.values()):
                   messages.error(request,error)
                   return redirect('login')
        else:
           form = ChangePasswordForm(current_user)
           return render(request,"core/update_password.html",{'form':form})
    else:
        messages.success(request,"Please log in first.")
        return redirect('frontpage')

def update_info(request):
    if request.user.is_authenticated:
        current_user=Profile.objects.get(user__id=request.user.id)
        shipping_user=ShippingAdress.objects.get(user__id=request.user.id)
        form= UserInfoForm(request.POST or None, instance=current_user)
        shipping_form=ShippingForm(request.POST or None, instance=shipping_user)

        
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            #login(request,current_user)
            messages.success(request,"Your information has been updated successfully.")
            return redirect('frontpage')
        return render(request,"core/update_info.html",{'form':form,'shipping_form':shipping_form})
    else:
        messages.success(request, "Please log in first.")
        return redirect('frontpage')

    
    
    
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Hi {user.username}, please fill your information")
                return redirect('update_info')
            else:
                messages.error(request, "Authentication failed. Please try again.")
                return redirect('register')
        else:
            messages.error(request, "Invalid form submission. Please try again.")
            return redirect('register')
    return render(request, 'core/register.html', {'form': form})

def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'core/product.html',{'product':product})

def categories(request,name):
    #replacing - by space of the name to hndling it 
    name =name.replace('-',' ')
    try:
        category=Category.objects.get(name=name)
        products=Product.objects.filter(category=category)
        return render(request,'core/category.html',{'products':products,'category':category})
 
    except:
        messages.success(request,("Sorry,we dont have this type."))
        return render(request,'core/frontpage.html',{})


    