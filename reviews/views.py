from django.shortcuts import render
from .models import Review
from django.db.models import Count, Avg, Q

def product_sentiments(request):
    products = (
        Review.objects.values("product_name")
        .annotate(
            total=Count("id"),
            positive=Count("id", filter=Q(sentiment_score__gt=0.2)),
            neutral=Count("id", filter=Q(sentiment_score__gte=-0.2) & Q(sentiment_score__lte=0.2)),
            negative=Count("id", filter=Q(sentiment_score__lt=-0.2)),
        )
    )

    # Convert counts to percentages
    for product in products:
        total = product["total"] or 1  # avoid division by zero
        product["positive"] = round((product["positive"] / total) * 100, 2)
        product["neutral"] = round((product["neutral"] / total) * 100, 2)
        product["negative"] = round((product["negative"] / total) * 100, 2)

    return render(request, "reviews/dashboard.html", {"products": products})
