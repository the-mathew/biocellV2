<template>
  <NuxtLayout name="dashboard">
    <!-- HERO BANNER -->
    <section class="hero-banner">
      <div class="hero-text">
        <h2 class="hero-title"><span class="title-bio">Bio</span><span class="title-cell">Cell</span></h2>
        <div class="hero-subtitle">Viaje al Interior de la Célula</div>
        <p class="hero-desc">Explora, aprende y diviértete descubriendo la unidad básica de la vida.</p>
        <NuxtLink :to="{ path: '/contenido', query: $route.query }" class="btn-primary">
          <i class="mdi mdi-rocket-launch-outline" style="font-size: 18px"></i> Comenzar aventura <i class="mdi mdi-arrow-right"></i>
        </NuxtLink>
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
          <div class="orbit-wrapper">
            <!-- Item 1: Núcleo -->
            <div class="orbit-item item-1">
              <div class="static-counter anti-1">
                <div class="callout">
                  <div class="callout-box">
                    <h5><i class="mdi mdi-nucleus"></i> Núcleo</h5>
                    <p>Centro de control y ADN.</p>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Item 2: Mitocondria -->
            <div class="orbit-item item-2">
              <div class="static-counter anti-2">
                <div class="callout">
                  <div class="callout-box">
                    <h5><i class="mdi mdi-flash"></i> Mitocondria</h5>
                    <p>Produce energía (ATP).</p>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Item 3: Membrana -->
            <div class="orbit-item item-3">
              <div class="static-counter anti-3">
                <div class="callout">
                  <div class="callout-box">
                    <h5><i class="mdi mdi-shield-outline"></i> Membrana</h5>
                    <p>Filtro protector celular.</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Item 4: Ribosomas -->
            <div class="orbit-item item-4">
              <div class="static-counter anti-4">
                <div class="callout">
                  <div class="callout-box">
                    <h5><i class="mdi mdi-dots-grid"></i> Ribosomas</h5>
                    <p>Sintetizan las proteínas.</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Item 5: Citoplasma -->
            <div class="orbit-item item-5">
              <div class="static-counter anti-5">
                <div class="callout">
                  <div class="callout-box">
                    <h5><i class="mdi mdi-water-outline"></i> Citoplasma</h5>
                    <p>Fluido de soporte celular.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="dashboard-grid">
      <div class="quick-actions-col">
        <h3 class="section-title">¿Qué quieres hacer hoy?</h3>
        <div class="actions-grid">
          <NuxtLink :to="{ path: '/contenido', query: $route.query }" class="action-card card-explore">
            <div class="action-icon"><i class="mdi mdi-microscope"></i></div>
            <h4>Contenido</h4>
            <p>Descubre los tipos de células y sus partes.</p>
            <div class="action-arrow"><i class="mdi mdi-arrow-right"></i></div>
          </NuxtLink>
          <NuxtLink :to="{ path: '/actividades', query: $route.query }" class="action-card card-activities">
            <div class="action-icon"><i class="mdi mdi-gamepad-variant"></i></div>
            <h4>Actividades</h4>
            <p>Aprende jugando con retos interactivos.</p>
            <div class="action-arrow"><i class="mdi mdi-arrow-right"></i></div>
          </NuxtLink>
          <NuxtLink :to="{ path: '/recursos', query: $route.query }" class="action-card card-lab">
            <div class="action-icon"><i class="mdi mdi-flask-outline"></i></div>
            <h4>Recursos</h4>
            <p>Accede a material de apoyo y herramientas.</p>
            <div class="action-arrow"><i class="mdi mdi-arrow-right"></i></div>
          </NuxtLink>
          <NuxtLink :to="{ path: '/evaluaciones', query: $route.query }" class="action-card card-challenges">
            <div class="action-icon"><i class="mdi mdi-clipboard-check-outline"></i></div>
            <h4>Evaluaciones</h4>
            <p>Pon a prueba tus conocimientos adquiridos.</p>
            <div class="action-arrow"><i class="mdi mdi-arrow-right"></i></div>
          </NuxtLink>
        </div>

        <div class="progress-section">
          <span class="progress-label">Sigue tu progreso</span>
          <div class="progress-track">
            <div class="progress-fill" :style="{ width: `${progressPercent}%` }"></div>
          </div>
          <span class="progress-percent">{{ progressPercent }}%</span>
        </div>
      </div>

      <div class="mission-col">
        <h3 class="section-title">Tu misión actual</h3>
        <div class="mission-card">
          <div class="mission-icon"><i class="mdi" :class="currentMission.icon"></i></div>
          <h4 class="mission-title">{{ currentMission.title }}</h4>
          <p class="mission-desc">{{ currentMission.desc }}</p>
          <div class="mission-stats">
            <span class="mission-steps">{{ completedMissions }}/{{ totalMissions }} secciones completadas</span>
            <div class="progress-track small">
              <div class="progress-fill" :style="{ width: `${progressPercent}%` }"></div>
            </div>
          </div>
          <NuxtLink :to="currentMission.link" class="btn-secondary" style="text-decoration: none;">
            <i class="mdi" :class="completedMissions === totalMissions ? 'mdi-refresh' : 'mdi-play-circle-outline'" style="font-size: 18px"></i> 
            {{ completedMissions === totalMissions ? 'Repasar contenido' : 'Continuar misión' }} 
            <i class="mdi mdi-arrow-right"></i>
          </NuxtLink>
        </div>
      </div>
    </div>

    <section class="trivia-row">
      <h3 class="section-title">Datos curiosos</h3>
      <div class="trivia-grid">
        <div class="trivia-card"><i class="mdi mdi-microscope"></i><p>Las células pueden ser 10-30 micras de tamaño.</p></div>
        <div class="trivia-card"><i class="mdi mdi-dna"></i><p>Todas las células contienen material genético (ADN).</p></div>
        <div class="trivia-card"><i class="mdi mdi-flash"></i><p>Las mitocondrias son las "centrales eléctricas" de la célula.</p></div>
        <div class="trivia-card"><i class="mdi mdi-leaf"></i><p>Las células vegetales tienen cloroplastos para realizar fotosíntesis.</p></div>
      </div>
    </section>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

definePageMeta({ layout: false })

const visitedPages = useState('visitedPages', () => [])

onMounted(() => {
  if (process.client) {
    const saved = localStorage.getItem('biocell_progress')
    if (saved) {
      try { visitedPages.value = JSON.parse(saved) } catch (e) {}
    }
  }
})

const totalMissions = 4
const completedMissions = computed(() => visitedPages.value.filter(p => p !== '/dashboard').length)
const progressPercent = computed(() => Math.round((completedMissions.value / totalMissions) * 100))

const currentMission = computed(() => {
  if (!visitedPages.value.includes('/contenido')) {
    return {
      title: 'Misión 1: Fundamentos',
      desc: 'Explora el contenido interactivo y visualiza los videos sobre biología celular.',
      link: '/contenido',
      icon: 'mdi-microscope'
    }
  } else if (!visitedPages.value.includes('/actividades')) {
    return {
      title: 'Misión 2: Práctica',
      desc: 'Completa los 4 minijuegos interactivos para afianzar tus conocimientos.',
      link: '/actividades',
      icon: 'mdi-gamepad-variant'
    }
  } else if (!visitedPages.value.includes('/recursos')) {
    return {
      title: 'Misión 3: Investigación',
      desc: 'Explora los recursos suplementarios y documentos de apoyo.',
      link: '/recursos',
      icon: 'mdi-flask-outline'
    }
  } else if (!visitedPages.value.includes('/evaluaciones')) {
    return {
      title: 'Misión 4: Evaluación',
      desc: 'Pon a prueba todo lo que has aprendido en el examen final.',
      link: '/evaluaciones',
      icon: 'mdi-clipboard-check-outline'
    }
  } else {
    return {
      title: '¡Misiones Completadas!',
      desc: 'Has completado todas las misiones principales del OVA. ¡Excelente trabajo!',
      link: '/dashboard',
      icon: 'mdi-check-decagram'
    }
  }
})
</script>

<style scoped>
@keyframes float {
  from { transform: translateY(0); }
  to { transform: translateY(-5px); }
}

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

.hero-text { max-width: 45%; z-index: 2; }

.hero-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 48px;
  margin-bottom: 8px;
  line-height: 1;
}

.title-bio { color: var(--cyan); text-shadow: var(--glow-cyan); }
.title-cell { color: var(--lime); text-shadow: var(--glow-lime); }

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

.hero-desc { font-size: 15px; color: var(--text-main); line-height: 1.6; margin-bottom: 24px; }

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
  text-decoration: none;
}
.btn-primary:hover {
  background: linear-gradient(135deg, rgba(0,229,255,0.3), rgba(0,191,165,0.3));
  box-shadow: 0 0 25px rgba(0,229,255,0.3);
  transform: translateY(-2px);
}

.hero-image { position: relative; width: 460px; height: 250px; display: flex; align-items: center; justify-content: center; }
.cell-illustration { position: relative; animation: float 6s ease-in-out infinite alternate; }

.orbit-wrapper {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  animation: orbitSpin 25s linear infinite;
  z-index: 10;
}

.orbit-item {
  position: absolute;
  top: 0;
  left: 0;
}
.item-1 { transform: rotate(0deg) translateX(150px); }
.item-2 { transform: rotate(72deg) translateX(150px); }
.item-3 { transform: rotate(144deg) translateX(150px); }
.item-4 { transform: rotate(216deg) translateX(150px); }
.item-5 { transform: rotate(288deg) translateX(150px); }

.anti-1 { transform: rotate(0deg); }
.anti-2 { transform: rotate(-72deg); }
.anti-3 { transform: rotate(-144deg); }
.anti-4 { transform: rotate(-216deg); }
.anti-5 { transform: rotate(-288deg); }

.callout {
  position: absolute;
  width: 140px;
  top: -30px;
  left: -70px;
  background: transparent;
  border: none;
  animation: orbitSpinReverse 25s linear infinite;
  pointer-events: none;
}

.callout-box h5 { color: var(--cyan); font-size: 13px; margin-bottom: 4px; display: flex; align-items: center; justify-content: center; gap: 6px; text-shadow: 0 2px 4px rgba(0,0,0,0.8); }
.callout-box p { font-size: 11px; color: var(--text-main); line-height: 1.4; text-align: center; text-shadow: 0 2px 4px rgba(0,0,0,0.8); }

@keyframes orbitSpin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
@keyframes orbitSpinReverse {
  from { transform: rotate(0deg); }
  to { transform: rotate(-360deg); }
}

.dashboard-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 30px; }
.section-title { font-size: 18px; font-weight: 600; margin-bottom: 20px; color: var(--text-main); }
.actions-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 30px; }

.action-card {
  background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px;
  padding: 20px; display: flex; flex-direction: column; position: relative;
  transition: all 0.3s ease; cursor: pointer; overflow: hidden; text-decoration: none; color: var(--text-main);
}
.action-card:hover { transform: translateY(-4px); background: var(--bg-card-hover); border-color: var(--cyan); box-shadow: 0 10px 20px rgba(0,229,255,0.05); }

.action-icon { font-size: 32px; margin-bottom: 16px; }
.card-explore .action-icon { color: var(--cyan); text-shadow: 0 0 15px rgba(0,229,255,0.4); }
.card-activities .action-icon { color: var(--lime); text-shadow: 0 0 15px rgba(118,255,3,0.4); }
.card-lab .action-icon { color: #2979ff; text-shadow: 0 0 15px rgba(41,121,255,0.4); }
.card-challenges .action-icon { color: #ffd600; text-shadow: 0 0 15px rgba(255,214,0,0.4); }

.action-card h4 { font-size: 15px; margin-bottom: 8px; color: white; }
.action-card p { font-size: 11px; color: var(--text-muted); line-height: 1.4; margin-bottom: 12px; flex: 1; }
.action-arrow { align-self: flex-end; background: rgba(255,255,255,0.05); width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; color: var(--text-muted); transition: all 0.3s ease; }
.action-card:hover .action-arrow { background: var(--cyan); color: var(--bg-main); }

.progress-section { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px 24px; display: flex; align-items: center; gap: 20px; }
.progress-label { font-size: 14px; font-weight: 500; white-space: nowrap; }
.progress-track { flex: 1; height: 8px; background: rgba(255,255,255,0.05); border-radius: 4px; overflow: hidden; }
.progress-fill { height: 100%; background: linear-gradient(90deg, var(--cyan), var(--lime)); border-radius: 4px; box-shadow: 0 0 10px rgba(118,255,3,0.5); }
.progress-percent { font-weight: 700; color: var(--lime); }

.mission-card { background: linear-gradient(180deg, var(--bg-card) 0%, rgba(2,11,24,0.5) 100%); border: 1px solid var(--border-color); border-radius: 16px; padding: 30px; height: calc(100% - 44px); display: flex; flex-direction: column; }
.mission-icon { width: 60px; height: 60px; background: rgba(0,229,255,0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 32px; color: var(--cyan); margin-bottom: 20px; }
.mission-title { font-size: 18px; color: var(--cyan); margin-bottom: 12px; }
.mission-desc { font-size: 13px; color: var(--text-muted); line-height: 1.5; flex: 1; }
.mission-stats { margin-bottom: 20px; }
.mission-steps { display: block; font-size: 12px; color: var(--text-main); margin-bottom: 8px; text-align: right; }
.progress-track.small { height: 4px; }
.btn-secondary { background: var(--cyan); color: var(--bg-main); border: none; padding: 12px; border-radius: 8px; font-weight: 600; font-size: 13px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.2s ease; width: 100%; }
.btn-secondary:hover { background: var(--lime); transform: translateY(-2px); }

.trivia-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.trivia-card { background: var(--bg-card); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 16px; display: flex; align-items: center; gap: 16px; }
.trivia-card i { font-size: 24px; color: var(--cyan); opacity: 0.7; }
.trivia-card p { font-size: 11px; color: var(--text-muted); line-height: 1.4; margin: 0; }

/* ═══════════════════════════════════════════════
   RESPONSIVE (MOBILE SUPPORT)
═══════════════════════════════════════════════ */
@media (max-width: 1200px) {
  .dashboard-grid { grid-template-columns: 1fr; }
  .actions-grid { grid-template-columns: repeat(2, 1fr); }
  .trivia-grid { grid-template-columns: repeat(2, 1fr); }
  .hero-image { width: 350px; }
}

@media (max-width: 992px) {
  .hero-banner { flex-direction: column; text-align: center; padding: 40px 30px; }
  .hero-text { max-width: 100%; margin-bottom: 30px; }
  .hero-image { width: 100%; height: 200px; }
  .callout { display: none; } /* Hide callouts on tablet to save space */
}

@media (max-width: 600px) {
  .hero-banner { padding: 30px 20px; }
  .hero-title { font-size: 36px; }
  .hero-image { display: none; }
  .actions-grid { grid-template-columns: 1fr; }
  .trivia-grid { grid-template-columns: 1fr; }
  .progress-section { flex-direction: column; align-items: flex-start; gap: 12px; }
  .mission-card { padding: 20px; }
}
</style>
