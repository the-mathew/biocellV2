<template>
  <div class="activity-container">
    <div class="activity-header">
      <h3>Clasificador Celular</h3>
      <p>Clasifica las siguientes características según correspondan a una célula Procariota o Eucariota.</p>
    </div>

    <div v-if="gameCompleted" class="victory-screen">
      <div class="victory-icon"><i class="mdi mdi-microscope"></i></div>
      <h2>¡Clasificación Perfecta!</h2>
      <p>Has demostrado un excelente dominio de los tipos celulares.</p>
      <button class="btn-primary" @click="resetGame">Volver a Clasificar</button>
    </div>

    <div v-else class="sorter-board">
      <div class="unassigned-area">
        <h4>Características por clasificar ({{ unassignedItems.length }})</h4>
        <div class="items-pool">
          <transition-group name="list">
            <div 
              v-for="item in unassignedItems" 
              :key="item.id" 
              class="sort-item"
            >
              <span>{{ item.text }}</span>
              <div class="sort-actions">
                <button class="action-btn left" @click="sortItem(item, 'procariota')" title="Es Procariota"><i class="mdi mdi-arrow-left"></i> Procariota</button>
                <button class="action-btn right" @click="sortItem(item, 'eucariota')" title="Es Eucariota">Eucariota <i class="mdi mdi-arrow-right"></i></button>
              </div>
            </div>
          </transition-group>
          <div v-if="unassignedItems.length === 0" class="empty-msg">Todas las características han sido asignadas.</div>
        </div>
      </div>

      <div class="buckets-area">
        <div class="bucket procariota-bucket">
          <div class="bucket-header">
            <h4>Célula Procariota</h4>
          </div>
          <transition-group name="list" tag="div" class="bucket-content">
            <div v-for="item in procariotaItems" :key="item.id" class="sorted-item success">
              <i class="mdi mdi-check-circle"></i> {{ item.text }}
            </div>
          </transition-group>
        </div>

        <div class="bucket eucariota-bucket">
          <div class="bucket-header">
            <h4>Célula Eucariota</h4>
          </div>
          <transition-group name="list" tag="div" class="bucket-content">
            <div v-for="item in eucariotaItems" :key="item.id" class="sorted-item success">
              <i class="mdi mdi-check-circle"></i> {{ item.text }}
            </div>
          </transition-group>
        </div>
      </div>
      
      <div v-if="errorMessage" class="error-toast">
        <i class="mdi mdi-alert-circle"></i> {{ errorMessage }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const allItems = [
  { id: '1', text: 'El ADN está libre en el citoplasma (nucleoide)', type: 'procariota' },
  { id: '2', text: 'Posee núcleo definido y delimitado por membrana', type: 'eucariota' },
  { id: '3', text: 'Son las células de bacterias y arqueas', type: 'procariota' },
  { id: '4', text: 'Son las células de animales, plantas y hongos', type: 'eucariota' },
  { id: '5', text: 'Presenta organelos membranosos complejos (ej. mitocondrias)', type: 'eucariota' },
  { id: '6', text: 'Generalmente su tamaño es mucho más pequeño (1-10 µm)', type: 'procariota' },
  { id: '7', text: 'Su tamaño es mayor y más compleja (10-100 µm)', type: 'eucariota' },
  { id: '8', text: 'Evolutivamente son las más antiguas en la Tierra', type: 'procariota' }
]

const unassignedItems = ref([])
const procariotaItems = ref([])
const eucariotaItems = ref([])
const errorMessage = ref(null)

const gameCompleted = computed(() => unassignedItems.value.length === 0 && procariotaItems.value.length > 0)

const shuffleArray = (array) => {
  const newArr = [...array]
  for (let i = newArr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [newArr[i], newArr[j]] = [newArr[j], newArr[i]]
  }
  return newArr
}

const resetGame = () => {
  unassignedItems.value = shuffleArray(allItems)
  procariotaItems.value = []
  eucariotaItems.value = []
  errorMessage.value = null
}

onMounted(() => {
  resetGame()
})

const sortItem = (item, selectedType) => {
  if (item.type === selectedType) {
    // Correct
    unassignedItems.value = unassignedItems.value.filter(i => i.id !== item.id)
    if (selectedType === 'procariota') procariotaItems.value.push(item)
    else eucariotaItems.value.push(item)
    errorMessage.value = null
  } else {
    // Incorrect
    errorMessage.value = "¡Incorrecto! Vuelve a intentar con esa característica."
    setTimeout(() => { errorMessage.value = null }, 2000)
  }
}
</script>

<style scoped>
.activity-container { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px; padding: 30px; min-height: 500px; display: flex; flex-direction: column; position: relative; overflow-x: hidden; overflow-y: visible; word-break: break-word; }
.activity-header { text-align: center; margin-bottom: 30px; }
.activity-header h3 { font-family: 'Orbitron', sans-serif; color: var(--cyan); font-size: 24px; margin-bottom: 10px; }
.activity-header p { color: var(--text-muted); font-size: 15px; }

.sorter-board { display: flex; flex-direction: column; gap: 30px; flex: 1; }

.unassigned-area { background: rgba(0,0,0,0.2); border: 1px dashed var(--border-color); border-radius: 12px; padding: 20px; text-align: center; }
.unassigned-area h4 { margin-bottom: 15px; color: var(--text-muted); font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }

.items-pool { display: flex; flex-direction: column; gap: 10px; align-items: center; min-height: 100px; }
.sort-item { background: var(--bg-main); border: 1px solid var(--cyan); border-radius: 8px; padding: 12px 20px; width: 100%; max-width: 600px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: all 0.3s ease; }
.sort-item span { font-size: 14px; font-weight: 500; text-align: left; flex: 1; }
.sort-actions { display: flex; gap: 10px; }
.action-btn { background: rgba(255,255,255,0.05); border: 1px solid var(--border-color); border-radius: 6px; padding: 6px 12px; color: var(--text-muted); font-size: 12px; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 4px; }
.action-btn:hover { background: rgba(0,229,255,0.1); border-color: var(--cyan); color: var(--cyan); }

.buckets-area { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.bucket { background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); border-radius: 12px; overflow: hidden; display: flex; flex-direction: column; min-height: 250px; }
.bucket-header { padding: 15px; text-align: center; background: rgba(255,255,255,0.02); border-bottom: 1px solid var(--border-color); }
.bucket-header h4 { margin: 0; color: var(--cyan); font-family: 'Orbitron', sans-serif; }
.bucket-content { padding: 15px; display: flex; flex-direction: column; gap: 8px; flex: 1; }

.sorted-item { background: rgba(0,191,165,0.1); border: 1px solid rgba(0,191,165,0.3); border-radius: 6px; padding: 10px; font-size: 13px; color: #a7ffeb; display: flex; align-items: flex-start; gap: 8px; }
.sorted-item i { color: #00bfa5; margin-top: 2px; }

.empty-msg { color: var(--text-muted); font-style: italic; padding: 20px; }

.error-toast { position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); background: #ff5252; color: white; padding: 10px 20px; border-radius: 8px; font-size: 14px; font-weight: bold; display: flex; align-items: center; gap: 8px; box-shadow: 0 5px 15px rgba(255,82,82,0.4); animation: slideUp 0.3s ease-out; z-index: 10; }

.list-enter-active, .list-leave-active { transition: all 0.4s ease; }
.list-enter-from, .list-leave-to { opacity: 0; transform: translateY(15px); }

.victory-screen { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; animation: fadeIn 0.5s ease; }
.victory-icon { font-size: 80px; color: #00bfa5; margin-bottom: 20px; text-shadow: 0 0 30px rgba(0,191,165,0.4); }
.victory-screen h2 { font-family: 'Orbitron', sans-serif; font-size: 32px; color: var(--text-main); margin-bottom: 15px; }
.btn-primary { background: linear-gradient(135deg, rgba(0,229,255,0.2), rgba(0,191,165,0.2)); border: 1px solid var(--cyan); color: var(--cyan); padding: 12px 30px; border-radius: 8px; font-family: 'Orbitron', sans-serif; font-size: 15px; cursor: pointer; transition: all 0.3s ease; }
.btn-primary:hover { background: linear-gradient(135deg, rgba(0,229,255,0.3), rgba(0,191,165,0.3)); box-shadow: 0 0 25px rgba(0,229,255,0.3); transform: translateY(-2px); }

@keyframes slideUp { from { transform: translate(-50%, 20px); opacity: 0; } to { transform: translate(-50%, 0); opacity: 1; } }
@keyframes fadeIn { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }

@media (max-width: 768px) {
  .activity-container { padding: 15px; }
  .buckets-area { grid-template-columns: 1fr; }
  .sort-item { flex-direction: column; gap: 15px; text-align: center; }
  .sort-actions { width: 100%; justify-content: space-between; }
  .action-btn { padding: 8px 10px; font-size: 11px; }
}
</style>
