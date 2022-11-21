from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Product, Tag, Category, Comment
from django.contrib.auth.models import User
from .forms import ProductForm, TagForm, CategoryForm, CommentForm
from .utils import cart_total_info

# Create your views here.

def store (request):
    #list product
    products = Product.objects.all().order_by("date_added")
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    items = data["items"]    
    order = data["order"]    
    context = {"items":items,"order":order,"products":products,"cart_total":cart_total}
    return render (request,"core/store.html",context)

def cart (request):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    items = data["items"]    
    order = data["order"]   
        
    context = {"items":items,"order":order,"cart_total":cart_total}
    return render(request,"core/cart.html",context)

def checkout (request):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    items = data["items"]    
    order = data["order"]   
    context = {"items":items,"order":order,"cart_total":cart_total}
    return render(request,"core/checkout.html", context)


##############################################################                         CRUD FOR PRODUCTS                      #############################################################

def create_product(request):
    submitted = False
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit = False)
            form.owner = request.user
            form.save()
            return HttpResponseRedirect("create-product?submitted=True")
        else:
            messages.warning(request,"Somethig went wrong, please try again!")
            return render (request,"product/create.html",{"form":form,"cart_total":cart_total})
    else:
        #GET method
        form = ProductForm()
        if "submitted" in request.GET:
            submitted = True
        
        return  render (request,"product/create.html",{"form":form,"submitted":submitted,"cart_total":cart_total})

def update_product(request,product_id:int):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    updated = False
    if request.method == "POST":
        product = Product.objects.get(pk = product_id)
        form = ProductForm(request.POST or None,instance = product) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"{product_id}?updated=True")
        else:
            messages.info("Something went wrong!")
            return render (request,"product/update.html",{"product":product,"form":form,"updated":updated,"cart_total":cart_total})
        
    else:
        #GET method
        product = Product.objects.get(id = product_id)
        form = ProductForm(instance = product) 
        if "updated" in request.GET:
            updated = True    
        return render (request,"product/update.html",{"product":product,"form":form,"updated":updated,"cart_total":cart_total})
    
def delete_product(request,product_id:int):
    try:
        product = Product.objects.get(pk = product_id)
        product.delete()
    except product.DoesNotExist:
        pass
    return redirect("store")
        

def detail_product(request,product_id:int):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    product = Product.objects.get(id = product_id)
    
    #list comments related to this product
    try:
       comment = Comment.objects.filter(product = product).order_by("date_added")
       comment = comment[0]
    except:
      comment = []
    return render(request,"product/detail.html",{"product":product,"cart_total":cart_total,"comment":comment})


##############################################################                         CRUD FOR  TAGS                      #############################################################

def tag_list(request):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    tags = Tag.objects.all()
    return render (request,"tags/list.html",{"tags":tags,"cart_total":cart_total})

def create_tag(request):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    submitted = False
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.owner = request.user
            form.save()
            return HttpResponseRedirect("create-tag?submitted=True")
        else:
            messages.warning("Something went wrong!")
            return render (request,"tags/create.html",{"form":form,"submitted":submitted,"cart_total":cart_total})
    else:
        #GET method
        form = TagForm()
        if "submitted" in request.GET:
            submitted = True
        return render (request,"tags/create.html",{"form":form,"submitted":submitted,"cart_total":cart_total})

def update_tag(request,tag_id:int):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    updated = False
    if request.method == "POST":
        tag = Tag.objects.get(id = tag_id)
        form = TagForm(request.POST or None,instance = tag)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"{tag_id}?updated=True")
        else:
            messages.warning("Something went wrong!")
            return render (request,"tags/update.html",{"form":form,"cart_total":cart_total})
    else:
        #GET method 
        tag = Tag.objects.get(id = tag_id)
        form = TagForm(instance = tag)
        if "updated" in request.GET:
            updated = True
        return render (request,"tags/update.html",{"updated":updated,"form":form,"tag":tag,"cart_total":cart_total})

def delete_tag(request,tag_id:int):
    try:
        tag = Tag.objects.get(id = tag_id)
        tag.delete()

        return  redirect("tag_list")
    except:
        pass
        
   
   
   
    
##############################################################                         CRUD FOR  CATEGORY                      #############################################################
def category_list(request):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    categories = Category.objects.all()
    return render (request,"category/list.html",{"categories":categories,"cart_total":cart_total})

def create_category(request):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    submitted = False
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.owner = request.user
            form.save()
            return HttpResponseRedirect("create-category?submitted=True")
        else:
            messages.warning("Something went wrong!")
            return render (request,"category/create.html",{"form":form,"submitted":submitted,"cart_total":cart_total})
    else:
        #GET method
        form = CategoryForm()
        if "submitted" in request.GET:
            submitted = True
        return render (request,"category/create.html",{"form":form,"submitted":submitted,"cart_total":cart_total})

def update_category(request,category_id:int):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    updated = False
    if request.method == "POST":
        category = Category.objects.get(id = category_id)
        form = CategoryForm(request.POST or None,instance = category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"{category_id}?updated=True")
        else:
            messages.warning("Something went wrong!")
            return render (request,"tags/update.html",{"form":form,"cart_total":cart_total})
    else:
        #GET method 
        category = Category.objects.get(id = category_id)
        form = CategoryForm(instance = category)
        if "updated" in request.GET:
            updated = True
        return render (request,"category/update.html",{"updated":updated,"form":form,"category":category,"cart_total":cart_total})

def delete_category(request,category_id:int):
    
    try:
        category = Category.objects.get(id = category_id)
        category.delete()
        return  redirect("categpry_list")
    except:
        pass
        


def search (request):
    data = cart_total_info(request)
    cart_total = data["cart_total"]    
    searched = request.POST.get("search")
    products = Product.objects.filter(name__contains = searched.title()).order_by("date_added")
    return render (request,"core/store.html",{"products":products,"cart_total":cart_total})


##############################################################                         CRUD FOR COMMENTS                      #############################################################

def comment_list(request,product_id:int):
    """  
    comments are related to product, so we have to parse product_id 
    """
    product = Product.objects.get(id  = product_id)
    comments = Comment.objects.filter(product = product).order_by("date_added")
    return render (request, "comment/list.html",{"comments":comments,"product":product})

def create_comment(request,product_id:int):
    submitted = False 
    if request.method == "POST":
        product = Product.objects.get(id = product_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.product = product
            try:
                form.owner = request.user
            except:
                form.owner,created = User.objects.get_or_create(username = "Guest User")
            form.save()
            return HttpResponseRedirect("create-comment?submitted=True")
        else:
            messages.info(request,"Something went wrong!")
            return render (request,"comment/create.html",{"form":form})                        
    else:
        form = CommentForm()
        if "submitted" in request.GET: 
            submitted = True   
        return render (request,"comment/create.html",{"form":form,"submitted":submitted})


def delete_comment(request,product_id,comment_id:int):
    try:
       comment = Comment.objects.get(id = comment_id)
       comment.delete()
    except: 
        pass
    
    return HttpResponseRedirect(reverse("detail_product",args = [str(product_id)]))
    
