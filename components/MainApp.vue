<template>
  <div class="dashboard-wrapper">

    <aside class="sidebar" :class="{ 'is-closed': !isSidebarOpen }">
      <div class="sidebar-header">
        <div class="sidebar-logo-container">
          <div class="logo-icon">
            <i class="mdi mdi-dna"></i>
          </div>
          <div class="logo-tagline">Viaje al Interior de la Célula</div>
        </div>
      </div>

      <nav class="sidebar-nav">
        <a href="#" class="nav-item" :class="{ active: currentView === 'inicio' }" @click.prevent="currentView = 'inicio'">
          <i class="mdi mdi-home"></i> Inicio
        </a>
        <a href="#" class="nav-item" :class="{ active: currentView === 'contenido' }" @click.prevent="currentView = 'contenido'">
          <i class="mdi mdi-microscope"></i> Contenido
        </a>
        <a href="#" class="nav-item" :class="{ active: currentView === 'actividades' }" @click.prevent="currentView = 'actividades'">
          <i class="mdi mdi-gamepad-variant"></i> Actividades
        </a>
        <a href="#" class="nav-item" :class="{ active: currentView === 'recursos' }" @click.prevent="currentView = 'recursos'">
          <i class="mdi mdi-flask-outline"></i> Recursos
        </a>
        <a href="#" class="nav-item" :class="{ active: currentView === 'evaluaciones' }" @click.prevent="currentView = 'evaluaciones'">
          <i class="mdi mdi-clipboard-check-outline"></i> Evaluaciones
        </a>
        <a href="#" class="nav-item" :class="{ active: currentView === 'creditos' }" @click.prevent="currentView = 'creditos'">
          <i class="mdi mdi-information-outline"></i> Creditos
        </a>
      </nav>
    </aside>


    <main class="main-content">
      

      <header class="topbar">
        <div class="topbar-left">
          <button class="icon-btn menu-toggle" @click="isSidebarOpen = !isSidebarOpen">
            <i class="mdi mdi-menu"></i>
          </button>
          
          <div class="topbar-info">
            <div class="welcome-container">
              <h1>¡Bienvenido, <span class="highlight">{{ userName || 'Explorador' }}</span>! <i class="mdi mdi-hand-wave-outline greeting-icon"></i></h1>
              <p class="tagline">¿Listo para descubrir los secretos de la célula?</p>
            </div>
            
            <div class="divider"></div>
            
            <div class="header-status">
              <div class="mini-logo">
                <i class="mdi mdi-dna"></i>
                <span>BioCell</span>
                <span class="badge-ova">OVA</span>
              </div>
              <span class="status-item"><i class="mdi mdi-microscope"></i> Laboratorio</span>
              <span class="status-item"><i class="mdi mdi-molecule"></i> Bio-Exploración</span>
            </div>
          </div>
        </div>
        <div class="topbar-actions">
          <div class="points-badge">
            <i class="mdi mdi-star"></i> 120 pts
          </div>
          <button class="icon-btn">
            <i class="mdi mdi-bell"></i>
            <span class="badge">3</span>
          </button>
          <div class="user-profile">
            <div class="avatar">
               <i class="mdi mdi-account"></i>
            </div>
            <div class="user-info">
              <span class="user-name">{{ userName || 'Explorador' }}</span>
              <span class="user-level">Nivel 3</span>
            </div>
          </div>
          <button class="btn-exit" @click="$emit('back')" title="Salir al menú principal">
            <i class="mdi mdi-logout"></i>
          </button>
        </div>
      </header>

      <div class="content-scroll">
        <!-- VISTA: INICIO (DASHBOARD) -->
        <template v-if="currentView === 'inicio'">
          <!-- HERO BANNER -->
          <section class="hero-banner">
            <div class="hero-text">
              <h2 class="hero-title"><span class="title-bio">Bio</span><span class="title-cell">Cell</span></h2>
              <div class="hero-subtitle">Viaje al Interior de la Célula</div>
              <p class="hero-desc">Explora, aprende y diviértete descubriendo la unidad básica de la vida.</p>
              <button class="btn-primary" @click="currentView = 'contenido'">
                <i class="mdi mdi-rocket-launch-outline" style="font-size: 18px"></i> Comenzar aventura <i class="mdi mdi-arrow-right"></i>
              </button>
            </div>
            
            <div class="hero-image">
              <div class="cell-illustration">
                <svg width="220" height="220" viewBox="0 0 100 100">
                  <circle cx="50" cy="50" r="46" fill="rgba(0,229,255,0.05)" stroke="rgba(0,229,255,0.4)" stroke-width="1.5" stroke-dasharray="4 3"/>
                  <circle cx="50" cy="50" r="38" fill="rgba(0,191,165,0.1)" stroke="rgba(0,191,165,0.3)" stroke-width="1"/>
                  <circle cx="50" cy="50" r="20" fill="rgba(118,255,3,0.15)" stroke="rgba(118,255,3,0.5)" stroke-width="1.5"/>
                  <circle cx="50" cy="50" r="8" fill="rgba(118,255,3,0.6)"/>
                  <ellipse cx="28" cy="38" rx="8" ry="4" fill="rgba(0,229,255,0.3)" stroke="rgba(0,229,255,0.6)" stroke-width="1" transform="rotate(-30,28,38)"/>
                  <ellipse cx="72" cy="62" rx="8" ry="4" fill="rgba(0,229,255,0.3)" stroke="rgba(0,229,255,0.6)" stroke-width="1" transform="rotate(145,72,62)"/>
                </svg>

                <div class="callout callout-1">
                   <div class="callout-box">
                     <h5><i class="mdi mdi-nucleus"></i> Núcleo</h5>
                     <p>Controla las actividades celulares.</p>
                   </div>
                </div>
                <div class="callout callout-2">
                   <div class="callout-box">
                     <h5><i class="mdi mdi-flash"></i> Mitocondria</h5>
                     <p>Produce la energía celular.</p>
                   </div>
                </div>
                <div class="callout callout-3">
                   <div class="callout-box">
                     <h5><i class="mdi mdi-shield-outline"></i> Membrana</h5>
                     <p>Protege y regula entrada/salida.</p>
                   </div>
                </div>
              </div>
            </div>
          </section>

          <div class="dashboard-grid">
            <div class="quick-actions-col">
              <h3 class="section-title">¿Qué quieres hacer hoy?</h3>
              <div class="actions-grid">
                
                <div class="action-card card-explore" @click="currentView = 'contenido'">
                  <div class="action-icon"><i class="mdi mdi-microscope"></i></div>
                  <h4>Contenido</h4>
                  <p>Descubre los tipos de células y sus partes.</p>
                  <div class="action-arrow"><i class="mdi mdi-arrow-right"></i></div>
                </div>

                <div class="action-card card-activities" @click="currentView = 'actividades'">
                  <div class="action-icon"><i class="mdi mdi-gamepad-variant"></i></div>
                  <h4>Actividades</h4>
                  <p>Aprende jugando con retos interactivos.</p>
                  <div class="action-arrow"><i class="mdi mdi-arrow-right"></i></div>
                </div>

                <div class="action-card card-lab" @click="currentView = 'recursos'">
                  <div class="action-icon"><i class="mdi mdi-flask-outline"></i></div>
                  <h4>Recursos</h4>
                  <p>Accede a material de apoyo y herramientas.</p>
                  <div class="action-arrow"><i class="mdi mdi-arrow-right"></i></div>
                </div>

                <div class="action-card card-challenges" @click="currentView = 'evaluaciones'">
                  <div class="action-icon"><i class="mdi mdi-clipboard-check-outline"></i></div>
                  <h4>Evaluaciones</h4>
                  <p>Pon a prueba tus conocimientos adquiridos.</p>
                  <div class="action-arrow"><i class="mdi mdi-arrow-right"></i></div>
                </div>
              </div>

              <div class="progress-section">
                <span class="progress-label">Sigue tu progreso</span>
                <div class="progress-track">
                  <div class="progress-fill" style="width: 60%"></div>
                </div>
                <span class="progress-percent">60%</span>
              </div>
            </div>

            <div class="mission-col">
              <h3 class="section-title">Tu misión actual</h3>
              <div class="mission-card">
                <div class="mission-icon">
                   <i class="mdi mdi-target"></i>
                </div>
                <h4 class="mission-title">Misión 2: Organelos</h4>
                <p class="mission-desc">Conoce las estructuras que hacen posible la vida celular.</p>
                <div class="mission-stats">
                  <span class="mission-steps">3/5 actividades</span>
                  <div class="progress-track small">
                    <div class="progress-fill" style="width: 60%"></div>
                  </div>
                </div>
                <button class="btn-secondary">
                  <i class="mdi mdi-play-circle-outline" style="font-size: 18px"></i> Continuar misión <i class="mdi mdi-arrow-right"></i>
                </button>
              </div>
            </div>
          </div>

          <section class="trivia-row">
            <h3 class="section-title">Datos curiosos</h3>
            <div class="trivia-grid">
              <div class="trivia-card">
                <i class="mdi mdi-microscope"></i>
                <p>Las células pueden ser 10-30 micras de tamaño.</p>
              </div>
              <div class="trivia-card">
                <i class="mdi mdi-dna"></i>
                <p>Todas las células contienen material genético (ADN).</p>
              </div>
              <div class="trivia-card">
                <i class="mdi mdi-flash"></i>
                <p>Las mitocondrias son las "centrales eléctricas" de la célula.</p>
              </div>
              <div class="trivia-card">
                <i class="mdi mdi-leaf"></i>
                <p>Las células vegetales tienen cloroplastos para realizar fotosíntesis.</p>
              </div>
            </div>
          </section>
        </template>

        <!-- VISTA: CONTENIDO (VIDEOTECA) -->
        <template v-else-if="currentView === 'contenido'">
          <div class="panel-header">
            <div class="header-text">
              <h2 class="panel-title">Centro de <span class="highlight">Contenidos</span></h2>
              <p class="panel-desc">Explora nuestra videoteca científica y descubre el asombroso mundo celular.</p>
            </div>
            <div class="header-filters">
              <div class="search-box">
                <i class="mdi mdi-magnify"></i>
                <input type="text" placeholder="Buscar video...">
              </div>
              <div class="filter-btn" :class="{ active: contentFilter === 'Todos' }" @click="setFilter('Todos')">Todos</div>
              <div class="filter-btn" :class="{ active: contentFilter === 'Teoría' }" @click="setFilter('Teoría')">Teoría</div>
              <div class="filter-btn" :class="{ active: contentFilter === 'Práctica' }" @click="setFilter('Práctica')">Práctica</div>
            </div>
          </div>

          <div class="video-grid" v-if="contentFilter !== 'Práctica'">
            <div v-for="video in videos" :key="video.id" class="video-card" @click="playVideo(video)">
              <div class="video-thumbnail">
                <img :src="`https://img.youtube.com/vi/${video.id}/maxresdefault.jpg`" :alt="video.title" class="thumbnail-img">
                <div class="thumbnail-overlay">
                  <div class="play-btn">
                    <i class="mdi mdi-play"></i>
                  </div>
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
        </template>

        <!-- PLACEHOLDER PARA OTRAS VISTAS (Actividades, Recursos, etc) -->
        <template v-else-if="currentView === 'actividades'">
          <div class="placeholder-view">
            <div class="placeholder-icon">
              <i class="mdi mdi-gamepad-variant-outline"></i>
            </div>
            <h2>Minijuegos en Desarrollo</h2>
            <p>El laboratorio interactivo ha sido movido a <b>Contenido > Práctica</b>. ¡Pronto añadiremos minijuegos aquí!</p>
            <button class="btn-primary" @click="currentView = 'contenido'; setFilter('Práctica')">Ir al Laboratorio</button>
          </div>
        </template>

        <!-- VISTA: CRÉDITOS -->
        <template v-else-if="currentView === 'creditos'">
          <div class="credits-container">
            <div class="credits-header">
              <h2 class="credits-title">Créditos</h2>
              <p class="credits-subtitle">Conoce el equipo detrás de BioCell OVA</p>
            </div>

            <div class="developers-grid">
              <div class="developer-card">
                <div class="card-image">
                  <img src="/images/Mateo ayala.jpeg" alt="Mateo Ayala" class="developer-photo">
                </div>
                <div class="card-content">
                  <h3 class="developer-name">Mateo Ayala</h3>
                  <p class="developer-role">Desarrollador</p>
                  <p class="developer-desc">Especialista en desarrollo web y diseño de interfaces interactivas.</p>
                </div>
              </div>

              <div class="developer-card">
                <div class="card-image">
                  <img src="/images/Maicol pereira.jpeg" alt="Maikol Pereira" class="developer-photo">
                </div>
                <div class="card-content">
                  <h3 class="developer-name">Maikol Pereira</h3>
                  <p class="developer-role">Desarrollador</p>
                  <p class="developer-desc">Experto en desarrollo de aplicaciones educativas y experiencias de usuario.</p>
                </div>
              </div>
            </div>

            <div class="credits-info">
              <div class="info-section">
                <h4><i class="mdi mdi-information-outline"></i> Acerca de BioCell OVA</h4>
                <p>BioCell es un Objeto Virtual de Aprendizaje (OVA) diseñado para hacer el aprendizaje de la biología celular interactivo, atractivo y accesible para estudiantes de todas las edades.</p>
              </div>
              <div class="info-section">
                <h4><i class="mdi mdi-lightbulb-outline"></i> Objetivo</h4>
                <p>Proporcionar una plataforma educativa moderna que permita a los estudiantes explorar, entender y aprender sobre los componentes y funciones de las células de manera lúdica y efectiva.</p>
              </div>
            </div>
          </div>
        </template>

        <!-- PLACEHOLDER PARA OTRAS VISTAS -->
        <template v-else>
          <div class="placeholder-view">
            <div class="placeholder-icon">
              <i class="mdi mdi-tools"></i>
            </div>
            <h2>Módulo en Desarrollo</h2>
            <p>Estamos trabajando para traerte el mejor contenido científico. ¡Vuelve pronto!</p>
            <button class="btn-primary" @click="currentView = 'inicio'">Volver al Inicio</button>
          </div>
        </template>
      </div>
    </main>

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
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({ userName: String })
defineEmits(['back'])

const isSidebarOpen = ref(true)
const currentView = ref('inicio')
const contentFilter = ref('Todos')

const setFilter = (filter) => {
  contentFilter.value = filter
}

const videos = [
  {
    id: 'bXphNRSOvEE',
    title: 'La Célula y sus Partes',
    category: 'General',
    duration: '06:30',
    views: '450k',
    date: 'El Gato Ilustrado',
    desc: 'Conceptos básicos sobre la célula, la teoría celular y la importancia de la unidad fundamental de la vida.'
  },
  {
    id: 'wqGuXyDmdv8',
    title: 'Biología: Célula y Organelos',
    category: 'Eucariotas',
    duration: '08:45',
    views: '320k',
    date: 'Ciencias Educativas',
    desc: 'Un recorrido detallado por la estructura de la célula eucariota y la función de sus componentes principales.'
  },
  {
    id: 'ELz0oH5D9Uo',
    title: 'Diferencias Animal y Vegetal',
    category: 'Comparativa',
    duration: '05:15',
    views: '800k',
    date: 'Ciencia Divertida',
    desc: 'Diferencias clave entre la célula animal y la célula vegetal, analizando sus organelos específicos de forma interactiva.'
  },
  {
    id: 'fD1s-6s7F0M',
    title: 'Viaje al Interior Celular',
    category: 'Exploración',
    duration: '07:20',
    views: '1.2M',
    date: 'Bio-Exploradores',
    desc: 'Animación en 3D sobre el funcionamiento interno de las células y cómo se transportan los nutrientes.'
  }
]

const activeVideo = ref(null)
const playVideo = (video) => {
  activeVideo.value = video
}
const closeVideo = () => {
  activeVideo.value = null
}
</script>

<style scoped>
/* ═══════════════════════════════════════════════
   VARIABLES GLOBALES (Mantenemos Dark Mode)
═══════════════════════════════════════════════ */
.dashboard-wrapper {
  --bg-main: #020b18;
  --bg-sidebar: #041224;
  --bg-card: #05182e;
  --bg-card-hover: #07213d;
  --cyan: #00e5ff;
  --teal: #00bfa5;
  --lime: #76ff03;
  --text-main: rgba(200, 240, 255, 0.9);
  --text-muted: rgba(200, 240, 255, 0.5);
  --border-color: rgba(0, 229, 255, 0.15);

  position: fixed;
  inset: 0;
  display: flex;
  background-color: var(--bg-main);
  color: var(--text-main);
  font-family: 'Exo 2', sans-serif;
  overflow: hidden;
}

/* ═══════════════════════════════════════════════
   SIDEBAR
═══════════════════════════════════════════════ */
.sidebar {
  width: 260px;
  background-color: var(--bg-sidebar);
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  padding: 24px 0;
  z-index: 10;
  transition: all 0.3s ease;
}

.sidebar.is-closed {
  width: 0;
  padding: 24px 0;
  border-right: none;
  opacity: 0;
  overflow: hidden;
}

.sidebar-header {
  padding: 0 24px 30px;
  border-bottom: 1px solid var(--border-color);
  margin-bottom: 20px;
  white-space: nowrap;
}

.sidebar-logo-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 10px;
}

.logo-icon {
  font-size: 54px;
  background: linear-gradient(135deg, var(--cyan), var(--lime));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 15px rgba(0, 229, 255, 0.6));
  display: flex;
  align-items: center;
  justify-content: center;
  animation: logo-pulse 4s ease-in-out infinite;
}

@keyframes logo-pulse {
  0%, 100% { filter: drop-shadow(0 0 15px rgba(0, 229, 255, 0.6)); transform: scale(1); }
  50% { filter: drop-shadow(0 0 25px rgba(118, 255, 3, 0.8)); transform: scale(1.1); }
}

.logo-tagline {
  font-size: 10px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 2px;
  max-width: 180px;
  line-height: 1.4;
}

.sidebar-nav {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 0 16px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.nav-item i {
  font-size: 20px;
}

.nav-item:hover, .nav-item.active {
  background: rgba(0, 229, 255, 0.1);
  color: var(--cyan);
}
.nav-item.active {
  background: linear-gradient(90deg, rgba(0,229,255,0.15) 0%, rgba(0,191,165,0.05) 100%);
  border-left: 3px solid var(--cyan);
}

.fixed-trivia {
  position: fixed;
  bottom: 24px;
  left: 20px;
  width: 220px;
  z-index: 20;
  transition: all 0.3s ease;
}

.sidebar-trivia {
  padding: 20px;
  background: linear-gradient(135deg, rgba(0,229,255,0.05), rgba(0,191,165,0.1));
  border: 1px solid rgba(0, 229, 255, 0.2);
  border-radius: 12px;
  text-align: center;
  backdrop-filter: blur(10px);
}

.trivia-icon {
  margin-bottom: 12px;
  animation: float 3s ease-in-out infinite alternate;
}

@keyframes float {
  from { transform: translateY(0); }
  to { transform: translateY(-5px); }
}

.sidebar-trivia h4 {
  color: var(--cyan);
  font-size: 12px;
  font-family: 'Orbitron', sans-serif;
  margin-bottom: 8px;
  letter-spacing: 1px;
}

.sidebar-trivia p {
  font-size: 11px;
  color: var(--text-main);
  line-height: 1.5;
}

/* ═══════════════════════════════════════════════
   MAIN CONTENT & TOPBAR
═══════════════════════════════════════════════ */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: radial-gradient(ellipse at top right, #04142a 0%, var(--bg-main) 70%);
  height: 100vh;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 30px;
  border-bottom: 1px solid var(--border-color);
  background: rgba(4, 18, 36, 0.5);
  backdrop-filter: blur(15px);
  z-index: 5;
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.topbar-info {
  display: flex;
  align-items: center;
  gap: 24px;
}

.welcome-container h1 {
  font-family: 'Orbitron', sans-serif;
  font-size: 20px;
  font-weight: 700;
  color: var(--text-main);
  margin: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.welcome-container .highlight {
  color: var(--cyan);
  text-shadow: 0 0 10px rgba(0, 229, 255, 0.3);
}

.tagline {
  font-size: 11px;
  color: var(--text-muted);
  margin: 2px 0 0 0;
}

.divider {
  width: 1px;
  height: 30px;
  background: var(--border-color);
}

.mini-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-right: 8px;
  color: var(--text-main);
  font-family: 'Orbitron', sans-serif;
  font-weight: 800;
  font-size: 14px;
}

.mini-logo i {
  color: var(--lime);
  font-size: 18px;
}

.badge-ova {
  background: var(--cyan);
  color: var(--bg-main);
  font-size: 9px;
  padding: 1px 4px;
  border-radius: 3px;
  font-weight: 900;
}

.header-status {
  display: flex;
  align-items: center;
  gap: 12px;
}

.status-item {
  font-size: 10px;
  color: var(--cyan);
  background: rgba(0, 229, 255, 0.05);
  padding: 4px 12px;
  border-radius: 6px;
  border: 1px solid rgba(0, 229, 255, 0.1);
  display: flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}

.topbar-actions {
  display: flex;
  align-items: center;
  gap: 20px;
}

.points-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(118, 255, 3, 0.1);
  border: 1px solid rgba(118, 255, 3, 0.3);
  color: var(--lime);
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.icon-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-main);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  cursor: pointer;
  transition: all 0.2s ease;
}

.icon-btn:hover {
  background: rgba(0, 229, 255, 0.1);
  border-color: var(--cyan);
}

.badge {
  position: absolute;
  top: -2px;
  right: -2px;
  background: #ff5252;
  color: white;
  font-size: 10px;
  font-weight: bold;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--bg-card);
  padding: 6px 16px 6px 6px;
  border-radius: 30px;
  border: 1px solid var(--border-color);
}

.avatar {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, var(--cyan), var(--teal));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--bg-main);
  font-size: 18px;
}

.user-info {
  display: flex;
  flex-direction: column;
}

.user-name {
  font-size: 13px;
  font-weight: 600;
}

.user-level {
  font-size: 11px;
  color: var(--cyan);
}

.btn-exit {
  background: transparent;
  border: none;
  color: var(--text-muted);
  font-size: 24px;
  cursor: pointer;
  transition: color 0.2s ease;
}
.btn-exit:hover {
  color: #ff5252;
}

.content-scroll {
  flex: 1;
  overflow-y: auto;
  padding: 30px 40px;
  display: flex;
  flex-direction: column;
  gap: 30px;
}

/* ═══════════════════════════════════════════════
   HERO BANNER
═══════════════════════════════════════════════ */
.hero-banner {
  background: linear-gradient(135deg, rgba(0,229,255,0.1) 0%, rgba(0,191,165,0.05) 100%);
  border: 1px solid rgba(0,229,255,0.2);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 50px 60px;
  position: relative;
}

.hero-text {
  max-width: 45%;
  z-index: 2;
}

.hero-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 48px;
  margin-bottom: 8px;
  line-height: 1;
}

.hero-subtitle {
  display: inline-block;
  background: rgba(0, 229, 255, 0.15);
  color: var(--cyan);
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 1px;
  margin-bottom: 20px;
  text-transform: uppercase;
}

.hero-desc {
  font-size: 15px;
  color: var(--text-main);
  line-height: 1.6;
  margin-bottom: 24px;
}

.btn-primary {
  background: linear-gradient(135deg, rgba(0,229,255,0.2), rgba(0,191,165,0.2));
  border: 1px solid var(--cyan);
  color: var(--cyan);
  padding: 12px 24px;
  border-radius: 6px;
  font-family: 'Orbitron', sans-serif;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 1px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  box-shadow: 0 0 15px rgba(0,229,255,0.1);
}

.btn-primary:hover {
  background: linear-gradient(135deg, rgba(0,229,255,0.3), rgba(0,191,165,0.3));
  box-shadow: 0 0 25px rgba(0,229,255,0.3);
  transform: translateY(-2px);
}

.hero-image {
  position: relative;
  width: 460px;
  height: 250px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cell-illustration {
  position: relative;
  animation: float 6s ease-in-out infinite alternate;
}

/* Callouts HUD style */
.callout {
  position: absolute;
  background: rgba(2, 11, 24, 0.85);
  border: 1px solid rgba(0, 229, 255, 0.3);
  padding: 12px;
  border-radius: 8px;
  width: 150px;
  backdrop-filter: blur(4px);
  z-index: 10;
}

.callout-box h5 {
  color: var(--cyan);
  font-size: 13px;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.callout-box p {
  font-size: 11px;
  color: var(--text-muted);
  line-height: 1.4;
}

.callout-1 { top: -10px; left: -10px; }
.callout-2 { bottom: -10px; left: 30px; }
.callout-3 { top: 50px; right: -30px; }

/* ═══════════════════════════════════════════════
   GRID (ACCIONES Y MISIÓN)
═══════════════════════════════════════════════ */
.dashboard-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 30px;
}

.section-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 20px;
  color: var(--text-main);
}

.actions-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 30px;
}

.action-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: all 0.3s ease;
  cursor: pointer;
  overflow: hidden;
}

.action-card:hover {
  transform: translateY(-4px);
  background: var(--bg-card-hover);
  border-color: var(--cyan);
  box-shadow: 0 10px 20px rgba(0,229,255,0.05);
}

.action-icon {
  font-size: 32px;
  margin-bottom: 16px;
}

.card-explore .action-icon { color: var(--cyan); text-shadow: 0 0 15px rgba(0,229,255,0.4); }
.card-activities .action-icon { color: var(--lime); text-shadow: 0 0 15px rgba(118,255,3,0.4); }
.card-lab .action-icon { color: #2979ff; text-shadow: 0 0 15px rgba(41,121,255,0.4); }
.card-challenges .action-icon { color: #ffd600; text-shadow: 0 0 15px rgba(255,214,0,0.4); }

.action-card h4 {
  font-size: 15px;
  margin-bottom: 8px;
  color: white;
}

.action-card p {
  font-size: 11px;
  color: var(--text-muted);
  line-height: 1.4;
  margin-bottom: 12px;
  flex: 1;
}

.action-arrow {
  align-self: flex-end;
  background: rgba(255,255,255,0.05);
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  color: var(--text-muted);
  transition: all 0.3s ease;
}

.action-card:hover .action-arrow {
  background: var(--cyan);
  color: var(--bg-main);
}

/* PROGRESS SECTION */
.progress-section {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 20px 24px;
  display: flex;
  align-items: center;
  gap: 20px;
}

.progress-label {
  font-size: 14px;
  font-weight: 500;
  white-space: nowrap;
}

.progress-track {
  flex: 1;
  height: 8px;
  background: rgba(255,255,255,0.05);
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--cyan), var(--lime));
  border-radius: 4px;
  box-shadow: 0 0 10px rgba(118,255,3,0.5);
}

.progress-percent {
  font-weight: 700;
  color: var(--lime);
}

/* MISSION CARD */
.mission-card {
  background: linear-gradient(180deg, var(--bg-card) 0%, rgba(2,11,24,0.5) 100%);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 30px;
  height: calc(100% - 44px);
  display: flex;
  flex-direction: column;
}

.mission-icon {
  width: 60px;
  height: 60px;
  background: rgba(0,229,255,0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  color: var(--cyan);
  margin-bottom: 20px;
}

.mission-title {
  font-size: 18px;
  color: var(--cyan);
  margin-bottom: 12px;
}

.mission-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.5;
  flex: 1;
}

.mission-stats {
  margin-bottom: 20px;
}

.mission-steps {
  display: block;
  font-size: 12px;
  color: var(--text-main);
  margin-bottom: 8px;
  text-align: right;
}

.progress-track.small {
  height: 4px;
}

.btn-secondary {
  background: var(--cyan);
  color: var(--bg-main);
  border: none;
  padding: 12px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 13px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.2s ease;
  width: 100%;
}

.btn-secondary:hover {
  background: var(--lime);
  transform: translateY(-2px);
}

/* ═══════════════════════════════════════════════
   TRIVIA ROW
═══════════════════════════════════════════════ */
.trivia-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.trivia-card {
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 12px;
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 16px;
}

.trivia-card i {
  font-size: 24px;
  color: var(--cyan);
  opacity: 0.7;
}

.trivia-card p {
  font-size: 11px;
  color: var(--text-muted);
  line-height: 1.4;
  margin: 0;
}

/* Estilos extra para la barra de desplazamiento */
.content-scroll::-webkit-scrollbar {
  width: 8px;
}
.content-scroll::-webkit-scrollbar-track {
  background: var(--bg-main);
}
.content-scroll::-webkit-scrollbar-thumb {
  background: rgba(0,229,255,0.2);
  border-radius: 4px;
}
.content-scroll::-webkit-scrollbar-thumb:hover {
  background: rgba(0,229,255,0.4);
}
/* ═══════════════════════════════════════════════
   CONTENIDO (VIDEOTECA)
═══════════════════════════════════════════════ */
.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-color);
}

.panel-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 32px;
  margin-bottom: 8px;
}

.panel-title .highlight {
  color: var(--cyan);
}

.panel-desc {
  color: var(--text-muted);
  font-size: 14px;
}

.header-filters {
  display: flex;
  gap: 12px;
  align-items: center;
}

.search-box {
  position: relative;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 0 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  height: 40px;
  width: 240px;
}

.search-box input {
  background: transparent;
  border: none;
  color: var(--text-main);
  font-size: 13px;
  width: 100%;
  outline: none;
}

.filter-btn {
  padding: 8px 16px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover {
  border-color: var(--cyan);
  color: var(--cyan);
}

.filter-btn.active {
  background: var(--cyan);
  color: var(--bg-main);
  font-weight: 700;
  border-color: var(--cyan);
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
}

.video-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
  cursor: pointer;
}

.video-card:hover {
  transform: translateY(-5px);
  border-color: var(--cyan);
  box-shadow: 0 10px 20px rgba(0,229,255,0.1);
}

.video-thumbnail {
  position: relative;
  aspect-ratio: 16/9;
  background: #000;
  overflow: hidden;
}

.thumbnail-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.video-card:hover .thumbnail-img {
  transform: scale(1.05);
}

.thumbnail-overlay {
  position: absolute;
  inset: 0;
  background: rgba(2, 11, 24, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.video-card:hover .thumbnail-overlay {
  opacity: 1;
}

.play-btn {
  width: 50px;
  height: 50px;
  background: var(--cyan);
  color: var(--bg-main);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  transform: scale(0.8);
  transition: transform 0.3s ease;
}

.video-card:hover .play-btn {
  transform: scale(1);
}

.video-duration {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 600;
}

.video-info {
  padding: 16px;
}

.video-category {
  color: var(--cyan);
  font-size: 10px;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 1px;
  margin-bottom: 6px;
}

.video-title {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 8px;
  line-height: 1.4;
  color: white;
}

.video-desc {
  font-size: 12px;
  color: var(--text-muted);
  line-height: 1.4;
  margin-bottom: 16px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.video-footer {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--text-muted);
}

/* ═══════════════════════════════════════════════
   PLACEHOLDER VIEW
═══════════════════════════════════════════════ */
.placeholder-view {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 60px;
  color: var(--text-muted);
}

.placeholder-icon {
  font-size: 80px;
  color: var(--border-color);
  margin-bottom: 24px;
}

.placeholder-view h2 {
  font-family: 'Orbitron', sans-serif;
  font-size: 24px;
  color: var(--text-main);
  margin-bottom: 12px;
}

.placeholder-view p {
  max-width: 400px;
  margin-bottom: 30px;
}

/* ═══════════════════════════════════════════════
   VIDEO MODAL
═══════════════════════════════════════════════ */
.video-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(2, 11, 24, 0.9);
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
}

.video-modal-content {
  background: var(--bg-card);
  border: 1px solid var(--cyan);
  border-radius: 16px;
  width: 90%;
  max-width: 800px;
  box-shadow: 0 0 30px rgba(0, 229, 255, 0.2);
  overflow: hidden;
  animation: modal-enter 0.3s ease-out;
}

@keyframes modal-enter {
  from { opacity: 0; transform: scale(0.95) translateY(20px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

.video-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  border-bottom: 1px solid var(--border-color);
  background: rgba(0, 0, 0, 0.2);
}

.video-modal-header h3 {
  font-size: 18px;
  color: var(--text-main);
  margin: 0;
}

.close-btn {
  color: #ff5252;
  border-color: rgba(255, 82, 82, 0.2);
}
.close-btn:hover {
  background: rgba(255, 82, 82, 0.1);
  border-color: #ff5252;
}

.video-modal-body {
  padding: 0;
  background: #000;
}

/* ═══════════════════════════════════════════════
   CRÉDITOS
═══════════════════════════════════════════════ */
.credits-container {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.credits-header {
  text-align: center;
  margin-bottom: 20px;
}

.credits-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 40px;
  color: var(--cyan);
  margin-bottom: 8px;
  text-shadow: 0 0 15px rgba(0, 229, 255, 0.3);
}

.credits-subtitle {
  font-size: 16px;
  color: var(--text-muted);
}

.developers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 20px;
}

.developer-card {
  background: linear-gradient(135deg, rgba(0,229,255,0.05), rgba(0,191,165,0.1));
  border: 1px solid rgba(0, 229, 255, 0.2);
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 15px rgba(0, 229, 255, 0.05);
}

.developer-card:hover {
  transform: translateY(-8px);
  border-color: var(--cyan);
  box-shadow: 0 12px 30px rgba(0, 229, 255, 0.15);
  background: linear-gradient(135deg, rgba(0,229,255,0.1), rgba(0,191,165,0.15));
}

.card-image {
  width: 100%;
  height: 280px;
  overflow: hidden;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
}

.developer-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.developer-card:hover .developer-photo {
  transform: scale(1.05);
}

.card-content {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.developer-name {
  font-size: 20px;
  font-weight: 700;
  color: var(--text-main);
  margin: 0;
}

.developer-role {
  font-size: 12px;
  color: var(--cyan);
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
  margin: 0;
}

.developer-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.5;
  margin: 0;
}

.credits-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  margin-top: 20px;
}

.info-section {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  transition: all 0.3s ease;
}

.info-section:hover {
  border-color: var(--cyan);
  background: var(--bg-card-hover);
}

.info-section h4 {
  font-size: 16px;
  color: var(--cyan);
  margin: 0 0 12px 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.info-section h4 i {
  font-size: 20px;
}

.info-section p {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.6;
  margin: 0;
}
</style>
