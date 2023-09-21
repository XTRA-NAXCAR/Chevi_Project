<template>
    <div class="container-flex my-5 pb-5 pt-2" style="overflow: hidden;">
        <h5 class="text-center mb-5 font_title titles_general">-Instagram-</h5>
        <div class="row row-cols-5 g-2">

            <div v-for="(post, index) in Instagram" :key="index" class="col">
                    <div class="card border-0">
                        <div>
                            <img :src="`http://127.0.0.1:8000/media/${post.imagen}`" alt="" class="image">
                        </div>
                    </div>
            </div>
            
            
        
        </div>
    </div>

</template>

<script>
import {ref, inject} from 'vue'

export default {
    setup(){
        const data_home = inject('$data_home')
        const Instagram = data_home.Instagram_post
        return {
            Instagram
        }
    }
}
</script>

<style scoped>
    .image{
        width: 100%;
        height: 19vw;
        object-fit: cover;
    }
</style>