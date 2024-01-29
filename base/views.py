from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from base import models


class HomeTemplateView(TemplateView):
    template_name = "base/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fruits"] = models.Product.objects.filter(type="FRUIT")
        context["vegetables"] = models.Product.objects.filter(type="VEGETABLE")
        context["spices"] = models.Product.objects.filter(type="SPICE")

        return context

class ProductDetailView(DetailView):
    model = models.Product
    template_name = "base/product.html"