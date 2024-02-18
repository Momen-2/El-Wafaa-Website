from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from base import models


class HomeTemplateView(TemplateView):
    template_name = "base/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fruits"] = models.Product.objects.filter(type="FRUIT")
        context["vegetables"] = models.Product.objects.filter(type="VEGETABLE")
        context["spices"] = models.Product.objects.filter(type="SPICE")

        return context
    
    def post(self, request, *args, **kwargs):
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        
        send_mail(
            subject,
            "This email is from: " + email + "\n" + message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        
        return HttpResponseRedirect(self.request.path_info)

class ProductDetailView(DetailView):
    model = models.Product
    template_name = "base/product.html"