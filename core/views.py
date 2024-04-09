from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from core.models import Category, Product, ProductImages, CartOrder, CartOrderItem, ProductReview,WishList,Address,Vendor

# Create your views here.
def index(request):
    products = Product.objects.filter(product_status="published", featured=True)
    context = {
        "products":products
    }
    
    return render(request, 'core/index.html',context)

def category_list_view(request):
    categories = Category.objects.all().annotate(product_count=Count("product"))
    
    context = {
        "categories":categories
    } 
    return render(request, 'core/category-list.html',context)

def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published",category=category)
    context = {
        "category":category,
        "products":products,
    }
    return render(request, 'core/category-product-list.html',context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")
    #product = get_object_or_404(Product, pid=pid)
    
    context = {
        "products":products
    }
    return render(request, 'core/product-list.html',context)
    

def product_detail_view(request,pid):
    product = Product.objects.get(pid=pid)
    #product = get_object_or_404(Product, pid=pid)
    
    p_image = product.p_image.all()
    context = {
        "product":product
    }
    return render(request, 'core/product-detail.html',context)

