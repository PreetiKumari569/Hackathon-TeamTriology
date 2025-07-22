from django.shortcuts import render
from .models import Product

def product_sentiments(request):
    products = Product.objects.all()
    product_data = []

    for product in products:
        reviews = product.reviews.all()
        total = reviews.count()
        positive = reviews.filter(sentiment='positive').count()
        percentage = round((positive / total) * 100, 2) if total else 0
        product_data.append((product.name, percentage, total))

    # Sort by highest % of positive reviews
    sorted_data = sorted(product_data, key=lambda x: x[1], reverse=True)

    return render(request, 'reviews/dashboard.html', {'data': sorted_data})
