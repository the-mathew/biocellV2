<template>
  <div class="activity-container">
    <div class="activity-header">
      <h3>Simulador de Membrana</h3>
      <p>Resuelve estos desafíos sobre el transporte celular y la permeabilidad de la membrana.</p>
    </div>

    <div v-if="gameCompleted" class="victory-screen">
      <div class="victory-icon"><i class="mdi mdi-trophy-variant-outline"></i></div>
      <h2>¡Simulación Exitosa!</h2>
      <p>Puntuación Final: {{ score }} / {{ questions.length }}</p>
      <div class="score-bar">
        <div class="score-fill" :style="{ width: `${(score / questions.length) * 100}%` }"></div>
      </div>
      <button class="btn-primary" @click="resetGame">Reiniciar Simulador</button>
    </div>

    <div v-else class="trivia-board">
      <div class="progress-indicator">
        Desafío {{ currentQuestionIndex + 1 }} de {{ questions.length }}
      </div>

      <transition name="fade" mode="out-in">
        <div :key="currentQuestionIndex" class="question-card">
          <div class="question-icon"><i class="mdi mdi-help-circle-outline"></i></div>
          <h4 class="question-text">{{ currentQuestion.text }}</h4>
          
          <div class="options-grid">
            <button 
              v-for="(option, index) in currentQuestion.options" 
              :key="index"
              class="option-btn"
              :class="{ 
                'correct': showFeedback && index === currentQuestion.correctAnswer,
                'wrong': showFeedback && selectedOption === index && index !== currentQuestion.correctAnswer,
                'disabled': showFeedback
              }"
              @click="selectOption(index)"
              :disabled="showFeedback"
            >
              <span class="option-letter">{{ String.fromCharCode(65 + index) }}</span>
              <span class="option-text">{{ option }}</span>
              <i v-if="showFeedback && index === currentQuestion.correctAnswer" class="mdi mdi-check-circle result-icon"></i>
              <i v-if="showFeedback && selectedOption === index && index !== currentQuestion.correctAnswer" class="mdi mdi-close-circle result-icon"></i>
            </button>
          </div>

          <div v-if="showFeedback" class="feedback-panel" :class="isCorrect ? 'success' : 'error'">
            <div class="feedback-title">
              <i :class="isCorrect ? 'mdi mdi-check' : 'mdi mdi-close'"></i>
              {{ isCorrect ? '¡Correcto!' : 'Incorrecto' }}
            </div>
            <p class="feedback-desc">{{ currentQuestion.explanation }}</p>
            <button class="btn-next" @click="nextQuestion">
              {{ currentQuestionIndex < questions.length - 1 ? 'Siguiente Desafío' : 'Ver Resultados' }}
              <i class="mdi mdi-arrow-right"></i>
            </button>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const questions = [
  {
    text: 'Una molécula pequeña de oxígeno necesita entrar a la célula a favor de su gradiente de concentración. ¿Qué mecanismo utiliza?',
    options: ['Transporte Activo', 'Difusión Simple', 'Endocitosis', 'Ósmosis'],
    correctAnswer: 1,
    explanation: 'El oxígeno es una molécula pequeña y sin carga que cruza libremente la bicapa lipídica sin gasto de energía mediante difusión simple.'
  },
  {
    text: 'La célula necesita expulsar una gran proteína producida en el aparato de Golgi hacia el exterior. ¿Cómo lo hace?',
    options: ['Exocitosis', 'Difusión Facilitada', 'Fagocitosis', 'Bomba de Sodio-Potasio'],
    correctAnswer: 0,
    explanation: 'Las moléculas muy grandes o en gran cantidad se envuelven en vesículas y se fusionan con la membrana para ser expulsadas mediante exocitosis.'
  },
  {
    text: 'Se requiere mover iones de sodio (Na+) en contra de su gradiente de concentración, lo cual requiere energía (ATP). Esto es un ejemplo de:',
    options: ['Transporte Pasivo', 'Transporte Activo', 'Pinocitosis', 'Difusión Simple'],
    correctAnswer: 1,
    explanation: 'Cualquier movimiento en contra del gradiente de concentración requiere gasto de energía celular (ATP) y se denomina transporte activo.'
  },
  {
    text: 'El movimiento específico de agua a través de una membrana semipermeable desde un área de menor concentración de solutos a una de mayor concentración se llama:',
    options: ['Ósmosis', 'Fagocitosis', 'Transporte Activo Secundario', 'Exocitosis'],
    correctAnswer: 0,
    explanation: 'La ósmosis es un tipo especial de difusión pasiva enfocada únicamente en el movimiento de moléculas de agua para equilibrar concentraciones.'
  }
]

const currentQuestionIndex = ref(0)
const selectedOption = ref(null)
const showFeedback = ref(false)
const score = ref(0)
const isCorrect = ref(false)

const currentQuestion = computed(() => questions[currentQuestionIndex.value])
const gameCompleted = computed(() => currentQuestionIndex.value >= questions.length)

const resetGame = () => {
  currentQuestionIndex.value = 0
  score.value = 0
  selectedOption.value = null
  showFeedback.value = false
}

const selectOption = (index) => {
  selectedOption.value = index
  isCorrect.value = (index === currentQuestion.value.correctAnswer)
  if (isCorrect.value) score.value++
  showFeedback.value = true
}

const nextQuestion = () => {
  selectedOption.value = null
  showFeedback.value = false
  currentQuestionIndex.value++
}
</script>

<style scoped>
.activity-container { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px; padding: 30px; min-height: 500px; display: flex; flex-direction: column; overflow-x: hidden; overflow-y: visible; word-break: break-word; }
.activity-header { text-align: center; margin-bottom: 20px; }
.activity-header h3 { font-family: 'Orbitron', sans-serif; color: var(--cyan); font-size: 24px; margin-bottom: 10px; }
.activity-header p { color: var(--text-muted); font-size: 15px; }

.trivia-board { display: flex; flex-direction: column; align-items: center; flex: 1; width: 100%; max-width: 700px; margin: 0 auto; }
.progress-indicator { background: rgba(0,229,255,0.1); color: var(--cyan); padding: 6px 16px; border-radius: 20px; font-size: 12px; font-weight: bold; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; }

.question-card { background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); border-radius: 12px; padding: 30px; width: 100%; position: relative; }
.question-icon { position: absolute; top: -20px; left: 50%; transform: translateX(-50%); background: var(--bg-card); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 1px solid var(--cyan); color: var(--cyan); font-size: 20px; }
.question-text { font-size: 18px; color: var(--text-main); line-height: 1.5; margin-top: 10px; margin-bottom: 24px; text-align: center; }

.options-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
.option-btn { background: var(--bg-main); border: 1px solid var(--border-color); border-radius: 8px; padding: 16px; display: flex; align-items: center; cursor: pointer; transition: all 0.2s; position: relative; text-align: left; }
.option-btn:hover:not(.disabled) { border-color: var(--cyan); background: rgba(0,229,255,0.05); }
.option-letter { background: rgba(255,255,255,0.05); width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 4px; margin-right: 12px; font-weight: bold; color: var(--text-muted); font-size: 12px; }
.option-text { flex: 1; color: var(--text-main); font-size: 14px; }
.result-icon { font-size: 20px; margin-left: 10px; }

.option-btn.correct { background: rgba(0,191,165,0.1); border-color: #00bfa5; }
.option-btn.correct .option-letter { background: #00bfa5; color: #000; }
.option-btn.correct .result-icon { color: #00bfa5; }

.option-btn.wrong { background: rgba(255,82,82,0.1); border-color: #ff5252; }
.option-btn.wrong .option-letter { background: #ff5252; color: #fff; }
.option-btn.wrong .result-icon { color: #ff5252; }

.option-btn.disabled { cursor: default; }

.feedback-panel { padding: 20px; border-radius: 8px; margin-top: 20px; animation: fadeIn 0.4s; }
.feedback-panel.success { background: rgba(0,191,165,0.05); border-left: 4px solid #00bfa5; }
.feedback-panel.error { background: rgba(255,82,82,0.05); border-left: 4px solid #ff5252; }
.feedback-title { font-weight: bold; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
.feedback-panel.success .feedback-title { color: #00bfa5; }
.feedback-panel.error .feedback-title { color: #ff5252; }
.feedback-desc { font-size: 13px; color: var(--text-muted); line-height: 1.5; margin-bottom: 15px; }

.btn-next { background: var(--cyan); color: var(--bg-main); border: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; cursor: pointer; display: flex; align-items: center; gap: 8px; float: right; transition: all 0.2s; }
.btn-next:hover { opacity: 0.9; transform: translateX(3px); }

.victory-screen { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
.victory-icon { font-size: 80px; color: #ffca28; margin-bottom: 20px; text-shadow: 0 0 30px rgba(255,202,40,0.3); }
.score-bar { width: 100%; max-width: 300px; height: 10px; background: rgba(255,255,255,0.1); border-radius: 5px; margin-bottom: 30px; overflow: hidden; }
.score-fill { height: 100%; background: linear-gradient(90deg, #00bfa5, var(--cyan)); transition: width 1s cubic-bezier(0.4, 0, 0.2, 1); }
.btn-primary { background: linear-gradient(135deg, rgba(0,229,255,0.2), rgba(0,191,165,0.2)); border: 1px solid var(--cyan); color: var(--cyan); padding: 12px 30px; border-radius: 8px; font-family: 'Orbitron', sans-serif; font-size: 15px; cursor: pointer; transition: all 0.3s ease; }
.btn-primary:hover { background: linear-gradient(135deg, rgba(0,229,255,0.3), rgba(0,191,165,0.3)); box-shadow: 0 0 25px rgba(0,229,255,0.3); transform: translateY(-2px); }

.fade-enter-active, .fade-leave-active { transition: opacity 0.3s, transform 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; transform: translateY(10px); }

@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

@media (max-width: 600px) {
  .activity-container { padding: 15px; }
  .options-grid { grid-template-columns: 1fr; gap: 10px; }
  .question-card { padding: 25px 15px 15px; }
  .option-btn { padding: 12px; }
  .question-text { font-size: 15px; margin-bottom: 15px; }
}
</style>
