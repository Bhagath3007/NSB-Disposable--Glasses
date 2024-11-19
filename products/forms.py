# products/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile  # Import your UserProfile model
from .models import Product


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Make sure you have a UserProfile model defined
        fields = ['profile_picture']  # Include only the fields you want to edit

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        if commit:
            user_profile.save()
        return user_profile
    
    from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'discount_price', 'image', 'rating', 'reviews_count', 'is_promotion', 'promotion_details']
