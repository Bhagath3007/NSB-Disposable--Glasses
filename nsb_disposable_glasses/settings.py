from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'your-secret-key'  # Replace with a secure random key for production
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['your-vercel-project-name.vercel.app', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',  # Your custom app for the project
    'django.contrib.sites',  # Required for django-allauth
    'allauth',  # Include django-allauth
    'allauth.account',  # Account management with allauth
    # Uncomment below if you want social account logins
    # 'allauth.socialaccount',  
]

# Sites framework
SITE_ID = 1

# Configure authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Add django-allauth backend
]

# Configure django-allauth settings
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # Set to 'mandatory' for required email verification
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # Allow login by username or email
ACCOUNT_USERNAME_REQUIRED = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Add allauth middleware
]

ROOT_URLCONF = 'nsb_disposable_glasses.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Directory for custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nsb_disposable_glasses.wsgi.application'

# Database Configuration
# Since you're using SQLite, this is fine for deployment, but remember it's not suitable for high traffic or production-level databases.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # SQLite database file
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# Set STATICFILES_DIRS and STATIC_ROOT for production use.
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Directory for static files during development
STATIC_ROOT = BASE_DIR / "staticfiles"  # Directory for collected static files in production

# Media files (User-uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Directory for media files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production (don't forget to change `SECRET_KEY` to a secure key)
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS (ensure you're using HTTPS)
