from django.urls import path 
from . import views 
urlpatterns = [
    path("",views.store, name = "store"),
    path("cart",views.cart,name = "cart"),
    path("checkout",views.checkout, name = "checkout"),
    
    #Product CRUD
    path("create-product",views.create_product,name = "create_product"),
    path("detail-product/<product_id>",views.detail_product, name = "detail_product"),
    path("update-product/<product_id>", views.update_product, name = "update_product"),
    path("delete-product/<product_id>",views.delete_product, name = "delete_product"),
    
    #Tag CRUD
    path("tag-list",views.tag_list,name = "tag_list"),
    path("create-tag",views.create_tag, name = "create_tag"),
    path("update-tag/<tag_id>",views.update_tag, name = "update_tag"),
    path("delete-tag/<tag_id>",views.delete_tag, name = "delete_tag"),
    
    #Tag CRUD
    path("category-list",views.category_list,name = "category_list"),
    path("create-category",views.create_category, name = "create_category"),
    path("update-category/<category_id>",views.update_category, name = "update_category"),
    path("delete-category/<category_id>",views.delete_category, name = "delete_category"),
   
   
    #Comment CRUD
    path("comment-list/<product_id>",views.comment_list,name = "comment_list"),
    path("create-comment/<product_id>",views.create_comment, name = "create_comment"),
    path("delete-comment/<product_id>/<comment_id>",views.delete_comment, name = "delete_comment"),
    
    path("searched",views.search, name  = "search")
]
