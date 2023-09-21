<template>
    <div style="background-color: #F8FBE6;box-shadow: 0 4px 4px rgba(0, 0, 0, 0.4); position: fixed; width: 100%; z-index: 999;" v-bind:class="['navbar-container', { 'navbar-fixed': isNavbarFixed }]">
      <nav class="navbar navbar-expand-lg">
        <a class='mt-1' @click="back_home" style="cursor: pointer;">
          <img src="@/assets/Logo/Logo_Chevi.png" style="width: 170px;height: auto;" alt="Logo" class="mx-5">
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav m-auto ps-1 pe-5 d-flex justify-content-evenly " style="font-family: 'Poppins', sans-serif;font-size: 21px;color: black;">
            <li class="nav-item d-flex px-3" style=" font-size: 40px; box-shadow: -4px 0 4px rgba(7, 32, 39, 0.1), 4px 0 4px rgba(7, 32, 39, 0.1);" v-for="(gender, index) in data_clothes.generos" @click="navigateToCategoryView(gender.id)">
              <a class="nav-link font_title" href="#">{{ gender.genero }}</a>
            </li>
            <li class="nav-item d-flex px-3" style=" font-size: 40px; cursor: pointer; box-shadow: -4px 0 4px rgba(7, 32, 39, 0.1), 4px 0 4px rgba(7, 32, 39, 0.1);" @click="navigateToCategoryView_Sale('on_sale')">
              <a class="nav-link font_title">ON SALE</a>
            </li>
            <li class="nav-item d-flex px-3" style="font-size: 40px; box-shadow: -4px 0 4px rgba(7, 32, 39, 0.1), 4px 0 4px rgba(7, 32, 39, 0.1);">
              <a class="nav-link font_title">DESTACADOS</a>
            </li>
            <li class="nav-item d-flex px-3" style="font-size: 40px; box-shadow: -4px 0 4px rgba(7, 32, 39, 0.1), 4px 0 4px rgba(7, 32, 39, 0.1);">
              <a class="nav-link font_title">¡DESCÚBRENOS!</a>
            </li>
          </ul>
        </div>
      </nav>
    </div>

</template>


<style scoped>

.navbar-brand img {
    width: 170px; 
    height: auto; 
}
  .navbar-nav {
    display: flex;
    justify-content: space-between;
    flex-basis: 100%;
    margin-right: -10px; /* Márgenes negativos para ajustar los símbolos | */
  }

  /* Agregar el símbolo | */
  .navbar-nav .nav-item {
    display: inline-block;
    justify-content: center;
    padding-right: 0px; /* Espacio para evitar que el símbolo se superponga con el texto */
  }


</style>


  
<script>
import { ref, inject, onMounted, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default {
  setup() {
    const data_clothes = inject('$data_clothes');
    const isNavbarFixed = ref(false);

    const handleScroll = () => {
      isNavbarFixed.value = window.pageYOffset > 0;
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
    });

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll);
    });

    const route = useRoute();
    const router = useRouter();

    const navigateToCategoryView = (genderId) => {
      // Agregar el prefijo "gen_" antes de pasar el identificador de género como parámetro de ruta
      const genderIdWithPrefix = 'gen_' + genderId;
      router.push({ name: 'Catalog', params: { categoryId: genderIdWithPrefix } });
    };

    const navigateToCategoryView_Sale = (param) => {
      router.push({ name: 'Catalog', params: { categoryId: param }});
    };

    const back_home = () => {
      router.push({ name: 'Home' });
    }

    return {
      data_clothes,
      isNavbarFixed,
      navigateToCategoryView,
      back_home,
      navigateToCategoryView_Sale,
    };
  },
};
</script>
