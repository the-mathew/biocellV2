<template>
  <div class="home-wrapper">

    <div class="cell-canvas">
      <div
        v-for="cell in cells"
        :key="cell.id"
        class="floating-cell"
        :style="cell.style"
      >
        <svg :width="cell.size" :height="cell.size" viewBox="0 0 100 100">

          <circle
            cx="50" cy="50" :r="cell.outerR"
            :fill="`rgba(${cell.color}, 0.04)`"
            :stroke="`rgba(${cell.color}, ${cell.opacity})`"
            stroke-width="1.5"
          />

          <circle
            cx="50" cy="50" :r="cell.nucleusR"
            :fill="`rgba(${cell.color}, 0.08)`"
            :stroke="`rgba(${cell.color}, ${cell.opacity * 1.5})`"
            stroke-width="1"
          />

          <circle
            cx="50" cy="50" :r="cell.nucleusR * 0.4"
            :fill="`rgba(${cell.color}, 0.2)`"
          />
          
          <ellipse
            v-for="(m, i) in cell.mitos"
            :key="i"
            :cx="m.cx" :cy="m.cy"
            rx="4" ry="2"
            :fill="`rgba(${cell.color}, 0.15)`"
            :stroke="`rgba(${cell.color}, 0.4)`"
            stroke-width="0.8"
            :transform="`rotate(${m.angle}, ${m.cx}, ${m.cy})`"
          />
        </svg>
      </div>

      <!-- Partículas de ADN / puntos -->
      <div
        v-for="p in particles"
        :key="`p-${p.id}`"
        class="particle"
        :style="p.style"
      />

      <!-- Líneas de conexión decorativas -->
      <svg class="connection-lines" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:rgba(0,229,255,0);stop-opacity:1" />
            <stop offset="50%" style="stop-color:rgba(0,229,255,0.3);stop-opacity:1" />
            <stop offset="100%" style="stop-color:rgba(0,229,255,0);stop-opacity:1" />
          </linearGradient>
        </defs>
        <line v-for="l in lines" :key="`l-${l.id}`"
          :x1="l.x1" :y1="l.y1" :x2="l.x2" :y2="l.y2"
          stroke="url(#lineGrad)" stroke-width="0.5"
          :opacity="l.opacity"
          class="anim-line"
          :style="`animation-delay: ${l.delay}s`"
        />
      </svg>
    </div>

    <!-- ══════════════════════════════════════════
         GRADIENTE RADIAL CENTRAL
    ══════════════════════════════════════════ -->
    <div class="radial-glow" />

    <!-- ══════════════════════════════════════════
         CONTENIDO PRINCIPAL
    ══════════════════════════════════════════ -->
    <div class="main-content">

      <!-- LOGO -->
      <div class="logo-container" :class="{ 'logo-visible': loaded }">
        <div class="logo-ring logo-ring-outer" />
        <div class="logo-ring logo-ring-mid" />
        <div class="logo-core">
          <svg width="80" height="80" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <!-- Membrana celular -->
            <circle cx="50" cy="50" r="44" fill="none" stroke="rgba(0,229,255,0.6)" stroke-width="1.5" stroke-dasharray="4 3"/>
            <!-- Citoplasma -->
            <circle cx="50" cy="50" r="38" fill="rgba(0,229,255,0.05)" />
            <!-- Núcleo principal -->
            <circle cx="50" cy="50" r="22" fill="rgba(0,191,165,0.15)" stroke="rgba(0,229,255,0.8)" stroke-width="1.5"/>
            <!-- Nucléolo -->
            <circle cx="50" cy="50" r="9" fill="rgba(0,229,255,0.5)" />
            <!-- Mitocondrias -->
            <ellipse cx="28" cy="38" rx="7" ry="3.5" fill="rgba(118,255,3,0.3)" stroke="rgba(118,255,3,0.6)" stroke-width="1" transform="rotate(-30,28,38)"/>
            <ellipse cx="72" cy="62" rx="7" ry="3.5" fill="rgba(118,255,3,0.3)" stroke="rgba(118,255,3,0.6)" stroke-width="1" transform="rotate(145,72,62)"/>
            <ellipse cx="68" cy="30" rx="5" ry="2.5" fill="rgba(0,229,255,0.25)" stroke="rgba(0,229,255,0.5)" stroke-width="0.8" transform="rotate(60,68,30)"/>
            <!-- Retículo endoplásmico (curvas) -->
            <path d="M 20 55 Q 35 48 30 62" fill="none" stroke="rgba(0,229,255,0.35)" stroke-width="1.2" stroke-linecap="round"/>
            <path d="M 75 40 Q 62 48 70 36" fill="none" stroke="rgba(0,229,255,0.35)" stroke-width="1.2" stroke-linecap="round"/>
            <!-- Ribosomas -->
            <circle cx="36" cy="26" r="2" fill="rgba(0,229,255,0.6)"/>
            <circle cx="65" cy="75" r="2" fill="rgba(0,229,255,0.6)"/>
            <circle cx="24" cy="66" r="1.5" fill="rgba(118,255,3,0.7)"/>
            <circle cx="78" cy="44" r="1.5" fill="rgba(118,255,3,0.7)"/>
          </svg>
        </div>
      </div>

      <!-- TÍTULO -->
      <div class="title-block" :class="{ 'title-visible': loaded }">
        <div class="subtitle-top">OBJETO VIRTUAL DE APRENDIZAJE</div>
        <h1 class="main-title">
          <span class="title-bio">Bio</span><span class="title-cell">Cell</span>
          <br />
          <span class="title-explorer">Explorer</span>
        </h1>
        <div class="title-divider">
          <div class="divider-line" />
          <div class="divider-icon">⬡</div>
          <div class="divider-line" />
        </div>
        <p class="tagline">
          Explora el fascinante universo microscópico<br/>
          de las <em>células</em> y sus componentes
        </p>
      </div>

      <!-- BOTÓN DE INICIO -->
      <div class="cta-block" :class="{ 'cta-visible': loaded }">
        <button class="btn-start" @click="openDialog">
          <span class="btn-inner">
            <span class="btn-icon"><i class="mdi mdi-play" style="font-size: 14px;"></i></span>
            <span class="btn-text">INICIAR EXPLORACIÓN</span>
          </span>
          <div class="btn-glow" />
        </button>
        <div class="version-tag">v1.0 · Biología Celular</div>
      </div>

    </div>

    <!-- ══════════════════════════════════════════
         DIÁLOGO DE BIENVENIDA
    ══════════════════════════════════════════ -->
    <v-dialog v-model="dialog" max-width="480" :scrim="'rgba(2,11,24,0.85)'">
      <v-card class="welcome-card">
        <!-- Header del diálogo -->
        <div class="dialog-header">
          <div class="dialog-cell-icon">
            <svg width="48" height="48" viewBox="0 0 100 100">
              <circle cx="50" cy="50" r="44" fill="none" stroke="rgba(0,229,255,0.5)" stroke-width="1.5" stroke-dasharray="4 3"/>
              <circle cx="50" cy="50" r="22" fill="rgba(0,191,165,0.15)" stroke="rgba(0,229,255,0.8)" stroke-width="1.5"/>
              <circle cx="50" cy="50" r="9" fill="rgba(0,229,255,0.5)"/>
            </svg>
          </div>
          <h2 class="dialog-title">¡Bienvenido al laboratorio!</h2>
          <p class="dialog-subtitle">Antes de comenzar, ¿cómo te llamas?</p>
        </div>

        <v-card-text class="dialog-body">
          <div class="input-wrapper">
            <label class="input-label">NOMBRE DEL EXPLORADOR</label>
            <input
              v-model="nameInput"
              class="bio-input"
              type="text"
              placeholder="Escribe tu nombre aquí..."
              @keyup.enter="confirmStart"
              ref="nameField"
              maxlength="40"
            />
            <div class="input-line" :class="{ active: nameInput.length > 0 }" />
          </div>

          <p v-if="nameError" class="name-error">
            ⚠ Por favor ingresa tu nombre para continuar
          </p>
        </v-card-text>

        <v-card-actions class="dialog-actions">
          <button class="btn-cancel" @click="closeDialog">
            <i class="mdi mdi-close" style="font-size: 14px; margin-right: 4px;"></i> Cancelar
          </button>
          <button class="btn-confirm" @click="confirmStart">
            <i class="mdi mdi-flask-outline" style="font-size: 16px;"></i>
            <span>Entrar al laboratorio</span>
            <span class="confirm-arrow"><i class="mdi mdi-arrow-right"></i></span>
          </button>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'

const emit = defineEmits(['start'])

const dialog = ref(false)
const nameInput = ref('')
const nameError = ref(false)
const nameField = ref(null)
const loaded = ref(false)

// ─── Generación de células flotantes ───────────────────────────────────────
const COLORS = [
  '0,229,255',   // cyan
  '0,191,165',   // teal
  '118,255,3',   // lime
  '0,150,255',   // blue
]

function randomBetween(a, b) {
  return a + Math.random() * (b - a)
}

function makeMitos(count) {
  const mitos = []
  for (let i = 0; i < count; i++) {
    const angle = (i / count) * 360
    const rad = (angle * Math.PI) / 180
    const dist = randomBetween(26, 35)
    mitos.push({
      cx: 50 + dist * Math.cos(rad),
      cy: 50 + dist * Math.sin(rad),
      angle: angle + 90,
    })
  }
  return mitos
}

const cells = Array.from({ length: 14 }, (_, i) => {
  const size = randomBetween(60, 180)
  const color = COLORS[i % COLORS.length]
  const outerR = randomBetween(38, 45)
  const nucleusR = randomBetween(14, 20)
  const opacity = randomBetween(0.08, 0.25)
  const duration = randomBetween(8, 18)
  const delay = randomBetween(-20, 0)
  const x = randomBetween(-5, 105)
  const y = randomBetween(-5, 105)
  const driftX = randomBetween(-250, 250)
  const driftY = randomBetween(-250, 250)
  const rot = randomBetween(-45, 45)

  return {
    id: i,
    size,
    color,
    outerR,
    nucleusR,
    opacity,
    mitos: makeMitos(randomBetween(3, 6)),
    style: {
      width: `${size}px`,
      height: `${size}px`,
      left: `${x}%`,
      top: `${y}%`,
      animation: `floatCell ${duration}s ${delay}s ease-in-out infinite alternate`,
      '--drift-x': `${driftX}px`,
      '--drift-y': `${driftY}px`,
      '--rot': `${rot}deg`,
    },
  }
})

// ─── Partículas ────────────────────────────────────────────────────────────
const particles = Array.from({ length: 40 }, (_, i) => {
  const size = randomBetween(1, 3.5)
  const color = COLORS[i % COLORS.length]
  const duration = randomBetween(6, 14)
  const delay = randomBetween(-15, 0)
  const moveX = randomBetween(-300, 300)
  const moveY = randomBetween(-300, 300)
  return {
    id: i,
    style: {
      width: `${size}px`,
      height: `${size}px`,
      left: `${randomBetween(0, 100)}%`,
      top: `${randomBetween(0, 100)}%`,
      background: `rgba(${color}, ${randomBetween(0.4, 0.9)})`,
      boxShadow: `0 0 ${size * 3}px rgba(${color}, 0.6)`,
      animation: `moveParticle ${duration}s ${delay}s ease-in-out infinite alternate`,
      '--move-x': `${moveX}px`,
      '--move-y': `${moveY}px`,
    },
  }
})

// ─── Líneas de conexión ─────────────────────────────────────────────────────
const lines = Array.from({ length: 8 }, (_, i) => ({
  id: i,
  x1: `${randomBetween(5, 45)}%`,
  y1: `${randomBetween(10, 90)}%`,
  x2: `${randomBetween(55, 95)}%`,
  y2: `${randomBetween(10, 90)}%`,
  opacity: randomBetween(0.15, 0.4),
  delay: randomBetween(0, 4),
}))

// ─── Métodos ────────────────────────────────────────────────────────────────
function openDialog() {
  dialog.value = true
  nameError.value = false
  nameInput.value = ''
  nextTick(() => nameField.value?.focus())
}

function closeDialog() {
  dialog.value = false
  nameError.value = false
}

function confirmStart() {
  if (!nameInput.value.trim()) {
    nameError.value = true
    return
  }
  dialog.value = false
  emit('start', nameInput.value.trim())
}

onMounted(() => {
  setTimeout(() => { loaded.value = true }, 100)
})
</script>

<style scoped>
/* ═══════════════════════════════════════════════
   WRAPPER BASE
═══════════════════════════════════════════════ */
.home-wrapper {
  position: fixed;
  inset: 0;
  background: radial-gradient(ellipse at 50% 40%, #031526 0%, #020b18 70%);
  overflow: hidden;
  font-family: 'Exo 2', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ═══════════════════════════════════════════════
   FONDO ANIMADO
═══════════════════════════════════════════════ */
.cell-canvas {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.floating-cell {
  position: absolute;
  transform: translate(-50%, -50%);
  filter: blur(0.3px);
}

.particle {
  position: absolute;
  border-radius: 50%;
  transform: translate(-50%, -50%);
}

.connection-lines {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.anim-line {
  animation: lineFlash 6s ease-in-out infinite;
}

.radial-glow {
  position: absolute;
  width: 700px;
  height: 700px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle, rgba(0,191,165,0.07) 0%, rgba(0,229,255,0.04) 35%, transparent 70%);
  pointer-events: none;
  animation: pulse 5s ease-in-out infinite;
}

/* ═══════════════════════════════════════════════
   CONTENIDO PRINCIPAL
═══════════════════════════════════════════════ */
.main-content {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 28px;
  text-align: center;
  padding: 24px;
}

/* ═══════════════════════════════════════════════
   LOGO
═══════════════════════════════════════════════ */
.logo-container {
  position: relative;
  width: 130px;
  height: 130px;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transform: scale(0.6) translateY(-20px);
  transition: all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.logo-container.logo-visible {
  opacity: 1;
  transform: scale(1) translateY(0);
}

.logo-ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid rgba(0, 229, 255, 0.2);
}

.logo-ring-outer {
  width: 130px;
  height: 130px;
  border-color: rgba(0, 229, 255, 0.15);
  animation: spinSlow 20s linear infinite;
  border-style: dashed;
}

.logo-ring-mid {
  width: 105px;
  height: 105px;
  border-color: rgba(0, 191, 165, 0.25);
  animation: spinSlow 14s linear infinite reverse;
}

.logo-core {
  width: 88px;
  height: 88px;
  border-radius: 50%;
  background: radial-gradient(circle at 40% 35%, rgba(0,229,255,0.12), rgba(0,191,165,0.06));
  border: 1.5px solid rgba(0,229,255,0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow:
    0 0 25px rgba(0,229,255,0.25),
    inset 0 0 20px rgba(0,229,255,0.08);
  animation: coreGlow 4s ease-in-out infinite;
}

/* ═══════════════════════════════════════════════
   TÍTULO
═══════════════════════════════════════════════ */
.title-block {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s cubic-bezier(0.22, 1, 0.36, 1) 0.35s;
}

.title-block.title-visible {
  opacity: 1;
  transform: translateY(0);
}

.subtitle-top {
  font-family: 'Exo 2', sans-serif;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 4px;
  color: rgba(0, 229, 255, 0.55);
  margin-bottom: 10px;
  text-transform: uppercase;
}

.main-title {
  font-family: 'Orbitron', sans-serif;
  line-height: 1;
  margin-bottom: 16px;
}

.title-bio {
  font-size: clamp(42px, 7vw, 68px);
  font-weight: 900;
  color: #00e5ff;
  text-shadow: var(--glow-cyan);
  letter-spacing: -1px;
}

.title-cell {
  font-size: clamp(42px, 7vw, 68px);
  font-weight: 900;
  color: #76ff03;
  text-shadow: var(--glow-lime);
  letter-spacing: -1px;
}

.title-explorer {
  font-size: clamp(28px, 4.5vw, 44px);
  font-weight: 400;
  color: rgba(0, 229, 255, 0.7);
  letter-spacing: 8px;
  text-transform: uppercase;
}

.title-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  justify-content: center;
  margin-bottom: 14px;
}

.divider-line {
  flex: 1;
  max-width: 80px;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(0,229,255,0.4), transparent);
}

.divider-icon {
  color: rgba(0, 229, 255, 0.5);
  font-size: 14px;
  animation: spin 8s linear infinite;
}

.tagline {
  font-family: 'Exo 2', sans-serif;
  font-size: 14px;
  font-weight: 300;
  color: rgba(200, 240, 255, 0.55);
  line-height: 1.7;
  letter-spacing: 0.5px;
}

.tagline em {
  color: rgba(0,229,255,0.8);
  font-style: normal;
  font-weight: 500;
}

/* ═══════════════════════════════════════════════
   BOTÓN DE INICIO
═══════════════════════════════════════════════ */
.cta-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.7s cubic-bezier(0.22, 1, 0.36, 1) 0.65s;
}

.cta-block.cta-visible {
  opacity: 1;
  transform: translateY(0);
}

.btn-start {
  position: relative;
  background: transparent;
  border: 1.5px solid rgba(0, 229, 255, 0.5);
  padding: 0;
  border-radius: 4px;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.3s ease;
}

.btn-start:hover {
  border-color: rgba(0, 229, 255, 0.9);
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(0,229,255,0.3), 0 0 60px rgba(0,229,255,0.1);
}

.btn-start:hover .btn-glow {
  opacity: 1;
}

.btn-inner {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 15px 36px;
  position: relative;
  z-index: 1;
}

.btn-icon {
  font-size: 12px;
  color: #76ff03;
  text-shadow: var(--glow-lime);
  animation: blink 2s ease-in-out infinite;
}

.btn-text {
  font-family: 'Orbitron', sans-serif;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 3px;
  color: #00e5ff;
  text-shadow: 0 0 15px rgba(0,229,255,0.5);
}

.btn-glow {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(0,229,255,0.08), rgba(0,191,165,0.12));
  opacity: 0;
  transition: opacity 0.3s ease;
}

.version-tag {
  font-family: 'Exo 2', sans-serif;
  font-size: 10px;
  letter-spacing: 2px;
  color: rgba(0,229,255,0.25);
  text-transform: uppercase;
}

/* ═══════════════════════════════════════════════
   DIÁLOGO
═══════════════════════════════════════════════ */
.welcome-card {
  background: #040f1e !important;
  border: 1px solid rgba(0,229,255,0.2) !important;
  border-radius: 8px !important;
  overflow: hidden;
}

.dialog-header {
  padding: 32px 32px 16px;
  text-align: center;
  border-bottom: 1px solid rgba(0,229,255,0.08);
  background: linear-gradient(180deg, rgba(0,229,255,0.04) 0%, transparent 100%);
}

.dialog-cell-icon {
  display: flex;
  justify-content: center;
  margin-bottom: 16px;
  animation: coreGlow 3s ease-in-out infinite;
}

.dialog-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 18px;
  font-weight: 700;
  color: #00e5ff;
  letter-spacing: 1px;
  margin-bottom: 8px;
  text-shadow: 0 0 20px rgba(0,229,255,0.4);
}

.dialog-subtitle {
  font-family: 'Exo 2', sans-serif;
  font-size: 13px;
  color: rgba(200, 240, 255, 0.5);
  letter-spacing: 0.5px;
}

.dialog-body {
  padding: 24px 32px !important;
}

.input-wrapper {
  position: relative;
}

.input-label {
  display: block;
  font-family: 'Exo 2', sans-serif;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 3px;
  color: rgba(0,229,255,0.5);
  margin-bottom: 10px;
}

.bio-input {
  width: 100%;
  background: transparent;
  border: none;
  outline: none;
  font-family: 'Exo 2', sans-serif;
  font-size: 18px;
  font-weight: 400;
  color: rgba(200, 240, 255, 0.9);
  padding: 8px 0;
  letter-spacing: 1px;
}

.bio-input::placeholder {
  color: rgba(200, 240, 255, 0.2);
  font-weight: 300;
}

.input-line {
  height: 1.5px;
  background: rgba(0,229,255,0.2);
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
}

.input-line::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, #00e5ff, rgba(118,255,3,0.8), transparent);
  transform: translateX(-100%);
  transition: transform 0.4s ease;
}

.input-line.active::after {
  transform: translateX(0);
}

.input-line.active {
  background: rgba(0,229,255,0.4);
  box-shadow: 0 0 8px rgba(0,229,255,0.3);
}

.name-error {
  font-family: 'Exo 2', sans-serif;
  font-size: 12px;
  color: #ff5252;
  margin-top: 10px;
  letter-spacing: 0.5px;
}

.dialog-actions {
  padding: 16px 32px 24px !important;
  display: flex;
  justify-content: space-between;
  gap: 12px;
}

.btn-cancel {
  background: transparent;
  border: 1px solid rgba(255,255,255,0.1);
  color: rgba(255,255,255,0.35);
  padding: 10px 20px;
  border-radius: 4px;
  font-family: 'Exo 2', sans-serif;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s ease;
  letter-spacing: 1px;
}

.btn-cancel:hover {
  border-color: rgba(255,255,255,0.25);
  color: rgba(255,255,255,0.55);
}

.btn-confirm {
  flex: 1;
  background: linear-gradient(135deg, rgba(0,229,255,0.15), rgba(0,191,165,0.2));
  border: 1.5px solid rgba(0,229,255,0.5);
  color: #00e5ff;
  padding: 12px 24px;
  border-radius: 4px;
  font-family: 'Orbitron', sans-serif;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 2px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  transition: all 0.3s ease;
}

.btn-confirm:hover {
  background: linear-gradient(135deg, rgba(0,229,255,0.25), rgba(0,191,165,0.3));
  box-shadow: 0 4px 20px rgba(0,229,255,0.25);
  transform: translateY(-1px);
}

.confirm-arrow {
  font-size: 16px;
  transition: transform 0.3s ease;
}

.btn-confirm:hover .confirm-arrow {
  transform: translateX(4px);
}

</style>

<style>
/* ═══════════════════════════════════════════════
   KEYFRAMES
═══════════════════════════════════════════════ */
@keyframes floatCell {
  0%   { transform: translate(-50%, -50%) rotate(0deg); }
  100% { transform: translate(calc(-50% + var(--drift-x)), calc(-50% + var(--drift-y))) rotate(var(--rot)); }
}

@keyframes moveParticle {
  0% { 
    opacity: 0.2; 
    transform: translate(-50%, -50%) scale(0.8); 
  }
  50% { 
    opacity: 1; 
    transform: translate(calc(-50% + var(--move-x) / 2), calc(-50% + var(--move-y) / 2)) scale(1.3); 
  }
  100% { 
    opacity: 0.2; 
    transform: translate(calc(-50% + var(--move-x)), calc(-50% + var(--move-y))) scale(0.8); 
  }
}

@keyframes lineFlash {
  0%, 100% { opacity: 0; }
  40%, 60% { opacity: 1; }
}

@keyframes spinSlow {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

@keyframes coreGlow {
  0%, 100% { box-shadow: 0 0 20px rgba(0,229,255,0.2), inset 0 0 15px rgba(0,229,255,0.06); }
  50%       { box-shadow: 0 0 40px rgba(0,229,255,0.4), inset 0 0 25px rgba(0,229,255,0.12); }
}

@keyframes pulse {
  0%, 100% { opacity: 0.6; transform: translate(-50%,-50%) scale(1); }
  50%       { opacity: 1;   transform: translate(-50%,-50%) scale(1.08); }
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.3; }
}
</style>
