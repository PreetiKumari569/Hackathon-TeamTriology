from django.urls import path
from .views import product_sentiments

urlpatterns = [
    path('', product_sentiments, name='dashboard'),
]
