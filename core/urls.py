from django.urls import path
from core.views import  cart_view,add_to_cart,search_view,product_detail_view,product_list_view,category_product_list_view,category_list_view,index

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
    
    ]

