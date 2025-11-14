from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')


from .models import Product

def product_list(request):
    products = Product.objects.all()  # Fetch all products (SELECT * FROM product)
    return render(request, 'myapp/product_list.html', {'products': products})
