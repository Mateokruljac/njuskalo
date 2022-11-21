from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from product.models import Product, Tag, Comment, Category
from django.contrib.auth.models import User 
from .serializers import ProductSerializer, Comment, CategorySerializer, TagSerializer

# Create your views here.


##############################################################                         CRUD API FOR PRODUCTS                      #############################################################

@api_view(["GET","POST"])
def list_or_create_product(request,format = None):
    """
    List all product order by date_added or create a one .
    For owner forward owner.id
    """
    if request.method == "GET":
        products = Product.objects.all().order_by("date_added")
        serializer = ProductSerializer(products, many = True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = ProductSerializer(data = request.data)
        owner = request.data.get("owner")
        user = User.objects.get(id = owner)
        if not User.objects.filter(id = owner).exists() or user.username == "GuestUser":
           return Response(data = {"msg":"This owner does not exists in database or owner is GuestUser!"},status = status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception = True):
           serializer.save()
           return Response(data = serializer.data, status = status.HTTP_201_CREATED)
        else:
           return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def detail_product_api(request,product_id:int,format = None):
    """ 
    Get product by id, update or delete
    """
    try: 
        product = Product.objects.get(id = product_id)
    except: 
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    if request.method == "GET":
        serializer = ProductSerializer(instance = product, many = False)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    if request.method == "PUT":
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid(raise_exception=True):
            #image file does not work 
            serializer.save()
            return Response(data = serializer.data, status = status.HTTP_200_OK)
        else:
           return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        product.delete()
        return Response(data = {"msg":"Successfully deleted!"},status = status.HTTP_204_NO_CONTENT)
       

##############################################################                         CRUD API FOR CATEGORY                      #############################################################

@api_view(["GET","POST"])
def list_or_create_category(request,format = None):
    """
    List all categories order by date_added or create a one .
    For owner forward owner.id
    """
    if request.method == "GET":
        category = Category.objects.all().order_by("date_added")
        serializer = CategorySerializer(category, many = True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    if request.method == "POST":
       serializer = CategorySerializer(data = request.data)
       if serializer.is_valid():
           serializer.save()
           return Response (data = serializer.data, status = status.HTTP_201_CREATED)
       else: 
           return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def detail_category_api(request, category_id, format = None):
    """ 
    Get category by id, update or delete
    """
    try:
        category = Category.objects.get(id = category_id)
    except:
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    if request.method == "GET":
        serializer = CategorySerializer(category, many = False)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    if request.method == "PUT":
        serializer = CategorySerializer(category, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = status.HTTP_200_OK)
        else: 
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE": 
        category.delete()
        return Response (data = {"msg":"Successfully deleted!"}, status = status.HTTP_204_NO_CONTENT)


##############################################################                         CRUD API FOR TAG                      #############################################################

@api_view(["GET","POST"])
def list_or_create_tag(request,format = None):
    """
    List all tags order by date_added or create a one .
    For owner forward owner.id
    """
    if request.method == "GET":
        tags = Tag.objects.all().order_by("date_added")
        serializer = TagSerializer(tags, many = True)
        return Response(data = serializer.data,status = status.HTTP_200_OK)
    
    if request.method == "POST": 
        serializer = TagSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data,status = status.HTTP_201_CREATED)

@api_view(["GET","PUT","DELETE"])
def detail_tag_api(request, tag_id, format = None):
    """ 
    Get tag by id, update or delete
    """
    try:
        tag = Tag.objects.get(id = tag_id)
        print("Tag",tag)
    except:
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    if request.method == "GET":
        serializer = TagSerializer(tag, many = False)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    if request.method == "PUT":
        serializer = TagSerializer(tag, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = status.HTTP_200_OK)
        else: 
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE": 
        tag.delete()
        return Response (data = {"msg":"Successfully deleted!"}, status = status.HTTP_204_NO_CONTENT)
    