from django.shortcuts import render,get_object_or_404
from .cart import Cart
from core.models import Product 
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request,):
    cart=Cart(request)
    cart_roducts=cart.get_products
    quantities=cart.get_qts
    total =cart.sum()
    
    return render(request,'cart/cart_summary.html',{"cart_roducts":cart_roducts,"quantities":quantities,'total':total})

def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        product_qt=int(request.POST.get('product_qt'))

        product=get_object_or_404(Product,id=product_id)

        cart.add(product=product,quantity=product_qt)
        
        cart_quantity=cart.__len__()
        #response=JsonResponse({'Product Name':product.name})
        response=JsonResponse({'qt':cart_quantity})
        messages.success(request,("successfuly add to cart"))

        
       
        return response

def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))

        cart.delete(product=product_id)

        respone=JsonResponse({'product':product_id})
        messages.success(request,("successfuly deleted from cart"))

        return respone
        



def cart_update(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        product_qt=int(request.POST.get('product_qt'))

        cart.update(product=product_id,quantity=product_qt)

        response=JsonResponse({'qt':product_qt})
        messages.success(request,("Your cart has been updated"))

        return response
    
        #return redirect('cart/cart_summary.html')


    
''' 

here i attemp to link the javascirpt of the updateshop cart here 'add-to-cart',
the issues:
1- the {% static %} wont be work in javascripts so the scripts are different than the embedd within the html pages{products,categories}
and the button too here after modifieded data-cart-url="{% url 'cart_add' %}">Add to Cart</button>
2-after that is solved ,another issue is apeared .403 a forbidden ,relatied to csrf so here is the code to solve it 
'''
'''
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def cart_add(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        cart_quantity = len(cart)
        return JsonResponse({'qt': cart_quantity})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
        '''
'''
now another error , 500 intenral server i did not solve it i think this related to authintication stuff so butter to let the scripts within the pages for now  

here a suggested code slution :
from django.contrib.auth.decorators import login_required

@login_required
def cart_add(request):
    # View logic remains the same


'''