from core.models import Category, Product, ProductImages, CartOrder, CartOrderItem, ProductReview,WishList,Address,Vendor

def default(request):
    categories = Category.objects.all()
    return{
        "categories":categories,
    }