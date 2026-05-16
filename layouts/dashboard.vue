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
        <NuxtLink to="/dashboard" class="nav-item" active-class="active">
          <i class="mdi mdi-home"></i> Inicio
        </NuxtLink>
        <NuxtLink to="/contenido" class="nav-item" active-class="active">
          <i class="mdi mdi-microscope"></i> Contenido
        </NuxtLink>
        <NuxtLink to="/actividades" class="nav-item" active-class="active">
          <i class="mdi mdi-gamepad-variant"></i> Actividades
        </NuxtLink>
        <NuxtLink to="/recursos" class="nav-item" active-class="active">
          <i class="mdi mdi-flask-outline"></i> Recursos
        </NuxtLink>
        <NuxtLink to="/evaluaciones" class="nav-item" active-class="active">
          <i class="mdi mdi-clipboard-check-outline"></i> Evaluaciones
        </NuxtLink>
        <NuxtLink to="/creditos" class="nav-item" active-class="active">
          <i class="mdi mdi-information-outline"></i> Creditos
        </NuxtLink>
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
              <h1>¡Bienvenido, <span class="highlight">{{ userName }}</span>! <i class="mdi mdi-hand-wave-outline greeting-icon"></i></h1>
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
          <div class="progress-badge" title="Progreso del OVA">
            <i class="mdi mdi-chart-donut"></i> Progreso: {{ progressPercentage }}%
          </div>
          <div class="user-profile">
            <div class="avatar">
               <i class="mdi mdi-account"></i>
            </div>
            <div class="user-info">
              <span class="user-name">{{ userName }}</span>
              <span class="user-role">Explorador</span>
            </div>
          </div>
          <NuxtLink to="/" class="btn-exit" title="Salir al menú principal">
            <i class="mdi mdi-logout"></i>
          </NuxtLink>
        </div>
      </header>

      <div class="content-scroll">
        <slot />
      </div>

      <footer class="dashboard-footer">
        <div class="footer-content">
          <div class="footer-section footer-logo">
            <div class="university-logo">
              <img src="/images/logo unicordoba.png" alt="Universidad de Córdoba" class="logo-img">
            </div>
            <div class="footer-text">
              <p class="university-name">Universidad de Córdoba</p>
              <p class="program-name">Licenciatura en Informática</p>
            </div>
          </div>
          <div class="footer-divider"></div>
          <div class="footer-section footer-ova">
            <i class="mdi mdi-dna"></i>
            <div class="ova-info">
              <p class="ova-name">BioCell Explorer</p>
              <p class="ova-version">v1.0 · Objeto Virtual de Aprendizaje</p>
            </div>
          </div>
          <div class="footer-divider"></div>
          <div class="footer-section footer-copyright">
            <p class="copyright-text">© 2026 Todos los derechos reservados</p>
          </div>
        </div>
      </footer>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'

const route = useRoute()
const userName = computed(() => route.query.user || 'Explorador')
const isSidebarOpen = ref(true)

// Sistema de progreso funcional
const mainRoutes = ['/dashboard', '/contenido', '/actividades', '/recursos', '/evaluaciones']
const visitedPages = useState('visitedPages', () => [])

const updateProgress = () => {
  // Manejar el caso del path actual (evitar barras finales redundantes)
  const currentPath = route.path === '/' ? '/dashboard' : route.path
  
  // Buscar si la ruta actual hace parte de las rutas principales
  const matchedRoute = mainRoutes.find(r => currentPath.startsWith(r))
  
  if (matchedRoute && !visitedPages.value.includes(matchedRoute)) {
    visitedPages.value.push(matchedRoute)
  }
}

onMounted(() => {
  if (process.client) {
    const saved = localStorage.getItem('biocell_progress')
    if (saved) {
      try { visitedPages.value = JSON.parse(saved) } catch (e) {}
    }
  }
  updateProgress()
})

watch(() => route.path, () => {
  updateProgress()
  if (process.client) {
    localStorage.setItem('biocell_progress', JSON.stringify(visitedPages.value))
  }
})

const progressPercentage = computed(() => {
  return Math.round((visitedPages.value.length / mainRoutes.length) * 100)
})
</script>

<style scoped>
/* ═══════════════════════════════════════════════
   VARIABLES GLOBALES (Mantenemos Dark Mode)
═══════════════════════════════════════════════ */
.dashboard-wrapper {
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

.nav-item i { font-size: 20px; }

.nav-item:hover, .nav-item.active {
  background: rgba(0, 229, 255, 0.1);
  color: var(--cyan);
}
.nav-item.active {
  background: linear-gradient(90deg, rgba(0,229,255,0.15) 0%, rgba(0,191,165,0.05) 100%);
  border-left: 3px solid var(--cyan);
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

.topbar-left { display: flex; align-items: center; gap: 20px; }
.topbar-info { display: flex; align-items: center; gap: 24px; }

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

.tagline { font-size: 11px; color: var(--text-muted); margin: 2px 0 0 0; }

.divider { width: 1px; height: 30px; background: var(--border-color); }

.mini-logo {
  display: flex; align-items: center; gap: 8px; margin-right: 8px;
  color: var(--text-main); font-family: 'Orbitron', sans-serif; font-weight: 800; font-size: 14px;
}
.mini-logo i { color: var(--lime); font-size: 18px; }

.badge-ova { background: var(--cyan); color: var(--bg-main); font-size: 9px; padding: 1px 4px; border-radius: 3px; font-weight: 900; }

.header-status { display: flex; align-items: center; gap: 12px; }

.status-item {
  font-size: 10px; color: var(--cyan);
  background: rgba(0, 229, 255, 0.05); padding: 4px 12px; border-radius: 6px;
  border: 1px solid rgba(0, 229, 255, 0.1); display: flex; align-items: center; gap: 6px; white-space: nowrap;
}

.topbar-actions { display: flex; align-items: center; gap: 20px; }

.progress-badge {
  display: flex; align-items: center; gap: 6px;
  background: rgba(0, 229, 255, 0.1); border: 1px solid rgba(0, 229, 255, 0.3);
  color: var(--cyan); padding: 6px 12px; border-radius: 20px; font-size: 13px; font-weight: 600;
  box-shadow: 0 0 10px rgba(0,229,255,0.1);
}

.icon-btn {
  background: var(--bg-card); border: 1px solid var(--border-color); color: var(--text-main);
  width: 40px; height: 40px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  position: relative; cursor: pointer; transition: all 0.2s ease;
}
.icon-btn:hover { background: rgba(0, 229, 255, 0.1); border-color: var(--cyan); }

.badge {
  position: absolute; top: -2px; right: -2px; background: #ff5252; color: white;
  font-size: 10px; font-weight: bold; width: 16px; height: 16px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}

.user-profile {
  display: flex; align-items: center; gap: 12px; background: var(--bg-card);
  padding: 6px 16px 6px 6px; border-radius: 30px; border: 1px solid var(--border-color);
}

.avatar {
  width: 32px; height: 32px;
  background: linear-gradient(135deg, var(--cyan), var(--teal)); border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: var(--bg-main); font-size: 18px;
}

.user-info { display: flex; flex-direction: column; }
.user-name { font-size: 13px; font-weight: 600; }
.user-role { font-size: 11px; color: var(--cyan); text-transform: uppercase; letter-spacing: 0.5px; }

.btn-exit {
  background: transparent; border: none; color: var(--text-muted);
  font-size: 24px; cursor: pointer; transition: color 0.2s ease; text-decoration: none;
}
.btn-exit:hover { color: #ff5252; }

.content-scroll {
  flex: 1; overflow-y: auto; padding: 30px 40px;
  display: flex; flex-direction: column; gap: 30px;
}

.content-scroll::-webkit-scrollbar { width: 8px; }
.content-scroll::-webkit-scrollbar-track { background: var(--bg-main); }
.content-scroll::-webkit-scrollbar-thumb { background: rgba(0,229,255,0.2); border-radius: 4px; }
.content-scroll::-webkit-scrollbar-thumb:hover { background: rgba(0,229,255,0.4); }

/* ═══════════════════════════════════════════════
   FOOTER
═══════════════════════════════════════════════ */
.dashboard-footer {
  padding: 20px 30px;
  border-top: 1px solid var(--border-color);
  background: rgba(4, 18, 36, 0.5);
  backdrop-filter: blur(15px);
}

.footer-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  max-width: 100%;
  flex-wrap: wrap;
}

.footer-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.footer-logo {
  flex: 1;
  min-width: 250px;
}

.university-logo {
  font-size: 32px;
  color: var(--cyan);
  display: flex;
  align-items: center;
  text-shadow: 0 0 10px rgba(0, 229, 255, 0.4);
}

.logo-img {
  height: 40px;
  width: auto;
  object-fit: contain;
  filter: brightness(1.1);
}

.footer-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.university-name {
  font-family: 'Orbitron', sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: var(--text-main);
  margin: 0;
}

.program-name {
  font-size: 11px;
  color: var(--lime);
  letter-spacing: 0.5px;
  margin: 0;
  text-transform: uppercase;
}

.footer-divider {
  width: 1px;
  height: 40px;
  background: var(--border-color);
}

.footer-ova {
  flex: 1;
  min-width: 200px;
}

.footer-ova i {
  font-size: 28px;
  color: var(--lime);
  filter: drop-shadow(0 0 8px rgba(118, 255, 3, 0.4));
}

.ova-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.ova-name {
  font-family: 'Orbitron', sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: var(--text-main);
  margin: 0;
}

.ova-version {
  font-size: 11px;
  color: var(--text-muted);
  margin: 0;
  letter-spacing: 0.5px;
}

.footer-copyright {
  flex-shrink: 0;
}

.copyright-text {
  font-size: 11px;
  color: var(--text-muted);
  margin: 0;
  letter-spacing: 0.5px;
}

/* ═══════════════════════════════════════════════
   RESPONSIVE (MOBILE SUPPORT)
═══════════════════════════════════════════════ */
@media (max-width: 992px) {
  .dashboard-wrapper { flex-direction: column; }
  .sidebar { position: fixed; top: 0; left: 0; bottom: 0; transform: translateX(0); z-index: 1000; box-shadow: 2px 0 15px rgba(0,0,0,0.5); }
  .sidebar.is-closed { transform: translateX(-100%); width: 260px; padding: 24px 0; border-right: 1px solid var(--border-color); opacity: 1; }
  .main-content { height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
  .topbar { padding: 12px 20px; }
  .header-status { display: none; }
  .user-info { display: none; }
  .content-scroll { padding: 20px; overflow-y: auto; }
  .footer-content { flex-direction: column; gap: 16px; }
  .footer-divider { width: 100%; height: 1px; }
  .footer-logo, .footer-ova { min-width: 100%; }
}

@media (max-width: 600px) {
  .welcome-container h1 { font-size: 16px; }
  .tagline { display: none; }
  .divider { display: none; }
  .progress-badge { font-size: 11px; padding: 4px 8px; }
  .user-profile { padding: 4px; }
  .avatar { width: 28px; height: 28px; font-size: 16px; }
  .btn-exit { font-size: 20px; }
  .dashboard-footer { padding: 15px 20px; }
  .footer-section { gap: 8px; }
  .university-logo { font-size: 24px; }
  .footer-ova i { font-size: 20px; }
  .university-name, .ova-name { font-size: 12px; }
  .program-name, .ova-version, .copyright-text { font-size: 10px; }
}
</style>
