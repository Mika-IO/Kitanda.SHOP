import '../styles/style.css';
import 'materialize-css/dist/css/materialize.min.css';


function Kitanda({ Component, pageProps }) {

    return <>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
        <Component {...pageProps} />;
    </>

}

export default Kitanda;
