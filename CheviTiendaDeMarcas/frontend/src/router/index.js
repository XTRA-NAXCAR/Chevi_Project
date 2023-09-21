import { createRouter, createWebHistory } from 'vue-router'
import  CatalogView  from '@/views/CatalogView.vue'
import HomeView from '@/views/HomeView.vue'
import ProductView from '@/views/ProductView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },

    {
      path: '/Catalog/:categoryId',
      name: 'Catalog',
      component: CatalogView
    },
    {
      path: '/Product/:productId',
      name: 'Product',
      component: ProductView
    }
  ]
})

export default router

