from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.http import JsonResponse
from core.models import Category, Product, ProductImages, CartOrder, CartOrderItem, ProductReview,WishList,Address

# Create your views here.
def index(request):
    products = Product.objects.filter(product_status="published", featured=True).order_by("-id")
    context = {
        "products":products
    }
    
    return render(request, 'core/index.html',context)

def category_list_view(request):
    categories = Category.objects.all()#.annotate(product_count=Count("product"))
    
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
    #product = Product.objects.get(pid=pid)
    product = get_object_or_404(Product, pid=pid)
    p_image = product.p_images.all()
    
    context = {
        "product":product,
        "p_image":p_image,
    }
    return render(request, 'core/product-detail.html',context)

def search_view(request):
    query = request.GET.get("q")
    
    products = Product.objects.filter(title__icontains=query).order_by("-date")
    
    context={
        "products":products,
        "query":query,
    }
    return render(request, 'core/search.html',context)


def add_to_cart(request):
    
   """
   Handles adding products to the cart session.

   Args:
       request (HttpRequest): The HTTP request with product details.

   Returns:
       JsonResponse: Updated cart data and total cart items.

   Expects the following GET parameters:
       - id (str): Product ID.
       - title (str): Product title.
       - qty (int): Product quantity.
       - price (str or float): Product price.

   Adds or updates the product in the 'cart_data_obj' session key.
   If the product exists, updates the quantity. Otherwise, adds the product.
   """
   cart_product = {}
   cart_product[str(request.GET['id'])] = {
       'title': request.GET['title'],
       'qty': int(request.GET['qty']),
       'price': request.GET['price'],
   }

   if 'cart_data_obj' in request.session:
       if str(request.GET['id']) in request.session['cart_data_obj']:
           cart_data = request.session['cart_data_obj']
           cart_data[str(request.GET['id'])]['qty'] = int(cart_data[str(request.GET['id'])]['qty']) + int(request.GET['qty'])
           request.session['cart_data_obj'] = cart_data
       else:
           cart_data = request.session['cart_data_obj']
           cart_data.update(cart_product)
           request.session['cart_data_obj'] = cart_data
   else:
       request.session['cart_data_obj'] = cart_product

   return JsonResponse({"data": request.session['cart_data_obj'], 'totalcartitem': len(request.session['cart_data_obj'])})


def cart_view(request):
    return render(request,"core/cart.html") 
    
    

