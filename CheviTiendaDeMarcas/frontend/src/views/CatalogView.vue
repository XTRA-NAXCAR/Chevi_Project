<template>
    <NavbarComponent></NavbarComponent>
    <div style="height: 150px;"></div>
    <CatalogComponent></CatalogComponent>
    <FooterComponent></FooterComponent>

</template>

<script>
    import NavbarComponent from '../components/NavbarComponent.vue';
    import CatalogComponent from '../components/CatalogComponent.vue';
    import FooterComponent from '../components/FooterComponent.vue'
    
    import { onMounted } from 'vue';
    export default{
        components:{
            NavbarComponent,
            CatalogComponent, 
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
  }
</script>
