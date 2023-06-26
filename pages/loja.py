from alicepy.alice import Component


loja = Component(
    f"""
    <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item has-text-centered is-size-3" href="#">
                <strong>Pizzaria do Gordola</strong>
            </a>
        </div>
    </nav>
    <div class="control">
            <a class="button is-primary">
              Pesquisar
            </a>
          </div>
        </div>
      </div>
      <div class="column is-narrow">
        <div class="select">
          <select>
            <option>Categoria 1</option>
            <option>Categoria 2</option>
            <option>Categoria 3</option>
            <option>Categoria 4</option>
            <option>Categoria 5</option>
          </select>
        </div>
      </div>
    </div>
  </div>
    <section class="section is-flex-touch">
        <div class="box has-background-white">
            <article class="media">
                <div class="media-left">
                    <figure class="image is-96x96">
                        <img src="https://qlickmenu.s3-us-west-1.amazonaws.com/companies/products/93cde489-c265-43bd-b5cc-88ceb00eec51.jpg" alt="Image"/>
                    </figure>
                </div>
                <div class="media-content has-text-grey-dark">
                    <div class="content">
                        <p>
                            <strong class="has-text-grey-dark">
                                Hibiscus Ficus
                            </strong>
                            <br />
                            <small>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean efficitur sit amet massa fringilla egestas.
                            </small>
                            <br/>
                            
                        </p>
                    </div>
                    <nav class="level is-mobile">
                        <div class="level-left">
                            <p class="level-item is-size-4 has-text-primary has-text-weight-bold">
                                699$
                            </p>
                        </div>
                        <div class="level-right">
                            <p class="level-item">
                                <button class="button is-primary ">
                                    +
                                </button>
                            </p>
                        </div>
                    </nav>
                </div>
            </article>
        </div>
    </section>
    """
)
