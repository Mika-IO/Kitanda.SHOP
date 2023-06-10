"use strict";

const Nav = () => {
  return (
    <nav class="kgreen lighten-1" role="navigation">
      <div class="nav-wrapper container">
        <a id="logo-container" href="/" class="brand-logo">
          kitanda.shop
        </a>
      </div>
    </nav>
  );
};

customElements.define("nav-header", Nav);
