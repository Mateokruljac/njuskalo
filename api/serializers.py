from rest_framework import serializers
from product.models import Category, Comment, Product, Tag
from django.contrib.auth.models import User

#create serializers in here 

class ProductSerializer(serializers.ModelSerializer):
    """  
    This class retruns django Product model and value in JSON format.
    For this serializer use Product model and following fields within 
    Meta class.
    **********************************
    Use this scheme 
    Do not put   and 'date_added' in fields, because is request.user
    and date_added is automaticly added after creating! 
    """
    class Meta:
        model = Product 
        fields = ["id","owner","name","about","tag","category","status","image","price"]
    
        

class CategorySerializer(serializers.ModelSerializer):
    """  
    This class retruns django Category model and value in JSON format.
    For this serializer use Category model and following fields within 
    Meta class.
    **********************************
    Use this scheme 
    Do not put   and 'date_added' in fields, because is request.user
    and date_added is automaticly added after creating! 
    """
    class Meta:
        model = Category 
        fields = ["id","title"]
        
class TagSerializer(serializers.ModelSerializer):
    """  
    This class retruns django Tag model and value in JSON format.
    For this serializer use Tag model and following fields within 
    Meta class.
    **********************************
    Use this scheme 
    Do not put   and 'date_added' in fields, because is request.user
    and date_added is automaticly added after creating! 
    """
    class Meta:
        model = Tag
        fields = ["id","title"]
        

class CommentSerializer(serializers.ModelSerializer):
    """  
    This class retruns django Comment model and value in JSON format.
    For this serializer use Comment model and following fields within 
    Meta class.
    **********************************
    Use this scheme 
    Do not put  ,'product' and 'date_added' in fields, because is request.user,
    product is the product where is comment and date_added is automaticly added after creating! 
    """
    class Meta:
        model = Comment
        fields = ["owner","name","body"]
        

