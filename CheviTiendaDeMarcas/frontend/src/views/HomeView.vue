<template>
  <NavbarComponent></NavbarComponent>
  <MultimediaPrincipalComponent></MultimediaPrincipalComponent>
  <BrandsComponent></BrandsComponent>
  <PromoComponent></PromoComponent>
  <CategoryComponent></CategoryComponent>
  <ImageShowComponent></ImageShowComponent>
  <InstagramComponent></InstagramComponent>
  <FooterComponent></FooterComponent>
</template>
<script >
import NavbarComponent from '../components/NavbarComponent.vue';
import MultimediaPrincipalComponent from '../components/MultimediaPrincipal.vue';
import PromoComponent from '../components/PromoComponent.vue'
import CategoryComponent from '../components/CategoryComponent.vue';
import InstagramComponent from '../components/InstagramComponent.vue';
import BrandsComponent from '../components/BrandsComponent.vue';
import ImageShowComponent from '../components/ImageShowComponent.vue';
import FooterComponent from '../components/FooterComponent.vue'

import { onMounted } from 'vue';

export default {
  components: {
      NavbarComponent,
      MultimediaPrincipalComponent,
      PromoComponent,
      CategoryComponent,
      InstagramComponent,
      BrandsComponent,
      ImageShowComponent,
      FooterComponent
  },
  setup() {
    // Hacer scroll hacia la parte superior al cargar la vista del producto
    onMounted(() => {
      window.scrollTo(0, 0);
    });

    return {

    };
  },
};
</script>

<style>

html, body {
  overflow-x: hidden;
}

/* Estilos para la barra de desplazamiento */
::-webkit-scrollbar {
  width: 10px; /* Ancho de la barra de desplazamiento */
}

::-webkit-scrollbar-track {
  background-color: #072027; /* Color del fondo de la barra de desplazamiento */
}

::-webkit-scrollbar-thumb {
  background-color: #881A19; /* Color del pulgar de la barra de desplazamiento */
  border-radius: 5px; /* Radio de borde del pulgar */
}

::-webkit-scrollbar-thumb:hover {
  background-color: #881A19; /* Color del pulgar de la barra de desplazamiento al pasar el cursor */
}

.app-container {
  position: relative;
}

.NavbarComponent {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 999; /* Asegura que el navbar esté en la capa superior */
}


@media (max-width: 576px) {
  /* Estilos para pantallas más pequeñas (hasta 576px) */
  .computer_tab{
    display: none;
  }
}

@media (min-width: 577px) and (max-width: 991px) {
  /* Estilos para pantallas de tamaño mediano (de 577px a 991px) */
  .computer_tab{
    display: none;
  }
}

@media (min-width: 992px) {
  /* Estilos para pantallas más grandes (a partir de 992px) */
  .mobile_tab{
    display: none;
  }
}
</style>
