from django.urls import path
from base import views

app_name = "base"

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("product/<int:pk>", views.ProductDetailView.as_view(), name="product"),
]