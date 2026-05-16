<template>
  <div class="activity-container">
    <div class="activity-header">
      <h3>Ingeniería Genética: Construye una Célula Vegetal</h3>
      <p>Selecciona únicamente las estructuras y organelos que componen una célula vegetal funcional. ¡Cuidado con las piezas incompatibles!</p>
    </div>

    <div v-if="gameCompleted" class="victory-screen">
      <div class="victory-icon"><i class="mdi mdi-leaf"></i></div>
      <h2>¡Célula Vegetal Ensamblada!</h2>
      <p>Has seleccionado correctamente todas las estructuras esenciales.</p>
      <button class="btn-primary" @click="resetGame">Iniciar Nueva Síntesis</button>
    </div>

    <div v-else class="builder-board">
      <div class="status-panel" :class="{ 'warning': errorCount > 0 }">
        <div class="status-text">
          <i class="mdi" :class="errorCount === 0 ? 'mdi-shield-check' : 'mdi-alert'"></i>
          {{ errorCount === 0 ? 'Sistemas estables' : `¡Atención! ${errorCount} piezas incompatibles detectadas` }}
        </div>
        <div class="progress-text">{{ selectedCorrect.length }} / {{ targetOrganelles.length }} estructuras esenciales</div>
      </div>

      <div class="organelles-grid">
        <div 
          v-for="item in availableOrganelles" 
          :key="item.id"
          class="organelle-card"
          :class="{ 
            'selected': isSelected(item.id),
            'correct-pulse': showPulse === item.id && item.isPlant,
            'error-shake': showPulse === item.id && !item.isPlant
          }"
          @click="toggleOrganelle(item)"
        >
          <div class="card-icon" :style="{ color: item.color }">
            <img v-if="item.image" :src="item.image" :alt="item.name" class="organ-image">
            <i v-else :class="item.icon"></i>
          </div>
          <h5 class="card-name">{{ item.name }}</h5>
          <div class="card-indicator"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const availableOrganelles = [
  { id: 'membrana', name: 'Membrana Plasmática', isPlant: true, icon: 'mdi-chart-donut', image: '/images/membrane.png', color: '#00e5ff' },
  { id: 'pared', name: 'Pared Celular', isPlant: true, icon: 'mdi-border-all', image: '/images/cell_wall.png', color: '#4caf50' },
  { id: 'nucleo', name: 'Núcleo', isPlant: true, icon: 'mdi-record-circle-outline', image: '/images/nucleus_render.png', color: '#76ff03' },
  { id: 'centriolos', name: 'Centriolos', isPlant: false, icon: 'mdi-asterisk', image: '/images/centrioles.png', color: '#ff5252' },
  { id: 'mitocondria', name: 'Mitocondria', isPlant: true, icon: 'mdi-flash', image: '/images/mitochondria_render.png', color: '#ffeb3b' },
  { id: 'cloroplasto', name: 'Cloroplastos', isPlant: true, icon: 'mdi-leaf', image: '/images/chloroplast_render.png', color: '#4caf50' },
  { id: 'vacuola', name: 'Gran Vacuola Central', isPlant: true, icon: 'mdi-water-outline', image: '/images/vacuole.png', color: '#00b8d4' },
  { id: 'nucleoide', name: 'Nucleoide (ADN libre)', isPlant: false, icon: 'mdi-dna', image: '/images/dna.png', color: '#e91e63' },
  { id: 'ribosomas', name: 'Ribosomas', isPlant: true, icon: 'mdi-dots-grid', image: '/images/ribosome.png', color: '#9c27b0' },
  { id: 'golgi', name: 'Aparato de Golgi', isPlant: true, icon: 'mdi-layers-outline', image: '/images/golgi_render.png', color: '#ff9800' }
]

const targetOrganelles = availableOrganelles.filter(o => o.isPlant)
const selectedIds = ref([])
const showPulse = ref(null)

const selectedCorrect = computed(() => selectedIds.value.filter(id => availableOrganelles.find(o => o.id === id)?.isPlant))
const errorCount = computed(() => selectedIds.value.filter(id => !availableOrganelles.find(o => o.id === id)?.isPlant).length)

const gameCompleted = computed(() => selectedCorrect.value.length === targetOrganelles.length && errorCount.value === 0)

const isSelected = (id) => selectedIds.value.includes(id)

const toggleOrganelle = (item) => {
  showPulse.value = item.id
  setTimeout(() => { showPulse.value = null }, 500)

  if (isSelected(item.id)) {
    selectedIds.value = selectedIds.value.filter(id => id !== item.id)
  } else {
    selectedIds.value.push(item.id)
  }
}

const resetGame = () => {
  selectedIds.value = []
  showPulse.value = null
}
</script>

<style scoped>
.activity-container { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px; padding: 30px; min-height: 500px; display: flex; flex-direction: column; overflow-x: hidden; overflow-y: visible; word-break: break-word; }
.activity-header { text-align: center; margin-bottom: 25px; }
.activity-header h3 { font-family: 'Orbitron', sans-serif; color: var(--cyan); font-size: 24px; margin-bottom: 10px; }
.activity-header p { color: var(--text-muted); font-size: 15px; max-width: 650px; margin: 0 auto; }

.builder-board { display: flex; flex-direction: column; gap: 20px; flex: 1; }

.status-panel { background: rgba(0, 191, 165, 0.1); border: 1px solid #00bfa5; border-radius: 8px; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; transition: all 0.3s; }
.status-panel.warning { background: rgba(255, 82, 82, 0.1); border-color: #ff5252; }
.status-text { display: flex; align-items: center; gap: 10px; font-weight: bold; color: #00bfa5; font-size: 14px; }
.status-panel.warning .status-text { color: #ff5252; }
.progress-text { font-family: 'Orbitron', sans-serif; font-size: 14px; color: var(--text-main); }

.organelles-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 15px; margin-top: 10px; }

.organelle-card { background: rgba(0,0,0,0.3); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px 15px; text-align: center; cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); position: relative; overflow: hidden; user-select: none; }
.organelle-card:hover { border-color: var(--cyan); transform: translateY(-3px); box-shadow: 0 5px 15px rgba(0,229,255,0.1); }
.card-icon { font-size: 32px; color: var(--text-muted); margin-bottom: 10px; transition: color 0.3s; display: flex; align-items: center; justify-content: center; height: 50px; }
.organ-image { height: 48px; width: 48px; object-fit: contain; filter: brightness(1.2) drop-shadow(0 0 8px currentColor); }
.card-name { font-size: 13px; color: var(--text-main); font-weight: 500; line-height: 1.3; margin: 0; }

.card-indicator { position: absolute; top: 10px; right: 10px; width: 12px; height: 12px; border-radius: 50%; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s; }

.organelle-card.selected { background: rgba(0,229,255,0.05); border-color: var(--cyan); }
.organelle-card.selected .card-icon { color: var(--cyan); text-shadow: 0 0 10px rgba(0,229,255,0.5); }
.organelle-card.selected .card-indicator { background: var(--cyan); border-color: var(--cyan); box-shadow: 0 0 10px var(--cyan); }

/* Animation classes */
.correct-pulse { animation: pulseGreen 0.5s; }
.error-shake { animation: shakeRed 0.5s; border-color: #ff5252 !important; }
.error-shake .card-indicator { background: #ff5252 !important; border-color: #ff5252 !important; box-shadow: 0 0 10px #ff5252 !important; }

@keyframes pulseGreen {
  0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 191, 165, 0.7); }
  50% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(0, 191, 165, 0); }
  100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 191, 165, 0); }
}
@keyframes shakeRed {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}

.victory-screen { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; animation: fadeIn 0.5s ease; }
.victory-icon { font-size: 80px; color: #4caf50; margin-bottom: 20px; text-shadow: 0 0 30px rgba(76,175,80,0.4); }
.victory-screen h2 { font-family: 'Orbitron', sans-serif; font-size: 32px; color: var(--text-main); margin-bottom: 15px; }
.victory-screen p { color: var(--text-muted); font-size: 16px; margin-bottom: 30px; }
.btn-primary { background: linear-gradient(135deg, rgba(0,229,255,0.2), rgba(0,191,165,0.2)); border: 1px solid var(--cyan); color: var(--cyan); padding: 12px 30px; border-radius: 8px; font-family: 'Orbitron', sans-serif; font-size: 15px; cursor: pointer; transition: all 0.3s ease; }
.btn-primary:hover { background: linear-gradient(135deg, rgba(0,229,255,0.3), rgba(0,191,165,0.3)); box-shadow: 0 0 25px rgba(0,229,255,0.3); transform: translateY(-2px); }

@keyframes fadeIn { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }

@media (max-width: 600px) {
  .activity-container { padding: 15px; }
  .organelles-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
  .organelle-card { padding: 15px 10px; }
  .card-icon { font-size: 24px; }
}
</style>
