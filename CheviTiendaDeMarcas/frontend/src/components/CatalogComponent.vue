<template>
    <div class="container-fluid py-5" style="overflow: hidden;">
        <div class="row">
            <div class="col-2 px-0">
                <h5 class="ps-4 mt-1 mb-4 font_title titles_general" style="font-size: 50px;">Filtros:</h5>
                <div class="ps-5">
                  <div class="dropdown mt-3">
                      <button class="btn text-white dropdown-toggle font_title titles_general" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="font-size: 20px;background-color: #072027;">
                          Categorías
                      </button>
                      <ul class="dropdown-menu" style="background-color: #F8FBE6;">
                          <li v-for="(category, index) in categories" :key="index"><a class="dropdown-item font_description" style="font-size: 20px;" href="#" @click="filterProducts(`cat_${category.id}`)">{{category.categoria_nombre_en_pantalla}}</a></li>
                      </ul>
                  </div>

                    <div class="dropdown mt-3">
                        <button class="btn text-white dropdown-toggle font_title titles_general" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="font-size: 20px; background-color: #072027;">
                            Género
                        </button>
                        <ul class="dropdown-menu" style="background-color: #F8FBE6;">
                            <li v-for="(gender, index) in genders" :key="index"><a class="dropdown-item font_description" style="font-size: 20px;" href="#" @click="filterProducts(`gen_${gender.id}`)">{{ gender.genero }}</a></li>
                        </ul>
                    </div>


                    <div class=" mt-3">
                        <button class="btn text-white font_title titles_general" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="font-size: 20px; background-color: #881A18;" @click="filterProducts(`on_sale`)">
                            ON SALE
                        </button>
                    </div>

                </div>
            </div>

            <div class="col-10 px-0">
                    <!--columnas imagenes-->
                    <div class="row p-2 g-3">
                        <div v-for="(product, index) in products_filtered" :key="index" class="col-3" @click="navigateToProductView(product.id)">
                            <div class="card border-0" style="background-color: transparent;overflow: hidden;border-radius: 0px;">
                                <img :src="`http://127.0.0.1:8000/media/${product.Foto_Principal}`" alt="" style="border-radius: 5px;height:300px;width: 100%; object-fit: cover;">
                                <div class="card-body">
                                    <h5 class="card-title text-center font_title " style="letter-spacing: 2.5px;font-size: 2rem">{{ product.titulo }}</h5>
                                    <p class="card-text text-center font_title" style="font-size: 1.8rem;">{{ product.precio }}</p>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                    
                    
            </div>
        </div>
        
    </div>
</template>

<script>
import { ref, inject, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default {
  setup() {
    const data_clothes = inject('$data_clothes');
    const categories = data_clothes.categorias;
    const genders = data_clothes.generos;
    const products = data_clothes.productos;
    const products_filtered = ref([]);

    const route = useRoute();

    // Función para filtrar productos por categoría o género
    const filterProducts = (categoryId) => {
      if (categoryId.startsWith('cat_')) {
        // Si es una categoría, filtramos por el ID de categoría sin el prefijo "cat_"
        const categoryIdWithoutPrefix = parseInt(categoryId.substring(4));
        products_filtered.value = products.filter(
          (product) => product.categoria_id === categoryIdWithoutPrefix
        );
      } else if (categoryId.startsWith('gen_')) {
        // Si es un género, filtramos por el ID de género sin el prefijo "gen_"
        const genderIdWithoutPrefix = parseInt(categoryId.substring(4));
        products_filtered.value = products.filter(
          (product) => product.genero_id === genderIdWithoutPrefix
        );
      } else if (categoryId === 'on_sale') {
        // Si el parámetro es "on_sale", filtramos los productos en oferta
        products_filtered.value = products.filter(
          (product) => product.on_sale === true
        );
      } else {
        // Si no coincide con ninguno de los prefijos anteriores, no aplicamos ningún filtro
        products_filtered.value = products;
      }
    };


    // Watch for changes in the categoryId parameter
    watch(() => route.params.categoryId, (newCategoryId) => {

      filterProducts(newCategoryId);
    });

    // Initial filter based on the current categoryId in the URL
    const categoryId_ = route.params.categoryId;

    filterProducts(categoryId_);

    const router = useRouter()
    const navigateToProductView = (productId) => {
      router.push({ name: 'Product', params: { productId: productId}});
    }

    return {
      categories,
      genders,
      products_filtered,
      filterProducts,
      navigateToProductView,
    };
  },
};
</script>
