from alicepy.alice import Component

from components.base import base_layout

home = base_layout(
    Component(
        """
            <div class="section no-pad-bot" id="index-banner">
                <div class="container">
                    <br /><br />
                    <h1 class="title is-1 has-text-centered has-text-success">Comece já!</h1>
                    <div class="columns is-centered">
                        <div class="column is-half">
                            <h5 class="subtitle is-5 has-text-centered">
                                Pedidos de forma simples, rápida e prática!
                            </h5>
                        </div>
                    </div>
                    <div class="columns is-centered">
                        <div class="column">
                            <div class="buttons is-centered">
                                <a href="STORE_PROFILE.HTML" class="button is-success is-large">Comprar</a>
                                <a href="biz.html" class="button is-success is-large">Vender</a>
                            </div>
                        </div>
                    </div>
                    <br /><br />
                </div>
            </div>

            <div class="container">
                <div class="section">
                    <div class="columns is-centered">
                        <div class="column is-one-third">
                            <div class="box has-text-centered">
                                <h2 class="center kgreen">
                                    <i class="material-icons">flash_on</i>
                                </h2>
                                <h3 class="title is-3 has-text-success">Agilize seu negócio</h3>
                                <p>
                                    Descubra como nossa plataforma de pedidos pode simplificar e
                                    acelerar o processo de venda e gerência de pedidos para sua
                                    loja, seja você um supermercado, restaurante, farmácia ou
                                    qualquer outro tipo de negócio...
                                </p>
                            </div>
                        </div>

                        <div class="column is-one-third">
                            <div class="box has-text-centered">
                                <h2 class="center kgreen">
                                    <i class="material-icons">group</i>
                                </h2>
                                <h3 class="title is-3 has-text-success">Foco em UX</h3>
                                <p>
                                    Estamos empenhados em oferecer a melhor experiência possível
                                    para os usuários. Nossa interface é intuitiva e fácil de usar
                                    para clientes e lojas, tornando o processo de pedidos rápido e
                                    conveniente.
                                </p>
                            </div>
                        </div>

                        <div class="column is-one-third">
                            <div class="box has-text-centered">
                                <h2 class="center kgreen">
                                    <i class="material-icons">paid</i>
                                </h2>
                                <h3 class="title is-3 has-text-success">Free to use</h3>
                                <p>
                                    Aproveite todas as funcionalidades sem custo adicional. Nossa
                                    plataforma é gratuita, permitindo que você se concentre em
                                    seu negócio sem se preocupar com despesas adicionais. Para
                                    entender como ganhamos dinheiro, <a href="#">clique aqui</a>.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <br /><br />
            </div>
        """
    )
)
