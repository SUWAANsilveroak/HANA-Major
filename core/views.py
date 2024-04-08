from django.shortcuts import render
from django.http import HttpResponse
from core.models import Category, Product, ProductImages, CartOrder, CartOrderItem, ProductReview,WishList,Address,Vendor

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    
    return render(request, 'core/index.html',context)
    