from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.


def index(request):
    category = Category.objects.all()
    discountProduct = DiscountProduct.objects.all()
    context = {
        'category':category,
        'discountProduct': discountProduct
    }
    return render(request,'index.html',context)




from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def products(request, d_slug):
    
    slug_category = get_object_or_404(Category, slug=d_slug)

    
    category = Category.objects.all()

    
    products = Product.objects.filter(category=slug_category)

    products_count = Product.objects.count()

    context = {
        'category': category,
        'slug_category': slug_category,
        'products': products,
        'products_count':products_count
        
    }
    return render(request, 'products.html', context)

def productDetail(request, d_slug):
    slug_product = get_object_or_404(Product, slug=d_slug)
    category = Category.objects.all()
    context = {
        'category': category,
        'slug_product': slug_product
    }
    return render(request, 'productsDetail.html', context)

def sepet(request):
    return render(request,'sepet.html')
