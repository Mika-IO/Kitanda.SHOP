var cartItems = [];

function addToCart(productName, price) {
  cartItems.push({ name: productName, price: price });
  updateCart();
}

function updateCart() {
  var cartList = document.getElementById("cart-items");
  cartList.innerHTML = "";

  for (var i = 0; i < cartItems.length; i++) {
    var item = cartItems[i];
    var listItem = document.createElement("li");
    listItem.innerText = item.name + " - R$ " + item.price.toFixed(2);
    cartList.appendChild(listItem);
  }
}
