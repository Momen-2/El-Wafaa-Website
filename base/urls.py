from django.urls import path
from base import views

app_name = "base"

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("product/<slug:slug>", views.ProductDetailView.as_view(), name="product"),
]