# products/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            UserProfile.objects.create(user=user)  # Create a UserProfile instance
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile')  # Redirect to user profile
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def user_profile(request):
    # Get all products
    products = Product.objects.all()


    # Render the page and pass the products data to the template
    return render(request, 'profile.html', {'products': products})
    # Use get_or_create to handle missing UserProfile instances
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})


# ----------------------------------------------------------------products--------------------------------


@login_required
def add_product(request):
    if request.user.is_authenticated:  # Ensure the user is logged in
        if request.user.is_superuser:  # Only superusers (owners or admins) can add products
            if request.method == 'POST':
                form = ProductForm(request.POST, request.FILES)
                if form.is_valid():
                    # Automatically set the owner of the product to the current logged-in user
                    product = form.save(commit=False)
                    product.owner = request.user
                    product.save()
                    return redirect('home')  # Redirect to the homepage after saving

            else:
                form = ProductForm()
            return render(request, 'add_product.html', {'form': form})
        else:
            # If the user is not authorized (not superuser)
            return redirect('home')
    else:
        return redirect('login')  # Redirect to login page if the user is not logged in
    
    
# views.py

from django.shortcuts import render
from .models import Product

import requests
from django.shortcuts import render
from .models import Product

# Function t
import requests
from decimal import Decimal
from django.shortcuts import render
from .models import Product

# Function to get the live exchange rate for USD to INR
 
# View function to display products
def home(request):
    
    # Get all products
    products = Product.objects.all()


    # Render the page and pass the products data to the template
    return render(request, 'base.html', {'products': products})




    
    # views.py
from django.shortcuts import render, redirect
from .models import CartItem
from .models import Product  # Assuming the Product model is in the same app
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

    if not created:
        cart_item.quantity += 1  # If the item already exists, increment the quantity
        cart_item.save()

    return redirect('view_cart')  # Redirect to the view cart page

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    
    return render(request, 'view_cart.html', context)
# views.py




from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def view_cart(request):
    # Your cart logic (e.g., fetching cart items from the session or database)
    return render(request,'view_cart.html')

from django.shortcuts import render

def view_cart(request):
    return render(request, 'view_cart.html')

def view_cart(request):
    cart = request.session.get('cart', [])
    products_in_cart = Product.objects.filter(id__in=cart)
    
    return render(request, 'view_cart.html', {'products': products_in_cart})
from django.shortcuts import redirect
from .models import Product

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Get cart from session or initialize an empty list if not found
    cart = request.session.get('cart', [])
    
    # Add product to cart (this assumes cart is a list of product IDs)
    if product.id not in cart:
        cart.append(product.id)
    
    # Save cart back to session
    request.session['cart'] = cart
    
    return redirect('view_cart')  # Redirect to the cart view
from django.shortcuts import render, redirect
from .models import Product

# Example of a cart management without session
def add_to_cart(request, product_id):
    # Get the product object
    product = Product.objects.get(id=product_id)

    # Initialize cart as a list of products
    cart = []
    
    # For this example, we just create an empty cart for now
    # If you want to store it temporarily, you'll need to pass it through the context or use session as before
    cart.append({'product_id': product.id, 'quantity': 1, 'price': product.price})

    # For now, we just print the cart to the console for debugging purposes
    print("Cart items:", cart)

    # Normally, we'd redirect to a page to view the cart or proceed with checkout
    return redirect('view_cart')

def view_cart(request):
    # Example cart, this can come from a context or session
    cart = [{'product_id': 1, 'quantity': 2, 'price': 25.00}, {'product_id': 2, 'quantity': 1, 'price': 15.00}]
    total_price = sum(item['quantity'] * item['price'] for item in cart)

    # Display cart items on the template
    return render(request, 'view_cart.html', {'cart_items': cart, 'total_price': total_price})
# views.py


from django.shortcuts import render

def view_cart(request):
    # Retrieve cart from session or initialize an empty list
    cart = request.session.get('cart', [])
    context = {'cart': cart}
    return render(request, 'view_cart.html', context)
from django.shortcuts import render

def view_cart(request):
    # Example cart structure; replace it with your actual implementation
    cart = request.session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    
    return render(request, 'view_cart.html', {'cart': cart, 'total_price': total_price})

from django.shortcuts import render, redirect

def add_to_cart(request, product_id):
    # Get the product based on the ID (adjust according to your models)
    product = get_object_or_404(Product, id=product_id)
    
    # Get the cart from the session, or create an empty cart if it doesn't exist
    cart = request.session.get('cart', [])

    # Check if the product is already in the cart
    existing_product = next((item for item in cart if item['id'] == product.id), None)

    if existing_product:
        # Update the quantity if the product is already in the cart
        existing_product['quantity'] += 1
    else:
        # Add the product to the cart
        cart.append({'id': product.id, 'title': product.title, 'price': product.price, 'quantity': 1})

    # Save the cart back into the session
    request.session['cart'] = cart
    
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    
    return render(request, 'view_cart.html', {'cart': cart, 'total_price': total_price})

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Product  # Assuming you have a Product model

def add_to_cart(request, product_id):
    # Retrieve product by ID
    product = get_object_or_404(Product, id=product_id)
    
    # Retrieve the current cart from the session or initialize an empty cart if not present
    cart = request.session.get('cart', [])
    
    # Check if the product is already in the cart
    for item in cart:
        if item['id'] == product.id:
            item['quantity'] += 1  # Update quantity if already in cart
            break
    else:
        # Add the product to the cart if not already present
        cart.append({'id': product.id, 'title': product.title, 'price': product.price, 'quantity': 1})

    # Save the cart back to the session
    request.session['cart'] = cart
    
    return redirect('view_cart')

def view_cart(request):
    # Retrieve the cart from the session
    cart = request.session.get('cart', [])
    
    # Calculate the total price of items in the cart
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    
    return render(request, 'view_cart.html', {'cart': cart, 'total_price': total_price})

def checkout(request):
    # Your checkout logic here
    return render(request, 'checkout.html')


# Define a view for the contact us page

def about(request):
    return render(request, 'aboutus.html')

def contact_view(request):
    return render(request, 'contact.html')



from django.shortcuts import render
from .models import Product
from django.db.models import Q

def home1(request):
    # Fetching all products
    products = Product.objects.all()
    return render(request, 'homep.html', {'products': products})

def search(request):
    query = request.GET.get('query', '')
    # Filtering products based on search query
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'homep.html', {'products': products})

