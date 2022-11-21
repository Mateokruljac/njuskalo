from django.urls import path 
from . import views 
urlpatterns = [
    #product API
    path("product/list-or-create",views.list_or_create_product, name = "list_or_create_product"),
    path("product/detail/<product_id>",views.detail_product_api, name = "detail_product_api"),
    
    #category API
    path("category/list-or-create",views.list_or_create_category, name = "list_or_create_category"),
    path("category/detail/<category_id>",views.detail_category_api, name = "detail_category_api"),
 
    #tag API
    path("tag/list-or-create",views.list_or_create_tag, name = "list_or_create_tag"),
    path("tag/detail/<tag_id>",views.detail_tag_api, name = "detail_tag_api"),
]
