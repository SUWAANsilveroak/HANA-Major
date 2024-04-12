from django.urls import path,include
from core.views import  checkout_view,payment_failed_view,payment_completed_view,cart_view,add_to_cart,search_view,product_detail_view,product_list_view,category_product_list_view,category_list_view,index

app_name = "core"

urlpatterns = [
    #HOME PAGE
    path("", index, name="index"),
    #product path
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"), 
    
    #category path
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),
    
    #searching path
    path("search/", search_view, name="search"),
    
    #cart path
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    
    #cart page url
    path("cart/", cart_view, name="cart"),
    
    #paypal
    path("paypal/", include('paypal.standard.ipn.urls')),
    
    path("checkout/", checkout_view, name="checkout"),
    
    
    #check out
    path("payment-failed/", payment_failed_view, name="payment-failed"),
    #payment success
    path("payment-completed/", payment_completed_view, name="payment-completed"),
    #payment failed
    path("payment-failed/", payment_failed_view, name="payment-failed"),
    
    
    
    
    
    ]

    
