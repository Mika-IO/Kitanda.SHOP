from alicepy.alice import Component


loja_perfil = Component(
    f"""
        <section class="hero is-primary kgreen is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title is-1">Pizzaria do Gordola</h1>
                    <h2 class="subtitle is-3">A melhor pizza da cidade</h2>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container has-text-centered">
                <h3 class="title mb-6 is-4">Retirada ou Delivery</h3>
            </div>
            <div class="container has-text-centered">
                <a class="button is-primary kgreen is-large mt-4" href="STORE.HTML">PEDIDO ONLINE</a>
            </div>
            <div class="container mt-6">
                <p class="has-text-centered">
                    Rua Urubu do pix Bairro setor 99 Nº 40028922, Ariquemes-RO
                </p>
                <p class="has-text-centered">
                    Digital menu of The Original Pizza
                </p>
            </div>
        </section>
    """
)
