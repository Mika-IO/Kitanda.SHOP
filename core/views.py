from django.shortcuts import render, redirect

# Auth
from django.contrib.auth import login as auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group


from .models import Store, Product, Order

# utils


def money_format(text):
    return "{:.2f}".format(text).replace(".", ",")


def increment_product_in_cart(cart, product):
    product_in_cart = False
    for item in cart:
        if item["product_id"] == str(product.id):
            item["quantity"] += 1
            product_in_cart = True
            break
    return product_in_cart


def add_product(cart, product):
    cart.append(
        {
            "product_id": str(product.id),
            "product_name": product.name,
            "product_price": str(product.price),
            "product_image": str(product.image),
            "quantity": 1,
        }
    )
    return cart


def remove_product(cart, product, all=False):
    new_cart = []
    for p in cart:
        if p["product_id"] == str(product.id):
            if p["quantity"] > 1 and not all:
                p["quantity"] -= 1
                new_cart.append(p)
        else:
            new_cart.append(p)
    return new_cart


def get_cart(request):
    return request.session.get("cart", [])


def update_cart(request, cart):
    request.session["cart"] = cart
    return cart


def get_address(request):
    address = request.session.get("address", [])
    return address


def get_whatsapp_link(context, phone_number):
    products_message = "Gostaria de fazer o pedido dos produtos:\n\n"
    for item in context["cart"]:
        products_message += f"- {item['product_name']} (Quantidade: {item['quantity']}, Preço: R${item['product_price']})\n"
    mensagem_context = f"Olá, vim pelo https://kitanda.shop/{context['name']}  :)\n\n"
    mensagem_context += products_message
    mensagem_context += f"\nEndereço: {context['address']['bairro']}, {context['address']['rua']} {context['address']['numero']}, {context['address']['complemento']}\n"
    mensagem_context += f"Subtotal: R${context['sub_total']}\n"
    mensagem_context += f"Taxa de entrega: R${context['delivery_fee']}\n"
    mensagem_context += f"Total: R${context['total']}"

    link = f"https://wa.me/{phone_number}?text={mensagem_context}"
    return link


# views


def handler404(request, *args, **argv):
    return render(request, "page_404.html", {})


def handler500(request, *args, **argv):
    return render(request, "page_500.html", {})


def home(request):
    stores = Store.objects.all()
    return render(request, "index.html", {"lojas": stores})


def store(request, name):
    store = Store.objects.get(slug=name)
    products = Product.objects.filter(store=store)
    cart = get_cart(request)

    product_id = request.GET.get("addToCart")
    if product_id:
        product = Product.objects.get(id=product_id)
        if product:
            is_product_in_cart = increment_product_in_cart(cart, product)

            if not is_product_in_cart:
                cart = add_product(cart, product)
            update_cart(request, cart)
            print(cart)

    return render(
        request,
        "loja.html",
        {
            "loja": store,
            "products": products,
            "products_in_cart": sum(p["quantity"] for p in cart),
        },
    )


def product(request, id):
    product = Product.objects.get(id=id)
    if product:
        context = {
            "id": product.id,
            "store_slug": product.store.slug,
            "name": product.name,
            "descript": product.description,
            "price": product.price,
            "image": product.image,
        }

        return render(
            request,
            "product.html",
            context,
        )
    return redirect("/")


def cart(request, name):
    cart = get_cart(request)

    product_id = request.GET.get("add")
    if product_id:
        product = Product.objects.get(id=product_id)
        if product:
            cart = get_cart(request)

            is_product_in_cart = increment_product_in_cart(cart, product)

            if not is_product_in_cart:
                cart = add_product(cart, product)
            update_cart(request, cart)

    product_id = request.GET.get("minus")
    if product_id:
        product = Product.objects.get(id=product_id)
        if product:
            cart = get_cart(request)

            cart = remove_product(cart, product)
            update_cart(request, cart)

    product_id = request.GET.get("remove")
    if product_id:
        product = Product.objects.get(id=product_id)
        if product:
            cart = get_cart(request)

            cart = remove_product(cart, product, all=True)
            update_cart(request, cart)

    store = Store.objects.get(slug=name)
    sub_total = 0
    total = 0
    for product in cart:
        sub_total += product["quantity"] * float(product["product_price"])
    delivery_fee = store.delivery_fee
    if sub_total:
        total = float(sub_total) + float(delivery_fee)
    return render(
        request,
        "cart/cart.html",
        {
            "name": name,
            "cart": cart,
            "sub_total": money_format(sub_total),
            "total": money_format(total),
            "delivery_fee": money_format(delivery_fee),
        },
    )


def address(request, name):
    if request.method == "POST":
        bairro = request.POST.get("bairro")
        rua = request.POST.get("rua")
        numero = request.POST.get("numero")
        complemento = request.POST.get("complemento")

        request.session["address"] = {
            "bairro": bairro,
            "rua": rua,
            "numero": numero,
            "complemento": complemento,
        }
        print(request.session["address"])
        return redirect(f"/review/{name}/")

    cart = get_cart(request)
    store = Store.objects.get(slug=name)
    sub_total = 0
    total = 0
    for product in cart:
        sub_total += product["quantity"] * float(product["product_price"])
    delivery_fee = store.delivery_fee
    if sub_total:
        total = float(sub_total) + float(delivery_fee)
    return render(
        request,
        "cart/address.html",
        {
            "name": name,
            "sub_total": money_format(sub_total),
            "total": money_format(total),
            "delivery_fee": money_format(delivery_fee),
        },
    )


def review(request, name):
    address = get_address(request)
    cart = get_cart(request)
    store = Store.objects.get(slug=name)

    if not cart:
        return redirect(f"/cart/{name}")

    if not address:
        return redirect(f"/address/{name}")

    sub_total = 0
    total = 0
    for product in cart:
        sub_total += product["quantity"] * float(product["product_price"])
    delivery_fee = store.delivery_fee
    if sub_total:
        total = float(sub_total) + float(delivery_fee)

    context = {
        "name": name,
        "address": address,
        "cart": cart,
        "sub_total": money_format(sub_total),
        "total": money_format(total),
        "delivery_fee": money_format(delivery_fee),
    }

    complete = request.GET.get("complete")
    if complete:
        order = Order(
            status="pendente",
            store=store,
            content=str(context),
            delivery_fee=delivery_fee,
            subtotal=sub_total,
            total=total,
        )
        order.save()
        whatsapp_link = get_whatsapp_link(context, store.whatsapp)
        return redirect(whatsapp_link)

    return render(request, "cart/review.html", context)


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
                error = "Usuário ou senha inválido"
        else:
            error = "Usuário ou senha inválido"
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

            # Adicione o usuário ao grupo "Owner"
            owner_group, created = Group.objects.get_or_create(name="Owner")
            user.groups.add(owner_group)
            user.is_staff = True
            user.save()
            # Adicione qualquer código adicional aqui para associar o usuário a um time, se necessário.

            return redirect("/login/")
        else:
            error = "Formulário inválido"
    else:
        form = UserCreationForm()
    return render(
        request,
        template_name="register.html",
        context={"register_form": form, "error": error},
    )
