from core.models import Category, Product, ProductImages, CartOrder, CartOrderItem, ProductReview,WishList,Address,Vendor

def default(request):
    categories = Category.objects.all()
    #address = Address.objects.get(user=request.user)
    return{
        "categories":categories,
        #"address":address, # use {{address.address}}
    }