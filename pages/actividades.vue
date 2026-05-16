<template>
  <NuxtLayout name="dashboard">
    <div class="activities-wrapper">
      <div class="activities-sidebar">
        <h2 class="sidebar-title">Módulo de <span class="highlight">Actividades</span></h2>
        <p class="sidebar-desc">Demuestra tus conocimientos celulares con estos desafíos interactivos.</p>
        
        <nav class="activities-nav">
          <button 
            v-for="act in activitiesList" 
            :key="act.id"
            class="nav-btn"
            :class="{ active: currentActivity === act.id }"
            @click="currentActivity = act.id"
          >
            <i class="mdi" :class="act.icon"></i>
            <div class="btn-text">
              <span class="btn-name">{{ act.name }}</span>
              <span class="btn-type">{{ act.type }}</span>
            </div>
            <i class="mdi mdi-chevron-right chevron"></i>
          </button>
        </nav>
      </div>

      <div class="activity-content">
        <transition name="fade" mode="out-in">
          <component :is="activeComponent" :key="currentActivity"></component>
        </transition>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed } from 'vue'
import ActivityMatchOrganelles from '~/components/activities/ActivityMatchOrganelles.vue'
import ActivityCellSorter from '~/components/activities/ActivityCellSorter.vue'
import ActivityTransportTrivia from '~/components/activities/ActivityTransportTrivia.vue'
import ActivityCellBuilder from '~/components/activities/ActivityCellBuilder.vue'

definePageMeta({ layout: false })

const activitiesList = [
  { id: 'match', name: 'Conexión Sináptica', type: 'Emparejamiento', icon: 'mdi-puzzle-outline', component: ActivityMatchOrganelles },
  { id: 'sorter', name: 'Clasificador Celular', type: 'Clasificación', icon: 'mdi-sort', component: ActivityCellSorter },
  { id: 'trivia', name: 'Simulador de Membrana', type: 'Desafíos', icon: 'mdi-head-question-outline', component: ActivityTransportTrivia },
  { id: 'builder', name: 'Ingeniería Genética', type: 'Construcción', icon: 'mdi-wrench-outline', component: ActivityCellBuilder }
]

const currentActivity = ref('match')

const activeComponent = computed(() => {
  return activitiesList.find(a => a.id === currentActivity.value)?.component
})
</script>

<style scoped>
.activities-wrapper {
  display: flex; gap: 30px; min-height: calc(100vh - 120px);
}

.activities-sidebar {
  width: 320px; flex-shrink: 0; display: flex; flex-direction: column;
}

.sidebar-title { font-family: 'Orbitron', sans-serif; font-size: 28px; margin-bottom: 10px; }
.sidebar-title .highlight { color: var(--cyan); }
.sidebar-desc { color: var(--text-muted); font-size: 14px; margin-bottom: 30px; line-height: 1.5; }

.activities-nav { display: flex; flex-direction: column; gap: 12px; }

.nav-btn {
  background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px;
  padding: 16px; display: flex; align-items: center; text-align: left; cursor: pointer;
  transition: all 0.3s ease; position: relative; overflow: hidden;
}

.nav-btn::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px;
  background: var(--cyan); transform: scaleY(0); transition: transform 0.3s;
}

.nav-btn:hover { background: rgba(0,229,255,0.05); border-color: var(--cyan); transform: translateX(5px); }

.nav-btn.active { background: rgba(0,229,255,0.1); border-color: var(--cyan); }
.nav-btn.active::before { transform: scaleY(1); }

.nav-btn i:first-child { font-size: 24px; color: var(--text-muted); margin-right: 15px; transition: color 0.3s; }
.nav-btn.active i:first-child, .nav-btn:hover i:first-child { color: var(--cyan); }

.btn-text { flex: 1; display: flex; flex-direction: column; gap: 4px; }
.btn-name { color: var(--text-main); font-weight: 600; font-size: 15px; }
.btn-type { color: var(--text-muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }

.chevron { color: var(--border-color); font-size: 20px; transition: all 0.3s; }
.nav-btn.active .chevron { color: var(--cyan); transform: translateX(3px); }

.activity-content {
  flex: 1; display: flex; flex-direction: column; min-width: 0;
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease, transform 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; transform: translateY(10px); }

@media (max-width: 992px) {
  .activities-wrapper { flex-direction: column; }
  .activities-sidebar { width: 100%; }
  .activities-nav { flex-direction: row; flex-wrap: wrap; }
  .nav-btn { flex: 1; min-width: 250px; }
}
</style>
