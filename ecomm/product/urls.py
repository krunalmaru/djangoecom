from django.urls import path
from product import views


urlpatterns = [
    path('<slug>/', views.get_product, name='product')
]
