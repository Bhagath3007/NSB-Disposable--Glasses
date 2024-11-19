from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'rating', 'reviews_count', 'is_promotion', 'owner')  # List of fields to show in admin
    search_fields = ('title', 'description')  # Enable search by title or description
    list_filter = ('is_promotion',)  # Enable filtering by promotion status
    ordering = ('-price',)  # Order by price in descending order