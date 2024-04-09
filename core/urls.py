from django.urls import path
from core.views import  product_detail_view,product_list_view,category_product_list_view,category_list_view,index

app_name = "core"

urlpatterns = [
    #HOME PAGE
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"), 
    
    
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list_view, name="category-product-list"),
    ]

    
    
    
    
    #Category
    
    

