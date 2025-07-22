from django.shortcuts import render
from .models import Review
from django.db.models import Count, Q

def product_sentiments(request):
    products = (
        Review.objects.values("product")
        .annotate(
            total=Count("id"),
            positive=Count("id", filter=Q(sentiment="positive")),
            neutral=Count("id", filter=Q(sentiment="neutral")),
            negative=Count("id", filter=Q(sentiment="negative")),
        )
    )

    for product in products:
        total = product["total"] or 1
        product["positive"] = round((product["positive"] / total) * 100, 2)
        product["neutral"] = round((product["neutral"] / total) * 100, 2)
        product["negative"] = round((product["negative"] / total) * 100, 2)

    return render(request, "reviews/dashboard.html", {"products": products})
