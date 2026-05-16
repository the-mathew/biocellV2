<template>
  <NuxtLayout name="dashboard">
    <div class="panel-header">
      <div class="header-text">
        <h2 class="panel-title">CENTRO DE <span class="highlight">VIDEOS - VERIFICADO</span></h2>
        <p class="panel-desc">explora nuestra videoteca científica y descubre el asombroso mundo celular.</p>
      </div>
      <div class="header-filters">
        <div class="search-box">
          <i class="mdi mdi-magnify"></i>
          <input type="text" placeholder="Buscar video...">
        </div>
        <div class="filter-btn" :class="{ active: contentFilter === 'Todos' }" @click="contentFilter = 'Todos'">Todos</div>
        <div class="filter-btn" :class="{ active: contentFilter === 'Teoría' }" @click="contentFilter = 'Teoría'">Teoría</div>
        <div class="filter-btn" :class="{ active: contentFilter === 'Práctica' }" @click="contentFilter = 'Práctica'">Práctica</div>
      </div>
    </div>

    <div class="video-grid" v-if="contentFilter !== 'Práctica'">
      <div v-for="video in videos" :key="video.id" class="video-card" @click="playVideo(video)">
        <div class="video-thumbnail">
          <img :src="`https://img.youtube.com/vi/${video.id}/hqdefault.jpg`" :alt="video.title" class="thumbnail-img">
          <div class="thumbnail-overlay">
            <div class="play-btn"><i class="mdi mdi-play"></i></div>
          </div>
          <div class="video-duration">{{ video.duration }}</div>
        </div>
        <div class="video-info">
          <div class="video-category">{{ video.category }}</div>
          <h4 class="video-title">{{ video.title }}</h4>
          <p class="video-desc">{{ video.desc }}</p>
          <div class="video-footer">
            <span class="video-views"><i class="mdi mdi-eye-outline"></i> {{ video.views }} vistas</span>
            <span class="video-date"><i class="mdi mdi-calendar-outline"></i> {{ video.date }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="practice-container" v-else>
      <InteractiveCells />
    </div>

    <!-- VIDEO MODAL -->
    <div v-if="activeVideo" class="video-modal-overlay" @click="closeVideo">
      <div class="video-modal-content" @click.stop>
        <div class="video-modal-header">
          <h3>{{ activeVideo.title }}</h3>
          <button class="icon-btn close-btn" @click="closeVideo"><i class="mdi mdi-close"></i></button>
        </div>
        <div class="video-modal-body">
          <iframe
            width="100%"
            height="450"
            :src="`https://www.youtube.com/embed/${activeVideo.id}?autoplay=1`"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
          </iframe>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue'

definePageMeta({ layout: false })

const contentFilter = ref('Todos')

const videos = [
  {
    id: 'pKkhJ5UaahQ',
    title: 'La Célula y sus Partes',
    category: 'General',
    duration: '07:44',
    views: '5.8M',
    date: 'Amoeba Sisters',
    desc: 'Descubre qué es la célula, cuáles son sus principales partes y las funciones vitales de nutrición, relación y reproducción.'
  },
  {
    id: 'sqgn1xolxpI',
    title: 'La Célula Animal y Vegetal',
    category: 'Comparativa',
    duration: '10:14',
    views: '3.2M',
    date: 'Khan Academy',
    desc: 'Animación detallada que compara los organelos exclusivos de la célula animal con los de la célula vegetal de forma interactiva.'
  },
  {
    id: 'yAGm4e4j0K8',
    title: 'Células Procariotas y Eucariotas',
    category: 'Clasificación',
    duration: '06:45',
    views: '2.1M',
    date: 'Khan Academy',
    desc: 'Aprende las diferencias entre células procariotas y eucariotas, y cómo se clasifican los seres vivos según su tipo celular.'
  },
  {
    id: 'fo6V3_MScxU',
    title: 'Los Organelos Celulares',
    category: 'Organelos',
    duration: '05:32',
    views: '1.5M',
    date: 'Biología',
    desc: 'Conoce en detalle cada organelo celular: mitocondria, retículo endoplasmático, ribosomas, aparato de Golgi y más.'
  }
]

const activeVideo = ref(null)
const playVideo = (video) => { activeVideo.value = video }
const closeVideo = () => { activeVideo.value = null }
</script>

<style scoped>
.panel-header {
  display: flex; justify-content: space-between; align-items: flex-end;
  margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid var(--border-color);
}
.panel-title { font-family: 'Orbitron', sans-serif; font-size: 32px; margin-bottom: 8px; }
.panel-title .highlight { color: var(--cyan); }
.panel-desc { color: var(--text-muted); font-size: 14px; }

.header-filters { display: flex; gap: 12px; align-items: center; }
.search-box {
  position: relative; background: var(--bg-card); border: 1px solid var(--border-color);
  border-radius: 8px; padding: 0 12px; display: flex; align-items: center; gap: 10px; height: 40px; width: 240px;
}
.search-box input { background: transparent; border: none; color: var(--text-main); font-size: 13px; width: 100%; outline: none; }

.filter-btn {
  padding: 8px 16px; background: var(--bg-card); border: 1px solid var(--border-color);
  border-radius: 8px; font-size: 13px; cursor: pointer; transition: all 0.2s ease; color: var(--text-muted);
}
.filter-btn:hover { border-color: var(--cyan); color: var(--cyan); }
.filter-btn.active { background: var(--cyan); color: var(--bg-main); font-weight: 700; border-color: var(--cyan); }

.video-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 24px; }

.video-card {
  background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px;
  overflow: hidden; transition: all 0.3s ease; cursor: pointer;
}
.video-card:hover { transform: translateY(-5px); border-color: var(--cyan); box-shadow: 0 10px 20px rgba(0,229,255,0.1); }

.video-thumbnail { position: relative; aspect-ratio: 16/9; background: #000; overflow: hidden; }
.thumbnail-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
.video-card:hover .thumbnail-img { transform: scale(1.05); }

.thumbnail-overlay {
  position: absolute; inset: 0; background: rgba(2, 11, 24, 0.4);
  display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s ease;
}
.video-card:hover .thumbnail-overlay { opacity: 1; }

.play-btn {
  width: 50px; height: 50px; background: var(--cyan); color: var(--bg-main);
  border-radius: 50%; display: flex; align-items: center; justify-content: center;
  font-size: 24px; transform: scale(0.8); transition: transform 0.3s ease;
}
.video-card:hover .play-btn { transform: scale(1); }

.video-duration { position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.8); color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600; }
.video-info { padding: 16px; }
.video-category { color: var(--cyan); font-size: 10px; text-transform: uppercase; font-weight: 700; letter-spacing: 1px; margin-bottom: 6px; }
.video-title { font-size: 15px; font-weight: 600; margin-bottom: 8px; line-height: 1.4; color: white; }
.video-desc { font-size: 12px; color: var(--text-muted); line-height: 1.4; margin-bottom: 16px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.video-footer { display: flex; justify-content: space-between; font-size: 11px; color: var(--text-muted); }

/* VIDEO MODAL */
.video-modal-overlay { position: fixed; inset: 0; background: rgba(2, 11, 24, 0.9); backdrop-filter: blur(5px); display: flex; align-items: center; justify-content: center; z-index: 100; }
.video-modal-content { background: var(--bg-card); border: 1px solid var(--cyan); border-radius: 16px; width: 90%; max-width: 800px; box-shadow: 0 0 30px rgba(0, 229, 255, 0.2); overflow: hidden; animation: modal-enter 0.3s ease-out; }
@keyframes modal-enter { from { opacity: 0; transform: scale(0.95) translateY(20px); } to { opacity: 1; transform: scale(1) translateY(0); } }
.video-modal-header { display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; border-bottom: 1px solid var(--border-color); background: rgba(0, 0, 0, 0.2); }
.video-modal-header h3 { font-size: 18px; color: var(--text-main); margin: 0; }
.icon-btn { background: var(--bg-card); border: 1px solid var(--border-color); color: var(--text-main); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.2s ease; }
.close-btn { color: #ff5252; border-color: rgba(255, 82, 82, 0.2); }
.close-btn:hover { background: rgba(255, 82, 82, 0.1); border-color: #ff5252; }
.video-modal-body { padding: 0; background: #000; }
</style>
