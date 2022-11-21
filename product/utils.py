from members.models import Order

def cart_total_info(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cart_total = order.total_items 
    else: 
        order = {"total_items" : 0, "total_price" : 0}
        items = []
        cart_total = 0
    context  = {"cart_total":cart_total,"order":order,"items":items}    
    return context  