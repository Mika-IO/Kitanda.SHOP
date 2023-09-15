from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Loja, ProductCategory, Product, Checkout


class LandingPageView(View):
    def get(self, request):
        lojas = [
            {
                "name": "Gramercy Tavern",
                "image": "https://img.freepik.com/vetores-premium/icone-do-icone-da-loja_942802-808.jpg?w=826",
                "url": "gramercy-tavern",
            },
            {
                "name": "Shake Shack",
                "image": "https://img.freepik.com/vetores-premium/icone-do-icone-da-loja_942802-808.jpg?w=826",
                "url": "shake-shack",
            },
            {
                "name": "Gott's Roadside",
                "image": "https://img.freepik.com/vetores-premium/icone-do-icone-da-loja_942802-808.jpg?w=826",
                "url": "gotts-roadside",
            },
            {
                "name": "Emmy Squared",
                "image": "https://img.freepik.com/vetores-premium/icone-do-icone-da-loja_942802-808.jpg?w=826",
                "url": "emmy-squared",
            },
            {
                "name": "Shake Shack",
                "image": "https://img.freepik.com/vetores-premium/icone-do-icone-da-loja_942802-808.jpg?w=826",
                "url": "shake-shack-2",
            },
            {
                "name": "Peter Luger Steak",
                "image": "https://img.freepik.com/vetores-premium/icone-do-icone-da-loja_942802-808.jpg?w=826",
                "url": "peter-luger-steak",
            },
            {
                "name": "Holeman & Finch",
                "image": "https://img.freepik.com/vetores-premium/icone-do-icone-da-loja_942802-808.jpg?w=826",
                "url": "holeman-finch",
            },
            {
                "name": "Pat LaFrieda Meats",
                "image": "https://img.freepik.com/vetores-premium/icone-do-icone-da-loja_942802-808.jpg?w=826",
                "url": "pat-lafrieda-meats",
            },
        ]
        print("aaaaaaaaaaaaaaaaaaa")
        # Implement your logic to fetch nearby stores or popular stores
        return render(request, "index.html", {"lojas": lojas})


class LojaView(View):
    def get(self, request, name):
        produtos = [
            {
                "nome": "Gramercy Tavern",
                "preco": "R$ 99,00",
                "imagem": "./static/img/cardapio/burguers/Gramercy-Tavern-Burger-and-Kielbasa-Kit-6.4.21-72ppi-1x1-15.jpg",
                "id": "the-gramercy-tavern-burger-4-pack",
            },
            {
                "nome": "Shake Shack",
                "preco": "R$ 49,00",
                "imagem": "./static/img/cardapio/burguers/shake-shack-shackburger-8-pack.973a5e26836ea86d7e86a327becea2b0.jpg",
                "id": "shake-shack-shackburger-8-pack",
            },
            {
                "nome": "Gott's Roadside",
                "preco": "R$ 99,00",
                "imagem": "./static/img/cardapio/burguers/gotts-complete-cheeseburger-kit-for-4.7bdc74104b193427b3fe6eae39e05b5e.jpg",
                "id": "gotts-cheeseburger-kit-for-4",
            },
            {
                "nome": "Emmy Squared",
                "preco": "R$ 99,00",
                "imagem": "./static/img/cardapio/burguers/le-big-matt-kit-for-6.1ddae6e382bb3218eeb0fd5247de115a.jpg",
                "id": "le-big-matt-kit-for-6",
            },
            {
                "nome": "Shake Shack",
                "preco": "R$ 89,00",
                "imagem": "./static/img/cardapio/burguers/shake-shack-shackburger-16-pack.316f8b09144db65931ea29e34869287a.jpg",
                "id": "shake-shack-shackburger-16-pack",
            },
            {
                "nome": "Peter Luger Steak House",
                "preco": "R$ 175,95",
                "imagem": "./static/img/cardapio/burguers/usda-prime-burgers-pack-of-18-8oz-each.274c67f15aa1c0b210dbf51801706670.jpg",
                "id": "21-usda-prime-burgers-pack-of-18-8oz-each",
            },
            {
                "nome": "Holeman & Finch",
                "preco": "R$ 79,00",
                "imagem": "./static/img/cardapio/burguers/handf-double-stack-burger-kit-for-4.4ee9f54b1d6087e9996335f07c13e5cd.jpg",
                "id": "double-stack-burger-kit-for-4",
            },
            {
                "nome": "Pat LaFrieda Meats",
                "preco": "R$ 109,00",
                "imagem": "./static/img/cardapio/burguers/the-burger-bash-package.bd9d12d031865940bbe5faf15f1a62f8.jpg",
                "id": "goldbelly-burger-bash-pack",
            },
        ]
        # Implement your logic to fetch store details by name
        return render(
            request,
            "loja.html",
            {"name": name.replace("-", " ").title, "produtos": produtos},
        )


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


class loginView(View):
    def get(self, request):
        # Implement your logic to fetch store information for the login
        return render(request, "login.html", {})


class registerView(View):
    def get(self, request):
        # Implement your logic to fetch store information for the register
        return render(request, "register.html", {})
