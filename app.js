"use strict";

const DinamicHome = () => {
  return (
    <div>
      <SplashScreen />
      <Nav />
    </div>
  );
};

ReactDOM.render(<DinamicHome />, document.querySelector("#root"));
