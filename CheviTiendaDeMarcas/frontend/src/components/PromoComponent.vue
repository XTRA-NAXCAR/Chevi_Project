<template>
    <div class="container-flex py-5" style="overflow: hidden;">
        <h5 class="text-center pb-5 my-5 titles_general font_title">-Más Vendidos-</h5>


    <swiper
        :slidesPerView="3"
        :slidesPerViewSkip="2"
        :spaceBetween="20"
        :navigation="true"
        :modules="modules"
        
        class="mySwiper px-4"
        style="overflow: hidden;"
    >
        <swiper-slide v-for="(product, index) in products_filtered" :key="index" class="card h-100 border-0 bg-transparent" @click="navigateToProductView(product.id)">

                <div class="images">
                    <img :src="`http://127.0.0.1:8000/media/${product.Foto_Principal}`" alt="" >
                </div>
                <div class="card-body pt-1">
                    <p class="card-title  mb-1 font_title" style="letter-spacing: 2.5px;font-size: 2rem">{{ product.titulo }}</p>
                    <p class="card-text font_title" style="font-size: 1.8rem;">{{ product.precio }}</p>
                </div>

        </swiper-slide>

    </swiper>
    </div>
</template>
<script>
    
    import { Swiper, SwiperSlide } from 'swiper/vue';
    
    import 'swiper/css';
    import 'swiper/css/pagination';

    import { Navigation } from 'swiper/modules';

    import { ref, inject, onMounted} from 'vue';
    import { useRouter } from 'vue-router';

    export default {
        components: {
            Swiper,
            SwiperSlide,
        },
        setup() {
            const data_clothes = inject('$data_clothes');
            const data_home = inject('$data_home');

            const id_product = data_home.Novedade;
            const products = data_clothes.productos;
            const products_filtered = ref([]);

            const filter_products = () => {
            products_filtered.value = [];
            
            for (const product_id of id_product) {
                const filtered = products.filter((product) => product.id === product_id.producto_id);
                products_filtered.value = [...products_filtered.value, ...filtered];
            }
            };

            filter_products();
            const router = useRouter()
            const navigateToProductView = (productId) => {
            router.push({ name: 'Product', params: { productId: productId}});
            }

            return {
                products_filtered,
                navigateToProductView,
                modules: [Navigation],
            };
        },
    };
</script>

<style scoped>
.images {
    width: 100%;
    height: 500px;
    align-items: center ;
    object-fit: cover;
}

body {
  position: relative;
  height: 100%;
}

body {
  background: #eee;
  font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
  font-size: 14px;
  color: #000;
  margin: 0;
  padding: 0;
}

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;

  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>