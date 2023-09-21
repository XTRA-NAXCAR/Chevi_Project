<template>
    <div class="container-fluid pt-4 pb-5 px-5">
        <h5 class="text-center pt-2 pb-5 my-5 titles_general font_title">-Nuestras marcas-</h5>
        <div class="row row-cols-3 row-cols-lg-5 justify-content-center pb-3" style="overflow: hidden; ">
            <div class="col" v-for="(brand, index) in brands">
                <card class="d-flex justify-content-center align-items-center" style="height: 200px;">
                    <img :src="`http://127.0.0.1:8000/media/${brand.imagen}`" class="px-4" alt="" style="width: 100%; object-fit: cover; ">
                </card>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, inject } from 'vue';

export default {
    setup() {
        const data_home = inject('$data_home')
        const brands = ref(data_home.Marcas)

        return {
            brands
        }
    }
}
</script>