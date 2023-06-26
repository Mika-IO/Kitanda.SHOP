# app.py

from alicepy.alice import Alice
from components.base import page

from pages.home import home
from pages.loja_perfil import loja_perfil
from pages.loja import loja


app = Alice()

app.add(page(home))
app.build("home.html")

app = Alice()

app.add(page(loja))
app.build("loja.html")

app = Alice()

app.add(page(loja_perfil))
app.build("loja_perfil.html")


# app.urls = [
#     ("/", "index.html"),
#     ("/comprar", "comprar.html"),
#     ("/vender", "vender.html"),
#     ("/store_profile/<store_id>", "store_profile.html"),
#     ("/store/<store_id>", "store.html"),
# ]

# if __name__ == "__main__":
