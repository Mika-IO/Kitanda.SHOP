"use strict";

const { useState, useEffect } = React;

const SplashScreen = () => {
  const [showSplash, setShowSplash] = useState(true);

  useEffect(() => {
    const randomTime = Math.floor(Math.random() * 701); // Gera um número aleatório entre 0 e 700
    setTimeout(() => {
      setShowSplash(false);
    }, randomTime);
  }, []);

  const Splash = () => (
    <div className="splash-screen">
      <img className="splash-logo" src="logo.svg" alt="Logo da aplicação" />
      <div className="progress">
        <div className="indeterminate"></div>
      </div>
    </div>
  );

  return <div>{showSplash ? <Splash /> : <div></div>}</div>;
};

customElements.define("splash-screen", SplashScreen);
