# app.py

from alicepy.alice import Alice

from pages.home import home
from pages.loja_perfil import loja_perfil
from pages.loja import loja

app = Alice()

app.urls = [
    ("/", home, "index.html"),
    ("/store_profile/<store_id>", loja_perfil, "loja_perfil.html"),
    ("/store/<store_id>", loja, "loja.html"),
]

if __name__ == "__main__":
    app.run()
