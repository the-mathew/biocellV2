<template>
  <div class="activity-container">
    <div class="activity-header">
      <h3>Conexión Sináptica: Organelos y Funciones</h3>
      <p>Selecciona un organelo de la columna izquierda y luego su función correspondiente en la columna derecha para establecer la conexión.</p>
    </div>

    <div v-if="gameCompleted" class="victory-screen">
      <div class="victory-icon"><i class="mdi mdi-check-decagram"></i></div>
      <h2>¡Conexión Completada!</h2>
      <p>Has emparejado correctamente todos los organelos con sus funciones.</p>
      <button class="btn-primary" @click="resetGame">Jugar de Nuevo</button>
    </div>

    <div v-else class="match-board">
      <div class="column organelles-col">
        <h4>Organelos</h4>
        <button 
          v-for="item in shuffledOrganelles" 
          :key="item.id"
          class="match-btn"
          :class="{ 
            'selected': selectedOrganelle === item.id, 
            'matched': matchedPairs.includes(item.id),
            'error': errorOrganelle === item.id
          }"
          @click="selectOrganelle(item.id)"
          :disabled="matchedPairs.includes(item.id)"
        >
          {{ item.name }}
        </button>
      </div>

      <div class="column functions-col">
        <h4>Funciones</h4>
        <button 
          v-for="item in shuffledFunctions" 
          :key="item.id"
          class="match-btn function-btn"
          :class="{ 
            'selected': selectedFunction === item.id, 
            'matched': matchedPairs.includes(item.id),
            'error': errorFunction === item.id
          }"
          @click="selectFunction(item.id)"
          :disabled="matchedPairs.includes(item.id)"
        >
          {{ item.desc }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const basePairs = [
  { id: 'mitocondria', name: 'Mitocondria', desc: 'Producción de energía (ATP) a través de la respiración celular.' },
  { id: 'nucleo', name: 'Núcleo', desc: 'Contiene el material genético (ADN) y coordina las actividades celulares.' },
  { id: 'ribosoma', name: 'Ribosomas', desc: 'Síntesis y ensamblaje de proteínas.' },
  { id: 'cloroplasto', name: 'Cloroplastos', desc: 'Realiza la fotosíntesis en células vegetales.' },
  { id: 'lisosoma', name: 'Lisosomas', desc: 'Digestión celular y reciclaje de desechos.' },
  { id: 'golgi', name: 'Aparato de Golgi', desc: 'Modifica, empaqueta y distribuye proteínas y lípidos.' }
]

const shuffledOrganelles = ref([])
const shuffledFunctions = ref([])

const selectedOrganelle = ref(null)
const selectedFunction = ref(null)
const errorOrganelle = ref(null)
const errorFunction = ref(null)
const matchedPairs = ref([])

const gameCompleted = computed(() => matchedPairs.value.length === basePairs.length)

const shuffleArray = (array) => {
  const newArr = [...array]
  for (let i = newArr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [newArr[i], newArr[j]] = [newArr[j], newArr[i]]
  }
  return newArr
}

const resetGame = () => {
  shuffledOrganelles.value = shuffleArray(basePairs.map(p => ({ id: p.id, name: p.name })))
  shuffledFunctions.value = shuffleArray(basePairs.map(p => ({ id: p.id, desc: p.desc })))
  selectedOrganelle.value = null
  selectedFunction.value = null
  errorOrganelle.value = null
  errorFunction.value = null
  matchedPairs.value = []
}

onMounted(() => {
  resetGame()
})

const checkMatch = () => {
  if (selectedOrganelle.value && selectedFunction.value) {
    if (selectedOrganelle.value === selectedFunction.value) {
      // Correct match
      matchedPairs.value.push(selectedOrganelle.value)
      selectedOrganelle.value = null
      selectedFunction.value = null
    } else {
      // Incorrect match
      errorOrganelle.value = selectedOrganelle.value
      errorFunction.value = selectedFunction.value
      setTimeout(() => {
        errorOrganelle.value = null
        errorFunction.value = null
        selectedOrganelle.value = null
        selectedFunction.value = null
      }, 800)
    }
  }
}

const selectOrganelle = (id) => {
  if (matchedPairs.value.includes(id)) return
  selectedOrganelle.value = id
  checkMatch()
}

const selectFunction = (id) => {
  if (matchedPairs.value.includes(id)) return
  selectedFunction.value = id
  checkMatch()
}
</script>

<style scoped>
.activity-container {
  background: var(--bg-card); border: 1px solid var(--border-color);
  border-radius: 16px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  min-height: 500px; display: flex; flex-direction: column;
  overflow-x: hidden; overflow-y: visible; word-break: break-word;
}

.activity-header { text-align: center; margin-bottom: 30px; }
.activity-header h3 { font-family: 'Orbitron', sans-serif; color: var(--cyan); font-size: 24px; margin-bottom: 10px; }
.activity-header p { color: var(--text-muted); font-size: 15px; max-width: 600px; margin: 0 auto; }

.match-board {
  display: grid; grid-template-columns: 1fr 1.5fr; gap: 40px; flex: 1;
}

.column { display: flex; flex-direction: column; gap: 12px; }
.column h4 { text-align: center; color: var(--text-main); font-size: 16px; margin-bottom: 10px; letter-spacing: 1px; text-transform: uppercase; }

.match-btn {
  background: rgba(255,255,255,0.03); border: 1px solid var(--border-color);
  padding: 16px 20px; border-radius: 12px; color: var(--text-main); font-size: 15px;
  cursor: pointer; transition: all 0.3s ease; text-align: left; position: relative;
  overflow: hidden;
}

.match-btn:hover:not(:disabled) { border-color: var(--cyan); background: rgba(0,229,255,0.05); transform: translateX(5px); }
.match-btn.selected { background: rgba(0,229,255,0.15); border-color: var(--cyan); box-shadow: 0 0 15px rgba(0,229,255,0.2); }
.match-btn.matched { background: rgba(0, 191, 165, 0.1); border-color: #00bfa5; color: #00bfa5; opacity: 0.7; transform: none; cursor: default; }
.match-btn.error { background: rgba(255, 82, 82, 0.1); border-color: #ff5252; animation: shake 0.4s; }

.function-btn { font-size: 14px; line-height: 1.4; color: var(--text-muted); }
.function-btn:hover:not(:disabled) { transform: translateX(-5px); }
.function-btn.selected { color: var(--text-main); }
.function-btn.matched { color: #00bfa5; }

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}

.victory-screen {
  flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center;
  text-align: center; animation: fadeIn 0.5s ease;
}
.victory-icon { font-size: 80px; color: #00bfa5; margin-bottom: 20px; text-shadow: 0 0 30px rgba(0,191,165,0.4); }
.victory-screen h2 { font-family: 'Orbitron', sans-serif; font-size: 32px; color: var(--text-main); margin-bottom: 15px; }
.victory-screen p { color: var(--text-muted); font-size: 16px; margin-bottom: 30px; }

.btn-primary {
  background: linear-gradient(135deg, rgba(0,229,255,0.2), rgba(0,191,165,0.2));
  border: 1px solid var(--cyan); color: var(--cyan); padding: 12px 30px; border-radius: 8px;
  font-family: 'Orbitron', sans-serif; font-size: 15px; font-weight: 600; cursor: pointer;
  transition: all 0.3s ease;
}
.btn-primary:hover { background: linear-gradient(135deg, rgba(0,229,255,0.3), rgba(0,191,165,0.3)); box-shadow: 0 0 25px rgba(0,229,255,0.3); transform: translateY(-2px); }

@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

@media (max-width: 768px) {
  .activity-container { padding: 15px; }
  .match-board { grid-template-columns: 1fr; gap: 20px; }
  .match-btn:hover:not(:disabled) { transform: none; }
  .function-btn:hover:not(:disabled) { transform: none; }
  .match-btn { padding: 12px; font-size: 13px; }
}
</style>
