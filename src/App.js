import React, { useState } from 'react';
import Store from './components/Store';

function App() {
  const [carrinho, setCarrinho] = useState([]);
  const [total, setTotal] = useState(0);
  return (
    <Store>
    </Store>
  );
}

export default App;
