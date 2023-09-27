from django.shortcuts import render, redirect

# Auth
from django.contrib.auth import login as auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from django.views.decorators.csrf import csrf_protect

from .models import Store, Product


def home(request):
    stores = Store.objects.all()
    return render(request, "index.html", {"lojas": stores})


def store(request, name):
    produtos = [
        {
            "nome": "Gramercy Tavern",
            "preco": "R$ 99,00",
            "imagem": "https://teuto.com.br/wp-content/uploads/2021/12/Laboratorio-Teuto-lanca-medicamento.jpg",
            "id": "the-gramercy-tavern-burger-4-pack",
        },
        {
            "nome": "Pat LaFrieda Meats",
            "preco": "R$ 109,00",
            "imagem": "https://teuto.com.br/wp-content/uploads/2021/12/Laboratorio-Teuto-lanca-medicamento.jpg",
            "id": "goldbelly-burger-bash-pack",
        },
    ]
    # Implement your logic to fetch store details by name
    return render(
        request,
        "loja.html",
        {"name": name.replace("-", " ").title, "produtos": produtos},
    )


def product(request, id):
    context = {
        "store_name": "store",
        "name": "steak-product".replace("-", " ").title,
        "price": "99,00",
        "image": "https://teuto.com.br/wp-content/uploads/2021/12/Laboratorio-Teuto-lanca-medicamento.jpg",
        "descript": "Lorem ispansum dolor sit amet . Os operadores gráficos e tipográficos sabem disso bem, na realidade, todas as profissões que lidam com o universo da comunicação têm um relacionamento estável com essas palavras, mas o que é? Lorem ipsum é um texto fofo sem qualquer sentido. É uma seqüência de palavras latinas que, como estão posicionadas, não formem frases com um sentido completo, mas dão vida a um texto de teste útil para preencher espaços que irão Posteriormente serão ocupados a partir de textos ad hoc compostos por profissionais de comunicação.",
        "id": "the-gramercy-tavern-burger-4-pack",
    }

    # Implement your logic to fetch store details by name
    return render(
        request,
        "product.html",
        context,
    )


def money_format(text):
    return "{:.2f}".format(text).replace(".", ",")


def cart(request, name):
    produtos = [{"produt": "nome", "quantity": 1, "price": 23.5}]
    sub_total = 0
    for p in produtos:
        sub_total += p["quantity"] * p["price"]
    entrega = 7
    total = sub_total + entrega
    return render(
        request,
        "cart/cart.html",
        {
            "name": name,
            "sub_total": money_format(sub_total),
            "total": money_format(total),
            "entrega": money_format(entrega),
        },
    )


def adress(request, name):
    produtos = [{"produt": "nome", "quantity": 1, "price": 23.5}]
    sub_total = 0
    for p in produtos:
        sub_total += p["quantity"] * p["price"]
    entrega = 7
    total = sub_total + entrega
    return render(
        request,
        "cart/adress.html",
        {
            "name": name,
            "sub_total": money_format(sub_total),
            "total": money_format(total),
            "entrega": money_format(entrega),
        },
    )


def dashboard(request):
    # Implement your logic to fetch store information for the dashboard
    return render(request, "seller/dashboard.html", {})


@csrf_protect
def login(request):
    error = False
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect("/dashboard/")
            else:
                error = "Invalid username, password or capcha."
        else:
            error = "Invalid username, password or capcha."
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="login.html",
        context={"login_form": form, "error": error},
    )


@csrf_protect
def register(request):
    error = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/login/")
        else:
            error = "Formulário inválido"
    form = UserCreationForm()
    return render(
        request,
        template_name="register.html",
        context={"register_form": form, "error": error},
    )
