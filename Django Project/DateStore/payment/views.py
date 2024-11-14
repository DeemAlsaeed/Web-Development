from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.forms import ShippingForm,PaymentForm
from payment.models import ShippingAdress
from django.contrib import messages



def payment_success(request):
    return render(request,'payment/payment_success.html')

def checkout(request):
    cart=Cart(request)
    cart_roducts=cart.get_products
    quantities=cart.get_qts
    total =cart.sum()
    
    if request.user.is_authenticated:
        shipping_user=ShippingAdress.objects.get(user__id=request.user.id)

        shipping_form=ShippingForm(request.POST or None, instance=shipping_user)

        return render(request,'payment/checkout.html',{"cart_roducts":cart_roducts,"quantities":quantities,'total':total,'shipping_form':shipping_form})
    else:
        shipping_form=ShippingForm(request.POST or None )
        return render(request,'payment/checkout.html',{"cart_roducts":cart_roducts,"quantities":quantities,'total':total,'shipping_form':shipping_form})

    return render(request,'payment/checkout.html')


def billing_info(request):
   if request.POST:
        cart=Cart(request)
        cart_roducts=cart.get_products
        quantities=cart.get_qts
        total =cart.sum()

        if request.user.is_authenticated:
            billing_form=PaymentForm()
            return render(request,'payment/billing_info.html',{"cart_roducts":cart_roducts,"quantities":quantities,'total':total,'shipping_info':request.POST,"billing_form":billing_form})
        else:
            return render(request,'payment/billing_info.html',{"cart_roducts":cart_roducts,"quantities":quantities,'total':total,'shipping_info':request.POST,"billing_form":billing_form})

    

        shipping_form=request.POST
        return render(request,'payment/billing_info.html',{"cart_roducts":cart_roducts,"quantities":quantities,'total':total,'shipping_form':shipping_form})
   else:
      messages.success(request , "Access denied")
      return redirect('frontpage')

