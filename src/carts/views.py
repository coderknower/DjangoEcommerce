from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart_create(user=None):
    cart_obj=Cart.objects.create(user=None)
    print("New Cart created")

    return cart_obj


def cart_home(request):
    del request.session['cart_id']
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:# and isinstance(cart_id, int):
        cart_obj= Cart.objects.create(user=None)
        request.session['cart_id']=cart_obj.id

    else:
        qs=Cart.objects.filter(id=cart_id)
        if qs.count()==1:
            print('Card Id Exists')
            cart_obj=qs.first()
        else:
            cart_obj=cart_create()

        print(cart_id)
        cart_obj= Cart.objects.get(id=cart_id)
    #print(request.session)
    #key=request.session.session_key#
    #print(key)
    #request.session.set_expiry(10)
    return render(request,"carts/home.html",{})