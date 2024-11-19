from django.urls import path
from . import views
from .views import register, user_profile

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),  # Profile URL
    path('add-product/', views.add_product, name='add_product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='aboutus'),  
    path('cart/', views.view_cart, name='view_cart'),  # Add this line
        path('contact/', views.contact_view, name='contact'),
            path('home/', views.home1, name='homep'),  # New path for homep view

  path('search/', views.search, name='search'),  # Search functionality


]
