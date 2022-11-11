from django.db import models
from base.models import BaseModel 
from django.utils.text import slugify


# Create your models here.
class Category(BaseModel):
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True,blank=True)
    category_image = models.ImageField(upload_to='categories')

    def save(self, *a,**kw):
        self.slug = slugify(self.category)
        super(Category,self).save(*a,**kw)
    
    def __str__(self):
        return self.category



class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField() 
    product_description = models.TextField()

    def save(self, *args,**kwargs):
        self.slug = slugify(self.product_name)
        super(Product,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.product_name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image =models.ImageField(upload_to='product')

