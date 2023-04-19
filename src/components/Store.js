import React, { useState } from 'react';
import { List, ListItem, ListItemText, ListItemSecondaryAction, IconButton, Typography, Button } from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';

function App() {
    const [cart, setCart] = useState([]);
    const [total, setTotal] = useState(0);

    const restaurant = {
        name: 'Restaurant XYZ',
        phone: '11234567890',
    };

    const products = [
        { name: 'Hamburger', price: 10.0 },
        { name: 'Pizza', price: 20.0 },
        { name: 'Salad', price: 5.0 },
    ];

    function addItem(name, price) {
        const item = {
            name: name,
            price: price,
        };
        setCart([...cart, item]);
        setTotal(total + price);
    }

    function removeItem(index) {
        const price = cart[index].price;
        const newCart = [...cart];
        newCart.splice(index, 1);
        setCart(newCart);
        setTotal(total - price);
    }

    function updateCart() {
        return (
            <>
                <List>
                    {cart.map((item, index) => (
                        <ListItem key={index}>
                            <ListItemText
                                primary={`${item.name} - $${item.price.toFixed(2)}`}
                            />
                            <ListItemSecondaryAction>
                                <IconButton edge="end" onClick={() => removeItem(index)}>
                                    <DeleteIcon />
                                </IconButton>
                            </ListItemSecondaryAction>
                        </ListItem>
                    ))}
                </List>
            </>
        );
    }

    function sendOrder() {
        let message = `Hi, I would like to place an order from ${restaurant.name}:\n`;
        cart.forEach((item) => {
            message += `- ${item.name} - $${item.price.toFixed(2)}\n`;
        });
        message += `\nTotal: $${total.toFixed(2)}`;
        const whatsappUrl =
            `https://wa.me/${restaurant.phone}?text=` + encodeURIComponent(message);
        window.open(whatsappUrl, '_blank');
    }

    return (
        <div>
            <Typography variant="h1">{restaurant.name}</Typography>
            <Typography>Welcome to {restaurant.name}! Choose items below:</Typography>
            <List>
                {products.map((product, index) => (
                    <ListItem key={index}>
                        <ListItemText
                            primary={`${product.name} - $${product.price.toFixed(2)}`}
                        />
                        <Button variant="contained" color="primary" onClick={() => addItem(product.name, product.price)}>
                            Add
                        </Button>
                    </ListItem>
                ))}
            </List>
            <Typography variant="h2">Cart</Typography>
            <List>{updateCart()}</List>
            <Typography>Total: ${total.toFixed(2)}</Typography>
            <Button variant="contained" color="primary" onClick={() => sendOrder()}>
                Place Order
            </Button>
        </div>
    );
}

export default App;
