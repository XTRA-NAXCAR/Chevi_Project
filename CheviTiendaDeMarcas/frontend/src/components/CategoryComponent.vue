<template>
    <div class="container-fluid p-5" style="overflow: hidden;">
        <div class="row row-cols-2" >
            <div v-for="(product, index) in products_filtered" :key="index" class="col" @click="navigateToCategoryView(product.id)" style="cursor: pointer;">
                <div class="card border-0 mb-4">
                    <div>
                        <img :src="`http://127.0.0.1:8000/media/${product.imagen}`" alt="" style="width: 100%;max-height: 320px;object-fit: cover">
                    </div>
                    <div class="d-flex align-items-center justify-content-center" style="background-color: rgba(136, 26, 25, 0.3);position: absolute;width: 100%;height: 100%;">
                        <h1 class="category titles_general font_title" style="font-size: 120px;">{{ product.categoria_nombre_en_pantalla }}</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { ref, inject } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default {
  setup() {
    const data_clothes = inject('$data_clothes');
    const data_home = inject('$data_home');

    const id_product = data_home.Categoria;
    const products = data_clothes.categorias;
    const products_filtered = ref([]);

    const filter_products = () => {
      products_filtered.value = [];

      for (const product_id of id_product) {
        const filtered = products.filter((product) => product.id === product_id.categoria_id);
        products_filtered.value = [...products_filtered.value, ...filtered];
      }
    };

    filter_products();

    const route = useRoute();
    const router = useRouter();

    const navigateToCategoryView = (categoryId) => {
      // Agregar el prefijo "cat_" antes de pasar el identificador de categoría como parámetro de ruta
      const categoryIdWithPrefix = 'cat_' + categoryId;
      router.push({ name: 'Catalog', params: { categoryId: categoryIdWithPrefix } });
    };

    return {
      products_filtered,
      navigateToCategoryView
    };
  }
}
</script>


<style scoped>
.category {
    font-size: 60px; color: #F8FBE6;
}
</style>
