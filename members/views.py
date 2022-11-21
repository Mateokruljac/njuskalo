from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from .models import Customer, Order, OrderItem, ShippingAddress
from product.models import Product
from product.utils import cart_total_info
import json
import datetime # for randomize transaction id 
# Create your views here.
def register_user(request):
    registered = False
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    if not request.user.is_authenticated:
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            buttonAgree = request.POST.get("checkbox")
            
            if password == confirm_password:
                if User.objects.filter(Q(email = email)|Q(username = username)).exists() == False:
                    if buttonAgree is not None:
                        user = User.objects.create_user(
                            first_name = first_name,
                            last_name = last_name,
                            username = username,
                            email = email,
                            password = password
                        )
                        user.save()
                        messages.info(request,"New user successfully created!")
                        return redirect("login")
                    else:
                        messages.info(request,"You must agree with all statements!")
                        return render (request,"register.html",{"cart_total":cart_total})
                else: 
                    messages.info(request,"User with that username or email already exists!")
                    return render (request,"register.html",{"cart_total":cart_total})
            else:
                messages.info(request,"Paswords not matching!")
                return render (request,"register.html",{"cart_total":cart_total})
        
        else:
            return render (request,"register.html",{"cart_total":cart_total})
    else:
        registered = True
        messages.info(request,"You are already registered!")
        return render (request,"register.html",{"cart_total":cart_total,"registered":registered})
    
def login_user(request):
    logged_in = False
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                try:
                    request.user.customer
                    return redirect("store")
                except:
                    create_user_customer(request)
            else:
                messages.info(request,"Invalid username or password! Try again!")       
                return render (request,"login.html",{"cart_total":cart_total})

        else:
            return render (request,"login.html",{"cart_total":cart_total})
    else:
        logged_in = True
        messages.info(request,"You are already logged in!")
        return render (request,"login.html",{"cart_total":cart_total,"logged_in":logged_in})
        
    
def logout_user(request):
    logout(request)
    return redirect("login")

def create_user_customer(request):
    if Customer.objects.filter(Q(user = request.user)|Q(email = request.user.email)|Q(username = request.user.username)).exists(): 
        return redirect("store")
    else:
        customer = Customer.objects.create(
            user = request.user,
            email = request.user.email,
            username = request.user.username)
        customer.save()
    return redirect("store")


def update_item(request):
    data = json.loads(request.body)
    product_id = data["productId"]
    action = data["action"]
    print("Productid:", product_id)
    print("Action",action)
    
    product = Product.objects.get(id = product_id)
    customer = request.user.customer
    order,created = Order.objects.get_or_create(customer = customer,complete = False)
    order_item,created = OrderItem.objects.get_or_create(order = order, product = product)
    print(order_item.quantity)
    if action == "add":
        order_item.quantity += 1
    if action == "remove":
        order_item.quantity -= 1
    
    order_item.save(
        
    )
    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse("Item was added!",safe = False)



def process_order(request):
    data = json.loads(request.body)
    transaction_id = datetime.datetime.now().timestamp() 
    if request.user.is_authenticated:
       customer = request.user.customer
       order, created = Order.objects.get_or_create(customer = customer, complete =  False)
       
       order.transaction_id = transaction_id
       order.complete = True
       order.save()
       shippping_address = ShippingAddress.objects.create(
           customer = customer,
           order = order,
           street_address = data["shipping_address"]["address"],
           city = data["shipping_address"]["city"],
           country = data["shipping_address"]["country"],
           zip_code = data["shipping_address"]["zipcode"]
           
       )
       shippping_address.save()
    else:
        pass
    
    return JsonResponse("Payment complete!",safe = False)