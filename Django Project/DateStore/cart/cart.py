
from core.models import Product,Profile
class Cart():
    def __init__(self,request):
        self.session=request.session

        self.request=request

        cart=self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key']={}
        
        self.cart=cart

    def db_add(self,product,quantity):
        product_id=str(product)
        product_qt=str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qt)
            #self.cart[product_id]={'price': str(product.price)}

        self.session.modified=True

        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            carty=str(self.cart)
            carty= carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))


    def add(self,product,quantity):
        product_id=str(product.id)
        product_qt=str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qt)
            #self.cart[product_id]={'price': str(product.price)}

        self.session.modified=True

        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            carty=str(self.cart)
            carty= carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))


    def __len__(self):
        return len(self.cart)
    

    def get_products(self):

        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)

        return products
    def get_qts(self):
        quantities=self.cart
        return quantities

    def sum(self):
        product_ides=self.cart.keys()
        products=Product.objects.filter(id__in=product_ides)
        quantitiies=self.cart
        total=0
        for key ,value in quantitiies.items():
            key=int(key)
            for p in products:
                if p.id == key:
                    total=total+(p.price*value)

        return total
        

        

        return sum

    def update(self,product,quantity):
        product_id=str(product)
        product_qt=int(quantity)

        thecart=self.cart
        thecart[product_id]=product_qt 

        self.session.modified=True

        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            carty=str(self.cart)
            carty= carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))
 

        thing=self.cart

        return thing
    
    def delete(self,product):
        product_id=str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified=True

        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            carty=str(self.cart)
            carty= carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))


        


        