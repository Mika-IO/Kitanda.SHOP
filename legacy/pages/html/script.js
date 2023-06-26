function searchStores() {
    var stores = [
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

    var locationInput = document.getElementById("location");
    var location = locationInput.value;

    // Aqui você pode utilizar a localização fornecida pelo usuário para buscar as lojas correspondentes
    // Você pode fazer uma requisição AJAX para um servidor que retorna a lista de lojas com base na localização

    // Exemplo de código para adicionar um item de loja fictícia na lista:
    var storeList = document.getElementById("store-list");
    storeList.innerHTML = ""; // Limpa a lista de lojas antes de adicionar os novos itens

    // Itera sobre a lista de lojas correspondentes e adiciona os itens à lista
    for (var i = 0; i < stores.length; i++) {
        var store = stores[i];

        var storeItem = document.createElement("div");
        storeItem.classList.add("col", "s12", "m6", "l4");
        storeItem.innerHTML = `
        <div className"card">
            <div className"card-image">
                <img src="${store.logo}" alt="Logo da Loja">
            </div>
            <div className"card-content">
                <span className"card-title">${store.nome}</span>
                <p>${store.descricao}</p>
            </div>
            <div className"card-action">
                <a href="${store.link}" style="color: #2bbbad;">Visitar Loja</a>
            </div>
        </div>
        `;
        storeList.appendChild(storeItem);
    }
}

// splash screen

window.addEventListener("load", function () {
    var splashScreen = document.querySelector(".splash-screen");
    var randomTime = Math.floor(Math.random() * 700); // Tempo aleatório entre 0 e 700 milissegundos

    setTimeout(function () {
        splashScreen.style.display = "none";
    }, randomTime);
});

