from django.urls import path
from accounts.views import login_page, register_page, acivate_email, cart

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('activate/<email_token>/', acivate_email, name='acivate_email'),
    path('cart/', cart, name='cart'),
    
]
