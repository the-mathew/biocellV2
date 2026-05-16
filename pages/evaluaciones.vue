<template>
  <NuxtLayout name="dashboard">
    <div class="evaluation-container">
      <div class="eval-header">
        <h2 class="eval-title">Evaluación de <span class="highlight">Biología Celular</span></h2>
        <p class="eval-desc">Responde las siguientes {{ questions.length }} preguntas de selección múltiple tipo ICFES. Selecciona la respuesta que consideres correcta. Tu puntuación final se calculará al enviar la prueba.</p>
        
        <div class="progress-bar-container">
          <div class="progress-text">Progreso: {{ answeredCount }} / {{ questions.length }} respondidas</div>
          <div class="progress-track">
            <div class="progress-fill" :style="{ width: `${(answeredCount / questions.length) * 100}%` }"></div>
          </div>
        </div>
      </div>

      <div class="questions-list">
        <div 
          v-for="(q, qIndex) in questions" 
          :key="q.id" 
          class="question-card"
          :class="{ 
            'is-answered': userAnswers[qIndex] !== null,
            'is-correct': isSubmitted && userAnswers[qIndex] === q.correct,
            'is-incorrect': isSubmitted && userAnswers[qIndex] !== null && userAnswers[qIndex] !== q.correct
          }"
        >
          <div class="question-number">Pregunta {{ qIndex + 1 }}</div>
          <p class="question-statement">{{ q.text }}</p>
          
          <div class="options-container">
            <label 
              v-for="(opt, oIndex) in q.options" 
              :key="oIndex"
              class="option-label"
              :class="{
                'selected': userAnswers[qIndex] === oIndex,
                'reveal-correct': isSubmitted && oIndex === q.correct,
                'reveal-wrong': isSubmitted && userAnswers[qIndex] === oIndex && oIndex !== q.correct
              }"
            >
              <input 
                type="radio" 
                :name="`question_${qIndex}`" 
                :value="oIndex" 
                v-model="userAnswers[qIndex]"
                :disabled="isSubmitted"
              >
              <span class="radio-custom"></span>
              <span class="option-text"><b>{{ String.fromCharCode(65 + oIndex) }}.</b> {{ opt }}</span>
              
              <i v-if="isSubmitted && oIndex === q.correct" class="mdi mdi-check-circle result-icon correct"></i>
              <i v-if="isSubmitted && userAnswers[qIndex] === oIndex && oIndex !== q.correct" class="mdi mdi-close-circle result-icon wrong"></i>
            </label>
          </div>

          <div v-if="isSubmitted && userAnswers[qIndex] !== q.correct" class="feedback-msg error">
            <i class="mdi mdi-alert-circle"></i> Respuesta incorrecta. La respuesta correcta era la <b>{{ String.fromCharCode(65 + q.correct) }}</b>.
          </div>
        </div>
      </div>

      <div class="eval-footer">
        <div v-if="!isSubmitted" class="submit-section">
          <p v-if="unansweredCount > 0" class="warning-text">
            <i class="mdi mdi-alert"></i> Te faltan {{ unansweredCount }} preguntas por responder.
          </p>
          <button 
            class="btn-submit" 
            :disabled="unansweredCount > 0"
            @click="submitExam"
            :class="{ 'ready': unansweredCount === 0 }"
          >
            <i class="mdi mdi-send"></i> Enviar Evaluación
          </button>
        </div>

        <div v-else class="results-section">
          <div class="results-card">
            <h3>Resultados de la Evaluación</h3>
            <div class="score-display">
              <span class="score-number" :class="getScoreClass(finalGrade)">{{ finalGrade.toFixed(1) }}</span>
              <span class="score-scale">/ 5.0</span>
            </div>
            <p class="score-details">Respondiste correctamente <b>{{ correctAnswersCount }}</b> de <b>{{ questions.length }}</b> preguntas.</p>
            <div class="score-message" :class="getScoreClass(finalGrade)">
              {{ getScoreMessage(finalGrade) }}
            </div>
            <button class="btn-retry" @click="resetExam">
              <i class="mdi mdi-refresh"></i> Reintentar Evaluación
            </button>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed } from 'vue'

definePageMeta({ layout: false })

const questions = [
  {
    id: 1,
    text: 'La teoría celular establece que todos los organismos están compuestos por células. ¿Cuál de los siguientes postulados también pertenece a la teoría celular?',
    options: [
      'Todas las células tienen un núcleo definido.',
      'Toda célula proviene de la división de otra célula preexistente.',
      'Las células vegetales son las únicas capaces de reproducirse.',
      'El tamaño de la célula determina el tamaño del organismo.'
    ],
    correct: 1
  },
  {
    id: 2,
    text: '¿Cuál es el organelo encargado de la respiración celular y la producción de energía en forma de ATP?',
    options: ['Aparato de Golgi', 'Lisosoma', 'Mitocondria', 'Ribosoma'],
    correct: 2
  },
  {
    id: 3,
    text: 'A diferencia de las células animales, las células vegetales poseen una estructura exterior rígida que les brinda soporte y protección. Esta estructura es:',
    options: ['La membrana plasmática', 'El citoesqueleto', 'La pared celular', 'La cápsula'],
    correct: 2
  },
  {
    id: 4,
    text: '¿Qué característica morfológica distingue principalmente a una célula procariota de una eucariota?',
    options: [
      'La ausencia de una membrana plasmática.',
      'La presencia de un núcleo definido delimitado por una membrana.',
      'La ausencia de material genético (ADN).',
      'La ausencia de un núcleo definido y de organelos membranosos.'
    ],
    correct: 3
  },
  {
    id: 5,
    text: 'En el proceso de transporte pasivo a través de la membrana celular, el movimiento de sustancias se caracteriza por:',
    options: [
      'Darse en contra del gradiente de concentración, requiriendo ATP.',
      'Requerir energía producida por las mitocondrias.',
      'Darse a favor del gradiente de concentración, sin gasto de energía.',
      'Ocurrir únicamente a través de la formación de vesículas.'
    ],
    correct: 2
  },
  {
    id: 6,
    text: '¿Qué organelo celular funciona como el centro de empaquetamiento, modificación y distribución de proteínas y lípidos?',
    options: ['Retículo endoplasmático liso', 'Aparato de Golgi', 'Ribosoma', 'Vacuola'],
    correct: 1
  },
  {
    id: 7,
    text: 'El proceso biológico mediante el cual el agua se mueve a través de una membrana semipermeable, desde una zona de menor concentración de solutos a una de mayor concentración, se denomina:',
    options: ['Difusión facilitada', 'Ósmosis', 'Transporte activo', 'Endocitosis'],
    correct: 1
  },
  {
    id: 8,
    text: '¿Qué estructura o complejo molecular es compartido tanto por células procariotas como eucariotas, y es esencial para la síntesis de proteínas?',
    options: ['Ribosomas', 'Lisosomas', 'Mitocondrias', 'Cilios'],
    correct: 0
  },
  {
    id: 9,
    text: 'En las células eucariotas, la mayor parte del material genético (ADN) se encuentra protegido y organizado dentro de:',
    options: ['El citoplasma', 'El nucléolo', 'El núcleo', 'El retículo endoplasmático rugoso'],
    correct: 2
  },
  {
    id: 10,
    text: '¿Cuál de los siguientes procesos es un ejemplo clásico de transporte activo, el cual requiere el gasto directo de energía (ATP)?',
    options: [
      'La entrada de oxígeno a la célula.',
      'El movimiento de agua por ósmosis.',
      'La difusión de dióxido de carbono hacia el exterior.',
      'El funcionamiento de la bomba de sodio-potasio.'
    ],
    correct: 3
  },
  {
    id: 11,
    text: 'Los lisosomas son organelos membranosos que contienen enzimas hidrolíticas. Su función biológica principal dentro de la célula animal es:',
    options: [
      'La digestión celular y degradación de desechos o macromoléculas.',
      'La síntesis de carbohidratos complejos.',
      'El almacenamiento de grandes cantidades de agua.',
      'La producción de ATP.'
    ],
    correct: 0
  },
  {
    id: 12,
    text: 'Según el modelo del mosaico fluido, la membrana plasmática celular está compuesta primordialmente por:',
    options: [
      'Una capa rígida de celulosa y proteínas.',
      'Una bicapa de fosfolípidos con diversas proteínas incrustadas.',
      'Una doble capa de proteínas cubiertas por ácidos nucleicos.',
      'Una matriz de glucógeno y lípidos simples.'
    ],
    correct: 1
  },
  {
    id: 13,
    text: 'Durante la observación microscópica de un tejido vegetal, se identifica un organelo de color verde responsable de la fotosíntesis. Este organelo es:',
    options: ['La vacuola', 'El cloroplasto', 'La mitocondria', 'El leucoplasto'],
    correct: 1
  },
  {
    id: 14,
    text: 'El citoplasma es una parte fundamental de todas las células debido a que:',
    options: [
      'Contiene la información genética codificada.',
      'Es la barrera que selecciona qué entra y qué sale de la célula.',
      'Es el medio acuoso donde se suspenden los organelos y ocurren múltiples reacciones químicas.',
      'Se encarga de la división celular celular (mitosis).'
    ],
    correct: 2
  },
  {
    id: 15,
    text: 'Cuando ciertos glóbulos blancos necesitan incorporar grandes partículas sólidas (como una bacteria) desde el exterior para destruirlas, utilizan un mecanismo celular llamado:',
    options: ['Pinocitosis', 'Exocitosis', 'Fagocitosis', 'Difusión facilitada'],
    correct: 2
  }
]

const userAnswers = ref(new Array(questions.length).fill(null))
const isSubmitted = ref(false)

const answeredCount = computed(() => userAnswers.value.filter(a => a !== null).length)
const unansweredCount = computed(() => questions.length - answeredCount.value)

const correctAnswersCount = computed(() => {
  return userAnswers.value.reduce((acc, answer, index) => {
    return acc + (answer === questions[index].correct ? 1 : 0)
  }, 0)
})

const finalGrade = computed(() => {
  if (!isSubmitted.value) return 0
  const score = (correctAnswersCount.value / questions.length) * 5.0
  return Math.max(0.1, score)
})

const submitExam = () => {
  if (unansweredCount.value > 0) return
  isSubmitted.value = true
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const resetExam = () => {
  userAnswers.value = new Array(questions.length).fill(null)
  isSubmitted.value = false
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const getScoreClass = (grade) => {
  if (grade >= 4.0) return 'excellent'
  if (grade >= 3.0) return 'good'
  return 'poor'
}

const getScoreMessage = (grade) => {
  if (grade >= 4.5) return '¡Sobresaliente! Tienes un excelente dominio de la biología celular.'
  if (grade >= 4.0) return '¡Muy buen trabajo! Tienes bases muy sólidas.'
  if (grade >= 3.0) return 'Aprobado. Tienes conocimientos básicos, pero puedes mejorar repasando el material.'
  return 'No aprobado. Te sugerimos repasar los videos y jugar nuevamente las actividades del laboratorio.'
}
</script>

<style scoped>
.evaluation-container {
  max-width: 900px; margin: 0 auto; padding: 20px 0 60px;
}

.eval-header {
  background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px;
  padding: 30px; margin-bottom: 30px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.eval-title { font-family: 'Orbitron', sans-serif; font-size: 28px; margin-bottom: 15px; }
.eval-title .highlight { color: var(--cyan); }
.eval-desc { color: var(--text-muted); font-size: 15px; max-width: 700px; margin: 0 auto 25px; line-height: 1.5; }

.progress-bar-container { background: rgba(0,0,0,0.2); border-radius: 8px; padding: 15px; }
.progress-text { font-size: 14px; color: var(--cyan); font-weight: bold; margin-bottom: 10px; }
.progress-track { height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden; }
.progress-fill { height: 100%; background: linear-gradient(90deg, #00bfa5, var(--cyan)); transition: width 0.3s ease; }

.questions-list { display: flex; flex-direction: column; gap: 24px; margin-bottom: 40px; }

.question-card {
  background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px;
  padding: 30px; transition: all 0.3s ease; position: relative; overflow: hidden;
}

.question-card::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: transparent; transition: all 0.3s;
}
.question-card.is-answered { border-color: rgba(0,229,255,0.3); }
.question-card.is-answered::before { background: var(--cyan); }
.question-card.is-correct { border-color: rgba(0,191,165,0.5); }
.question-card.is-correct::before { background: #00bfa5; }
.question-card.is-incorrect { border-color: rgba(255,82,82,0.5); }
.question-card.is-incorrect::before { background: #ff5252; }

.question-number { font-family: 'Orbitron', sans-serif; font-size: 13px; color: var(--cyan); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }
.question-statement { font-size: 16px; color: var(--text-main); line-height: 1.5; margin-bottom: 24px; font-weight: 500; }

.options-container { display: flex; flex-direction: column; gap: 12px; }

.option-label {
  display: flex; align-items: center; padding: 16px 20px; background: rgba(255,255,255,0.03);
  border: 1px solid var(--border-color); border-radius: 8px; cursor: pointer; transition: all 0.2s;
  position: relative;
}

.option-label:hover:not(.reveal-correct):not(.reveal-wrong) { background: rgba(0,229,255,0.05); border-color: var(--cyan); }
.option-label.selected { background: rgba(0,229,255,0.1); border-color: var(--cyan); }

.option-label input[type="radio"] { position: absolute; opacity: 0; cursor: pointer; height: 0; width: 0; }
.radio-custom {
  min-width: 20px; height: 20px; border: 2px solid var(--text-muted); border-radius: 50%;
  margin-right: 15px; display: inline-flex; align-items: center; justify-content: center; transition: all 0.2s;
}
.radio-custom::after {
  content: ""; width: 10px; height: 10px; border-radius: 50%; background: var(--cyan);
  transform: scale(0); transition: transform 0.2s;
}
.option-label.selected .radio-custom { border-color: var(--cyan); }
.option-label.selected .radio-custom::after { transform: scale(1); }

.option-text { flex: 1; font-size: 14.5px; color: var(--text-main); line-height: 1.4; }

/* Review Styles */
.option-label.reveal-correct { background: rgba(0,191,165,0.1); border-color: #00bfa5; cursor: default; }
.option-label.reveal-wrong { background: rgba(255,82,82,0.1); border-color: #ff5252; opacity: 0.7; cursor: default; }
.result-icon { font-size: 22px; margin-left: 10px; }
.result-icon.correct { color: #00bfa5; }
.result-icon.wrong { color: #ff5252; }

.feedback-msg { margin-top: 15px; padding: 12px 16px; border-radius: 6px; font-size: 13.5px; display: flex; align-items: center; gap: 8px; }
.feedback-msg.error { background: rgba(255,82,82,0.1); border-left: 3px solid #ff5252; color: #ffb4b4; }
.feedback-msg b { color: white; }

.eval-footer { display: flex; flex-direction: column; align-items: center; }

.submit-section { text-align: center; }
.warning-text { color: #ffca28; font-size: 14px; margin-bottom: 15px; display: flex; align-items: center; justify-content: center; gap: 6px; }

.btn-submit {
  background: var(--bg-card); border: 1px solid var(--border-color); color: var(--text-muted);
  padding: 16px 40px; border-radius: 8px; font-family: 'Orbitron', sans-serif; font-size: 16px;
  font-weight: bold; cursor: not-allowed; display: inline-flex; align-items: center; gap: 10px; transition: all 0.3s;
}
.btn-submit.ready {
  background: linear-gradient(135deg, rgba(0,229,255,0.2), rgba(0,191,165,0.2));
  border-color: var(--cyan); color: var(--cyan); cursor: pointer;
}
.btn-submit.ready:hover {
  background: linear-gradient(135deg, rgba(0,229,255,0.3), rgba(0,191,165,0.3));
  box-shadow: 0 0 25px rgba(0,229,255,0.3); transform: translateY(-2px);
}

.results-section { width: 100%; display: flex; justify-content: center; animation: slideUp 0.5s ease-out; }
.results-card {
  background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px;
  padding: 40px; text-align: center; width: 100%; max-width: 600px; box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}
.results-card h3 { font-family: 'Orbitron', sans-serif; font-size: 24px; color: var(--text-main); margin-bottom: 20px; }

.score-display { display: flex; align-items:baseline; justify-content: center; gap: 5px; margin-bottom: 20px; }
.score-number { font-family: 'Orbitron', sans-serif; font-size: 64px; font-weight: bold; line-height: 1; }
.score-scale { font-size: 24px; color: var(--text-muted); }

.score-number.excellent { color: #00bfa5; text-shadow: 0 0 20px rgba(0,191,165,0.4); }
.score-number.good { color: #ffca28; text-shadow: 0 0 20px rgba(255,202,40,0.4); }
.score-number.poor { color: #ff5252; text-shadow: 0 0 20px rgba(255,82,82,0.4); }

.score-details { font-size: 16px; color: var(--text-muted); margin-bottom: 15px; }
.score-details b { color: var(--text-main); }

.score-message { padding: 15px; border-radius: 8px; font-weight: 500; font-size: 15px; margin-bottom: 30px; }
.score-message.excellent { background: rgba(0,191,165,0.1); border: 1px solid rgba(0,191,165,0.3); color: #00bfa5; }
.score-message.good { background: rgba(255,202,40,0.1); border: 1px solid rgba(255,202,40,0.3); color: #ffca28; }
.score-message.poor { background: rgba(255,82,82,0.1); border: 1px solid rgba(255,82,82,0.3); color: #ff5252; }

.btn-retry {
  background: transparent; border: 1px solid var(--border-color); color: var(--text-main);
  padding: 12px 24px; border-radius: 8px; font-size: 14px; font-weight: bold; cursor: pointer;
  display: inline-flex; align-items: center; gap: 8px; transition: all 0.3s;
}
.btn-retry:hover { border-color: var(--cyan); color: var(--cyan); background: rgba(0,229,255,0.05); }

@keyframes slideUp { from { transform: translateY(30px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

@media (max-width: 768px) {
  .eval-header { padding: 20px; }
  .question-card { padding: 20px; }
  .score-number { font-size: 48px; }
}
</style>
