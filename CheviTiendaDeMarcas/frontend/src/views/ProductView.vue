<template>
    <NavbarComponent></NavbarComponent>
    <div style="height: 150px;"></div>
    <ProductComponent></ProductComponent>
    <PromoComponent></PromoComponent>
    <FooterComponent></FooterComponent>
</template>
<script>
    import NavbarComponent from '../components/NavbarComponent.vue';
    import ProductComponent from '../components/ProductComponent.vue';
    import PromoComponent from '../components/PromoComponent.vue';
    import FooterComponent from '../components/FooterComponent.vue';
    
    import { onMounted } from 'vue';

export default {
    components: {
        NavbarComponent,
        ProductComponent,
        PromoComponent,
        FooterComponent,
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