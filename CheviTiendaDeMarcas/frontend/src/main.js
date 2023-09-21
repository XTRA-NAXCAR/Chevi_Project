import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';
import axios from 'axios';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';

const app = createApp(App);

async function fetchData() {
  try {
    const response_clothes = await axios.get('http://127.0.0.1:8000/ropa/api/');
    const response_home = await axios.get('http://127.0.0.1:8000/home/api/');
    
    app.provide('$data_clothes', response_clothes.data);
    app.provide('$data_home', response_home.data);
    console.log(response_clothes.data)
    console.log(response_home.data)
    app.use(createPinia());
    app.use(router);
    
    app.mount('#app');
  } catch (error) {
    console.error(error);
  }
}

fetchData();

