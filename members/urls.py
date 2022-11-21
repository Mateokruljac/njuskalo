from django.urls  import path
from . import views 
urlpatterns = [
    path("register/", views.register_user, name = "register_user"),
    path("login/", views.login_user,name = "login_user"),
    path("logout/",views.logout_user,name = "logout_user"),
    
    path("update-cart",views.update_item,name = "update_cart"),
    path("process_order",views.process_order,name = "process_order")
    
]
