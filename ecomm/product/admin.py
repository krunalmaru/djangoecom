from django.contrib import admin
from .models import Category, Product, ProductImage,Sizevariant,Colorvariant,Coupon
# Register your models here.


admin.site.register(Category)
admin.site.register(Coupon)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','category','price']
    inlines = [ProductImageAdmin]

@admin.register(Colorvariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name','price']
    model = Colorvariant

@admin.register(Sizevariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name','price']
    model = Sizevariant

admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)