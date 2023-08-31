from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Loja, ProductCategory, Product, Checkout


class LandingPageView(View):
    def get(self, request):
        # Implement your logic to fetch nearby stores or popular stores
        return render(request, "landing_page.html", {})


class LojaView(View):
    def get(self, request, name):
        # Implement your logic to fetch store details by name
        return render(request, "loja.html", {})


class ComprarView(View):
    def get(self, request, name):
        # Implement your logic to fetch products by store name
        return render(request, "comprar.html", {})


class CheckoutView(View):
    def get(self, request, id):
        # Implement your logic to fetch checkout details by id
        return render(request, "checkout.html", {})


class DashboardView(View):
    def get(self, request):
        # Implement your logic to fetch store information for the dashboard
        return render(request, "dashboard.html", {})
