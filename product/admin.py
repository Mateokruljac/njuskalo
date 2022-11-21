from django.contrib import admin
from .models import Comment, Product, Status, Category, Tag
# Register your models here.
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Tag)