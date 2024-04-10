# This Python file defines models for our e-commerce platform including
# categories, products, cart orders, product reviews, wishlists, and addresses.

from django.db import models
from shortuuid.django_fields import ShortUUIDField 
from django.utils.html import mark_safe
from userauths.models import User


# Create your models here.

STATUS_CHOICE = (
    ("Process","Processing"),
    ("shipped","Shipped"),
    ("delivered","Delivered"),
)

STATUS = (
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("in_review","In Review"),
    ("published","Published"),
)

RATING = (
    ( 1,"★☆☆☆☆"),
    ( 2,"★★☆☆☆"),
    ( 3,"★★★☆☆"),
    ( 4,"★★★★☆"),
    ( 5,"★★★★★"),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="cat", alphabet="abcdefgh12345")
    title =models.CharField(max_length=100, default="Item")
    image = models.ImageField(upload_to="Category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"
        
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))
    
    def __str__(self):
        return self.title
    
class Tags(models.Model):
    pass

class Vendor(models.Model):
    pass

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="prd", alphabet="abcdefgh12345")
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    
    title =models.CharField(max_length=100, default="Fresh")
    image = models.ImageField(upload_to="Category", default="product.jpg")
    description = models.TextField(null=True, blank=True, default="This is the product")
    
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="2.99")
    
    specifications = models.TextField(null=True, blank=True)
    #tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    
    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    
    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")
    
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Products"
        
    def product_image(self): #facing some issue here 
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        percentage_off = (1 - (self.price / self.old_price)) * 100
        return round(percentage_off)


class ProductImages(models.Model):
    image = models.ImageField(upload_to="product-images", default="product.jpg") 
    product = models.ForeignKey(Product, related_name="p_images", on_delete=models.SET_NULL, null=True)
    date =models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Images"


###################################### cart order item #####################################################
###################################### cart order item #####################################################
###################################### cart order item #####################################################
###################################### cart order item #####################################################
        
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="Processing")

    class Meta:
        verbose_name_plural = "Cart Order"

class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")
    
    class Meta:
        verbose_name_plural = "Cart Order Items"
        
    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50"/>' % (self.image))
    

################################ Product Review, wishlist, Address #####################################################
################################ Product Review, wishlist, Address #####################################################
################################ Product Review, wishlist, Address #####################################################
################################ Product Review, wishlist, Address #####################################################

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Reviews"
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    
class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Wish List"
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Address"

