import React, { useState, useEffect } from 'react';
import Nav from '../components/Nav';
import SplashScreen from '../components/SplashScreen';
import Store from '../components/Store';


const StoreList = ({ onVisitStore }) => {
    const [searchStores, setSearchStores] = useState(false);
    const stores = [
        {
            nome: "Loja 1",
            link: "/loja.html",
            logo: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
            descricao: "Descrição da Loja 1",
            cidade: "Cidade 1",
            estado: "Estado 1"
        },
        {
            nome: "Loja 2",
            link: "/loja.html",
            logo: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
            descricao: "Descrição da Loja 2",
            cidade: "Cidade 2",
            estado: "Estado 2"
        },
        {
            nome: "Loja 3",
            link: "/loja.html",
            logo: "https://cdn.casaeculinaria.com/wp-content/uploads/2023/04/05163949/Hamburguer-artesanal.webp",
            descricao: "Descrição da Loja 3",
            cidade: "Cidade 3",
            estado: "Estado 3"
        }
    ];

    const handleVisitStore = () => {
        onVisitStore();

    };

    const handleSearchStores = () => {
        setSearchStores(true);
    };

    return (
        <div className="container">
            <div className="col s12">
                <div className="row">
                    <div className="col s12 m6 offset-m3">
                        <div className="card" style={{ marginTop: "10vh" }}>
                            <div className="card-content">
                                <div className="input-field">
                                    <input id="location" placeholder="Endereço" type="text" />
                                </div>
                                <div className="row">
                                    <div className="col s12 center-align">
                                        <button className="btn waves-effect waves-light kgreen" onClick={handleSearchStores}>
                                            Buscar lojas
                                        </button>
                                    </div>
                                    <div className="col s12 center-align">

                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>

                {searchStores && (

                    <div id="store-list" className="row">
                        {stores.map((store, index) => (
                            <div key={index} className="col s12 m6 l4">
                                <div className="card">
                                    <div className="card-image">
                                        <img src={store.logo} alt="Logo da Loja" />
                                    </div>
                                    <div className="card-content">
                                        <span className="card-title">{store.nome}</span>
                                        <p>{store.descricao}</p>
                                    </div>
                                    <div className="card-action">
                                        <a href="#" style={{ color: "#2bbbad" }} onClick={handleVisitStore}>
                                            Visitar Loja
                                        </a>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};


const Buy = () => {
    const [visitStore, setVisitStore] = useState(false); // Estado para controlar a exibição do componente Store

    const handleVisitStore = () => {
        setVisitStore(true); // Exibe o componente Store ao clicar no link "Visitar Loja"
    };

    return (
        <div>
            {!visitStore && (
                <div>
                    <SplashScreen />
                    <Nav />
                    <StoreList onVisitStore={handleVisitStore} />
                </div>
            )}
            {visitStore && (
                <div>
                    <SplashScreen />
                    <Nav />
                    <Store />
                </div>
            )
            }
        </div>
    );
};

export default Buy
