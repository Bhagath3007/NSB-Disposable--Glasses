# models.py
from django.db import models
from django.contrib.auth.models import User

# UserProfile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username  # Returns the username of the associated User

# Profile Model (additional user information)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', default='default.jpg')  # Default photo path

    def __str__(self):
        return self.user.username  # Returns the username of the associated User

# Product Model (for the products)
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    reviews_count = models.IntegerField()
    is_promotion = models.BooleanField(default=False)
    promotion_details = models.CharField(max_length=200, null=True, blank=True)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Default to user with ID 1
    
    class Meta:
        permissions = [
            ("can_add_product", "Can add product")
        ]

    def __str__(self):
        return self.title  # Returns the product title
# models.py
from django.db import models
from django.contrib.auth.models import User
from products.models import Product  # Assuming you have a Product model

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title} - {self.quantity}'

    def get_total_price(self):
        return self.product.price * self.quantity
# In your models.py (before running makemigrations)
from django.db import models

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Other fields...

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)  # Example default value

    def __str__(self):
        return f"{self.product.title} ({self.quantity})"
