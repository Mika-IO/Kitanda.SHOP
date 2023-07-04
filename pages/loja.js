const Loja = (props) => {
  const lojaId = props.match.params.loja_id;
  // Fazer algo com o lojaId...

  return <h1>Loja {lojaId}</h1>;
};
