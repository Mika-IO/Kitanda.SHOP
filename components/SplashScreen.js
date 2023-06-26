import React, { useState, useEffect } from 'react';
import logo from '../assets/logo.svg';
import Image from 'next/image'

function SplashScreen() {
  const [showSplash, setShowSplash] = useState(true);

  useEffect(() => {
    const randomTime = Math.floor(Math.random() * 701);
    setTimeout(() => {
      setShowSplash(false);
    }, randomTime);
  }, []);

  const Splash = () => (
    <div className="splash-screen">
      <Image className="splash-logo" src={logo} alt="Logo da aplicação" />
      <div className="progress">
        <div className="indeterminate"></div>
      </div>
    </div>
  );

  return <div>{showSplash ? <Splash /> : <div></div>}</div>;
}

export default SplashScreen;
