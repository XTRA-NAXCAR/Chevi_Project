<template>
  <div class="container-fluid px-0">
    <div class="video-wrapper">
      <video ref="videoRef" :src="videoUrl" class="video-element" autoplay muted></video>
      <div class="video-caption container">
        <h2 class=" multimedia_title font_title" style="color: #881A19;">{{ videoContent.titulo }}</h2>
        <p class="text-white description_Multimedia font_title ">{{ videoContent.descripcion }}</p>    
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, inject, computed } from 'vue';

export default {
  setup() {
    const data = inject('$data_home');
    const videoRef = ref(null);
    const playVideo = () => {
      videoRef.value.play();
    };

    const restartVideo = () => {
      videoRef.value.currentTime = 0;
      videoRef.value.play();
    };

    onMounted(() => {
      videoRef.value.addEventListener('ended', restartVideo);
      playVideo(); // Reproducir el video automáticamente al montar el componente
    });

    const videoPath = data.Multimedia[0].video;
    const videoContent = data.Multimedia[0];

    const videoUrl = computed(() => {
      const baseUrl = window.location.origin; // Reemplaza con la URL de tu servidor Django
      return `http://127.0.0.1:8000//media/${videoPath}`;
    });

    return {
      videoRef,
      videoContent,
      restartVideo,
      videoUrl
    };
  }
};
</script>


  
  <style>
  .video-wrapper {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    overflow: hidden;
  }
  
  .video-element {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .video-caption {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    color: #fff;
  }
  
  .video-caption h2 {
    margin-bottom: 10px;
  }
  
  .video-caption p {
    margin-bottom: 20px;
  }

  @media (max-width: 580px) {
  .multimedia_title{
    font-size: 30px;
    padding-top: 110px;
    }

  }

  @media (min-width: 581px) and (max-width: 992px){
    .multimedia_title{
      font-size: 50px;
      margin-top: 30px;
    }
  }
  @media(min-width: 993px){
    .multimedia_title{
      font-size: 400px;
      letter-spacing: 20px;
    }
  }
  @media (max-width: 576px) {
  /* Estilos para pantallas más pequeñas (hasta 576px) */
  .description_Multimedia {
    font-size: 1rem; /* Tamaño de fuente para pantallas pequeñas */
  }
  .button_Multimedia{
    font-size: 1rem;
  }
  .video-wrapper{
    height: 400px;
  }
}

@media (min-width: 577px) and (max-width: 991px) {
  /* Estilos para pantallas de tamaño mediano (de 577px a 991px) */
  .description_Multimedia {
    font-size: 1.2rem; /* Tamaño de fuente para pantallas medianas */
  }
  .button_Multimedia{
    font-size: 1.1rem;
  }
  .video-wrapper{
    height: 600px;
  }
}

@media (min-width: 992px) {
  /* Estilos para pantallas más grandes (a partir de 992px) */
  .description_Multimedia {
    font-size: 4.5rem; /* Tamaño de fuente para pantallas grandes */
  }
  .button_Multimedia{
    font-size: 2.5rem;
  }
}
  </style>
