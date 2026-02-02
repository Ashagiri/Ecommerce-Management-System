# Create your views here.
from django.shortcuts import render
from .models import Product

def product_list(request):
    # Fetch all available products from the database
    products = Product.objects.filter(available=True)
    return render(request, 'products/list.html', {'products': products})