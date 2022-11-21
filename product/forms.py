from django import forms 
from .models import Product,Tag, Category, Comment
#Create forms in here

class ProductForm(forms.ModelForm):
    """ 
     This form serves for create a new product or update. Use product model as model, and following fields as fields: 
     model = Product
     fields = ["name","about","tag","category","status","image","price"]. 
     *********************************************************************
       The fields owner, date_added and likes cannot be entered by the user,
       beacause owner is authenticated user, date_added is automaticly created and likes should be added by others.
     It is not sense that owner can added likes by others.
    """
    class Meta: 
        model = Product 
        fields = ["name","about","tag","category","status","image","price"]
        widgets = {
            "name" : forms.TextInput(attrs = {"placeholder" : "Name...","class":"form-control"}),
            "about" : forms.Textarea(attrs = {"placeholder" : "Write...","class":"form-control"}),
            "tag" : forms.Select(attrs = {"placeholder" : "Tag...","class":"form-control"}),
            "category" : forms.Select(attrs = {"placeholder" : "Category...","class":"form-control"}),
            "status" : forms.Select(attrs = {"placeholder" : "Status...","class":"form-control"}),
            "price" : forms.NumberInput(attrs = {"placeholder" : "Price...","class":"form-control"}),
        }

class TagForm(forms.ModelForm):
  """ 
  This form serves to create a tag  or update existing! Use tag model as model and following fields
  model: Tag
  fields = ["title"]
  """
  class Meta: 
    model = Tag
    fields = ["title"]
    widgets = {
          "title" : forms.TextInput(attrs = {"placeholder" : "Title","class":"form-control"}),
    }

class CategoryForm(forms.ModelForm):
  """ 
  This form serves to create a category or update existing! Use category model as model and following fields
  model: Category
  fields = ["title"]
  """
  class Meta: 
    model = Category
    fields = ["title"]
    widgets = {
          "title" : forms.TextInput(attrs = {"placeholder" : "Title","class":"form-control"}),
    }



class CommentForm(forms.ModelForm):
  """ 
  This form serves to create a comment!  Use comment model as model and following fields.
  Fields: owner and date_added are automaticly added by server.
  model: Category
  fields = ["title","body"]
  """
  class Meta: 
    model = Comment
    fields = ["title","body"]
    widgets = {
          "title" : forms.TextInput(attrs = {"placeholder" : "Title","class":"form-control"}),
          "body" : forms.Textarea(attrs = {"placeholder" : "Write...","class":"form-control"}),
    }