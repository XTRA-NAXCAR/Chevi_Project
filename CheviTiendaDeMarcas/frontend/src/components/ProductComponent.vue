<template>
    <div class="container-fluid mb-5 mt-5">
        

    
        <div class="row d-flex justify-content-center">
            <div class="col-10">
                <div class="row g-5">
                    

                    <div class="col-7">
                            <swiper :navigation="true"
                            :modules="modules"
                            class="mySwiper2"
                            style="height: 750px;">
                                <swiper-slide class="d-flex align-items-center justify-content-center">
                                    <div class="" style="overflow: hidden; width: 100%;">
                                        <img :src="`http://127.0.0.1:8000/media/${product.Foto_Principal}`" alt="" style="width: 100%;height: 100%;object-fit: cover;">
                                    </div>
                                </swiper-slide>
                                <swiper-slide class="d-flex align-items-center justify-content-center" v-for="pic in picture">
                                    <div class="" style="overflow: hidden; width: 100%;">
                                        <img :src="`http://127.0.0.1:8000/media/${pic.imagen}`" alt="" style="width: 100%;height: 100%;object-fit: cover;">
                                    </div>
                                </swiper-slide>
                            </swiper>
                    </div>
                    <div class="col-5 ps-5 pe-0">
                        <p class="mt-1 pb-2 mb-0 font_title" style="font-size: 31px; letter-spacing: 2px ;">{{ product.titulo }}</p>
                        
                        <div 
                        class="pb-3 font_description" 
                        style="
                            font-size: 20px; 
                            letter-spacing: 1px; 
                            text-align: justify;
                            max-width: 100%; /* Puedes ajustar el ancho máximo según tus preferencias */
                            word-wrap: break-word; /* Ajustar el texto al ancho de la caja y permitir quiebre de palabras */
                            white-space: pre-line; /* Respetar los saltos de línea */"
                            >
                            {{ product.descripcion }}
                        </div>
                   
                        <p class=" pb-2 font_title" style="font-size: 37px; letter-spacing: 1px;">{{ product.precio }}</p>
                        <p>
                            <div class="font_title" style="font-size: 25px;">
                                Tallas:
                            </div>
                            <div>
                                <a class="btn font_description" v-for="size in sizes">{{ size.nombre }}</a>
                            </div>
                        </p>
                        <p class="mt pb-2 font_title" style="font-size: 24px;">Stock disponible</p>
                        
                        <button class="d-flex pt-2 pb-3 px-5 mb-5" style="border-radius: 40px; border-width: 0px ;background-color:#0CC243">
                            <p class="mx-3 mb-0" style=";font-size: 40px;color: white;"><i class="bi bi-whatsapp me-3" style="font-size: 38px;"></i>Realizar Pedido</p> 
                        </button>

                        <div class="accordion" id="accordionPanelsStayOpenExample" style="border-radius: 25px;">
                            <div class="accordion-item" style="border-radius: 25px; border: 5px solid #072027;">
                                <h2 class="accordion-header" >
                                    <button class="accordion-button font_title" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne" style=" font-size: 25px;border-radius: 25px; background-color: #F8FBE6;">
                                        Especificaciones:
                                    </button>
                                </h2>
                                <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show" style="border-radius: 25px; ">
                                    <div class="accordion-body" style="background-color: #F8FBE6;border-radius: 25px; " >
                                        <div 
                                        class="pb-3 font_description" 
                                        style="
                                            font-size: 20px; 
                                            letter-spacing: 1px; 
                                            text-align: justify;
                                            max-width: 100%; /* Puedes ajustar el ancho máximo según tus preferencias */
                                            word-wrap: break-word; /* Ajustar el texto al ancho de la caja y permitir quiebre de palabras */
                                            white-space: pre-line; /* Respetar los saltos de línea */"
                                            >
                                            {{ product.especificacion }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>   
        </div> 
    </div>
</template>

<script>
    // Import Swiper Vue.js components
    import { Swiper, SwiperSlide } from 'swiper/vue';

    // Import Swiper styles
    import 'swiper/css';

    import 'swiper/css/navigation';


    // import required modules
    import { Navigation } from 'swiper/modules';
    import { inject, ref, computed } from 'vue';

    import { useRoute } from 'vue-router';

    export default {
        components: {
            Swiper,
            SwiperSlide,
        },
        setup() {
            const data_clothes = inject('$data_clothes')
            const products = data_clothes.productos
            const pictures = data_clothes.fotosProductos

            const route = useRoute();
            const productId = parseInt(route.params.productId);

            const product = computed(() => {
                return products.find((product) => product.id === productId);
            });


            const picture = computed(() => {
                return pictures.filter((picture) => picture.producto_id === product.value.id)
            })

            const sizes = data_clothes.tallas


            return {
                product,
                sizes,
                picture,
                modules: [Navigation],
        };
        },
    };
</script>

<style>

</style>