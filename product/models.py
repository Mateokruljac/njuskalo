from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model): 
    title = models.CharField(max_length=50,blank = False,null = False)
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length = 100)
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Status(models.Model):
    status = models.CharField(max_length = 100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status
    
class Product(models.Model):
    name = models.CharField(max_length = 100,blank = False,null = False)
    about = models.TextField()
    tag = models.ForeignKey(Tag,on_delete=models.SET_NULL, null = True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null = False)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status,on_delete=models.SET_NULL, null = True)
    likes = models.ManyToManyField(User, null = True, blank = True, related_name="likes")
    image = models.ImageField(blank = True, upload_to="images/", null = True)
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    
    @property
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    title = models.CharField(max_length=100,blank = False,null = False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null = False, blank = False)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,on_delete = models.CASCADE, null = False, blank = False)

    def __str__(self):
        return self.title

    
    
    