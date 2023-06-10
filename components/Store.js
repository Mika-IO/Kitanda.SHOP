"use strict";

const { useState, useEffect } = React;


const produtos = [
    {
        nome: "Item name",
        categoria: "Categoria 1",
        preco: "R$ 5.99",
        image: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
        descricao: "Description of the item goes here. It can be longer or shorter depending on the content."
    },
    {
        nome: "Item name",
        categoria: "Categoria 1",
        preco: "R$ 7.99",
        image: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
        descricao: "Description of the item goes here. It can be longer or shorter depending on the content."
    },
    {
        nome: "Item name",
        categoria: "Categoria 1",
        preco: "R$ 5.99",
        image: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
        descricao: "Description of the item goes here. It can be longer or shorter depending on the content."
    },
    {
        nome: "Item name",
        categoria: "Categoria 1",
        preco: "R$ 7.99",
        image: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
        descricao: "Description of the item goes here. It can be longer or shorter depending on the content."
    },
    {
        nome: "Item name",
        categoria: "Categoria 2",
        preco: "R$ 5.99",
        image: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
        descricao: "Description of the item goes here. It can be longer or shorter depending on the content."
    },
    {
        nome: "Item name",
        categoria: "Categoria 2",
        preco: "R$ 7.99",
        image: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
        descricao: "Description of the item goes here. It can be longer or shorter depending on the content."
    },
    {
        nome: "Item name",
        categoria: "Categoria 2",
        preco: "R$ 5.99",
        image: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
        descricao: "Description of the item goes here. It can be longer or shorter depending on the content."
    },
    {
        nome: "Item name",
        categoria: "Categoria 2",
        preco: "R$ 7.99",
        image: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
        descricao: "Description of the item goes here. It can be longer or shorter depending on the content."
    }
];


const FloatingButtons = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleButtons = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className="fixed-action-btn">
            <button className="btn-floating btn-large red" onClick={toggleButtons}>
                <i className="large material-icons">add</i>
            </button>
            {isOpen && (
                <ul>
                    <li>
                        <button className="btn-floating green">
                            <i className="material-icons">edit</i>
                        </button>
                    </li>
                    <li>
                        <button className="btn-floating blue">
                            <i className="material-icons">delete</i>
                        </button>
                    </li>
                </ul>
            )}
        </div>
    );
};




const ProductList = () => {

    return (
        <div className="row">
            {produtos.map((produto, index) => (
                <div key={index} className="col s12 m6 l4">
                    <div className="card">
                        <div className="card-image">
                            <img className="responsive-img" src={produto.image} alt="Imagem do produto" />
                        </div>
                        <div className="card-content">
                            <span className="card-title">{produto.nome}</span>
                            <p>{produto.descricao}</p>
                            <p>{produto.preco}</p>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    );
};

const Store = () => {
    return (
        <div className="container">
            <div className="row">
                <div className="col s12">
                    <h4 className="center-align">Pizzaria Delícia</h4>
                    <p className="center-align">As melhores pizzas da região!</p>

                    {/* <div className="row">
                        <div className="col s12 m4">
                            <div className="card">
                                <div className="card-content center-align">
                                    <i className="material-icons">phone</i>
                                    <p>Whatsapp</p>
                                </div>
                            </div>
                        </div>
                        <div className="col s12 m4">
                            <div className="card">
                                <div className="card-content center-align">
                                    <i className="material-icons">location_on</i>
                                    <p>Localização</p>
                                </div>
                            </div>
                        </div>
                        <div className="col s12 m4">
                            <div className="card">
                                <div className="card-content center-align">
                                    <i className="material-icons">add_shopping_cart</i>
                                    <p>Carrinho</p>
                                </div>
                            </div>
                        </div>
                    </div> */}

                    <FloatingButtons />

                    <div class="row">
                        <div class="col s12">
                            <div class="row">
                                <div class="input-field col s12">
                                    <i class="material-icons prefix">search</i>
                                    <input type="text" placeholder="Pesquisar..." id="autocomplete-input" class="autocomplete" />

                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="row">
                        <div className="col s12">
                            <div className="row">
                                <ProductList produtos={produtos} />
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </div>
    );
};

customElements.define("store-page", Store);
