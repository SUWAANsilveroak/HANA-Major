from django.contrib import admin
from core.models import Category, Product, ProductImages, CartOrder, CartOrderItem, ProductReview,WishList,Address,Vendor
# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title','product_image', 'price', 'featured', 'product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']
    

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status','order_date','product_status']
    
class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'qty', 'invoice_no','item','image','price','total']
    
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']
    
class WishListAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','date']
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address','status']
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItem, CartOrderItemAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Address, AddressAdmin)
#admin.site.register(Vendor, VendorAdmin) we are planning for vendor