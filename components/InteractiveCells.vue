<template>
  <div class="interactive-cells-container">
    <div class="cells-header">
      <div class="header-text">
        <h2 class="section-title">Laboratorio Interactivo: <span class="highlight">La Célula</span></h2>
        <p class="section-desc">Selecciona un tipo de célula y haz clic en sus organelos para descubrir su función.</p>
      </div>
      
      <div class="cell-type-selector">
        <button 
          class="type-btn" 
          :class="{ active: activeCellType === 'animal' }"
          @click="setActiveCell('animal')"
        >
          <i class="mdi mdi-paw"></i> Célula Animal
        </button>
        <button 
          class="type-btn" 
          :class="{ active: activeCellType === 'vegetal' }"
          @click="setActiveCell('vegetal')"
        >
          <i class="mdi mdi-leaf"></i> Célula Vegetal
        </button>
      </div>
    </div>

    <div class="cell-workspace">
      <!-- Célula SVG -->
      <div class="cell-svg-container">
        <div class="svg-hint" v-if="!activeOrganelle">
          <i class="mdi mdi-hand-pointing-up"></i> Toca los organelos
        </div>
        
        <!-- Animal Cell SVG - Improved 3D -->
        <svg v-if="activeCellType === 'animal'" viewBox="0 0 500 500" class="cell-svg">
          <defs>
            <!-- Enhanced gradients for 3D effect -->
            <radialGradient id="animal-bg-3d" cx="45%" cy="40%" r="65%">
              <stop offset="0%" stop-color="rgba(50,120,180,0.35)"/>
              <stop offset="35%" stop-color="rgba(20,60,100,0.25)"/>
              <stop offset="70%" stop-color="rgba(10,30,50,0.15)"/>
              <stop offset="100%" stop-color="#020b18"/>
            </radialGradient>
            <radialGradient id="cyto-grad-3d" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="rgba(0,229,255,0.08)"/>
              <stop offset="70%" stop-color="rgba(0,229,255,0.03)"/>
              <stop offset="100%" stop-color="rgba(0,229,255,0)"/>
            </radialGradient>
            <radialGradient id="nuc-grad-3d" cx="35%" cy="30%" r="70%">
              <stop offset="0%" stop-color="#bb86fc"/>
              <stop offset="40%" stop-color="#9c27b0"/>
              <stop offset="70%" stop-color="#6a1b9a"/>
              <stop offset="100%" stop-color="#38006b"/>
            </radialGradient>
            <filter id="glow-3d"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
            <filter id="glow-3d-strong"><feGaussianBlur stdDeviation="8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
            <filter id="shadow-3d"><feGaussianBlur in="SourceAlpha" stdDeviation="3"/><feOffset dx="2" dy="4" result="offsetblur"/><feMerge><feMergeNode in="offsetblur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
          </defs>
          
          <!-- Membrana plasmática mejorada -->
          <ellipse cx="250" cy="250" rx="220" ry="210" fill="url(#animal-bg-3d)" stroke="rgba(0,229,255,0.8)" stroke-width="4" stroke-dasharray="15 8" filter="url(#shadow-3d)"
            class="organelle" :class="{ active: activeOrganelleId === 'membrana' }"
            @click.stop="selectOrganelle('animal', 'membrana')"/>
          
          <!-- Citoplasm -->
          <circle cx="250" cy="250" r="200" fill="url(#cyto-grad-3d)" 
            class="organelle-bg" :class="{ active: activeOrganelleId === 'citoplasma' }"
            @click.stop="selectOrganelle('animal', 'citoplasma')"/>

          <!-- Núcleo mejorado - más 3D -->
          <g class="organelle" :class="{ active: activeOrganelleId === 'nucleo' }" @click.stop="selectOrganelle('animal', 'nucleo')">
            <!-- Nuclear envelope -->
            <circle cx="250" cy="250" r="65" fill="none" stroke="rgba(188,134,252,0.4)" stroke-width="2.5" stroke-dasharray="5 5"/>
            <!-- Main nucleus -->
            <circle cx="250" cy="250" r="58" fill="url(#nuc-grad-3d)" stroke="#d500f9" stroke-width="3.5" filter="url(#glow-3d-strong)"/>
            <!-- Nucleolus -->
            <circle cx="265" cy="235" r="18" fill="#6a1b9a" stroke="rgba(213,0,249,0.7)" stroke-width="2" filter="url(#glow-3d)"/>
            <!-- Chromatin structure -->
            <path d="M 230 230 Q 250 210 270 230" fill="none" stroke="rgba(210,140,255,0.4)" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M 235 260 Q 250 275 265 260" fill="none" stroke="rgba(210,140,255,0.3)" stroke-width="2" stroke-linecap="round"/>
          </g>

          <!-- Mitocondrias mejoradas -->
          <g class="organelle" :class="{ active: activeOrganelleId === 'mitocondria' }" @click.stop="selectOrganelle('animal', 'mitocondria')">
            <!-- Mitochondria 1 -->
            <ellipse cx="140" cy="180" rx="42" ry="24" fill="#ff6f00" stroke="#ffb74d" stroke-width="3" transform="rotate(35,140,180)" filter="url(#glow-3d)"/>
            <path d="M 115 175 Q 130 160 145 175" fill="none" stroke="#ffe0b2" stroke-width="2" transform="rotate(35,140,180)" stroke-linecap="round"/>
            <path d="M 130 185 Q 145 170 160 185" fill="none" stroke="#ffe0b2" stroke-width="2" transform="rotate(35,140,180)" stroke-linecap="round"/>
            <!-- Mitochondria 2 -->
            <ellipse cx="360" cy="320" rx="38" ry="22" fill="#ff6f00" stroke="#ffb74d" stroke-width="3" transform="rotate(-30,360,320)" filter="url(#glow-3d)"/>
            <path d="M 340 315 Q 355 300 370 315" fill="none" stroke="#ffe0b2" stroke-width="2" transform="rotate(-30,360,320)" stroke-linecap="round"/>
            <!-- Mitochondria 3 (small) -->
            <ellipse cx="320" cy="160" rx="26" ry="14" fill="#ff6f00" stroke="#ffb74d" stroke-width="2.5" transform="rotate(60,320,160)" filter="url(#glow-3d)"/>
          </g>

          <!-- Golgi Apparatus mejorado -->
          <g class="organelle" :class="{ active: activeOrganelleId === 'golgi' }" @click.stop="selectOrganelle('animal', 'golgi')">
            <path d="M 340 370 Q 375 350 405 370" fill="rgba(0,230,118,0.2)" stroke="#00ff00" stroke-width="7" stroke-linecap="round" filter="url(#glow-3d)"/>
            <path d="M 345 355 Q 380 335 410 355" fill="rgba(0,230,118,0.15)" stroke="#66ff00" stroke-width="7" stroke-linecap="round" filter="url(#glow-3d)"/>
            <path d="M 350 340 Q 385 320 415 340" fill="rgba(0,230,118,0.1)" stroke="#76ff03" stroke-width="6" stroke-linecap="round" filter="url(#glow-3d)"/>
            <!-- Vesicles -->
            <circle cx="420" cy="345" r="7" fill="rgba(0,230,118,0.5)" stroke="#66ff00" stroke-width="2" filter="url(#glow-3d)"/>
            <circle cx="425" cy="365" r="5" fill="rgba(0,230,118,0.4)" stroke="#66ff00" stroke-width="1.5"/>
          </g>

          <!-- Lisosomas mejorados -->
          <g class="organelle" :class="{ active: activeOrganelleId === 'lisosoma' }" @click.stop="selectOrganelle('animal', 'lisosoma')">
            <circle cx="180" cy="370" r="20" fill="rgba(233,30,99,0.6)" stroke="#ff4081" stroke-width="2.5" filter="url(#glow-3d)"/>
            <circle cx="175" cy="365" r="3.5" fill="rgba(255,150,200,0.6)"/><circle cx="188" cy="375" r="3" fill="rgba(255,150,200,0.5)"/>
            <circle cx="120" cy="310" r="15" fill="rgba(233,30,99,0.5)" stroke="#ff4081" stroke-width="2" filter="url(#glow-3d)"/>
            <circle cx="117" cy="306" r="2.5" fill="rgba(255,150,200,0.5)"/>
          </g>

          <!-- Retículo Endoplasmático -->
          <g class="organelle" :class="{ active: activeOrganelleId === 'reticulo' }" @click.stop="selectOrganelle('animal', 'reticulo')">
            <path d="M 170 200 Q 160 170 180 150" fill="none" stroke="#2979ff" stroke-width="5" stroke-linecap="round" filter="url(#glow-3d)"/>
            <path d="M 155 225 Q 140 190 160 160" fill="none" stroke="#2979ff" stroke-width="4" stroke-linecap="round" filter="url(#glow-3d)"/>
            <path d="M 190 180 Q 200 150 215 160" fill="none" stroke="#2979ff" stroke-width="4" stroke-linecap="round" filter="url(#glow-3d)"/>
            <!-- Ribosomes on ER -->
            <circle cx="170" cy="150" r="3.5" fill="#64b5f6" filter="url(#glow-3d)"/><circle cx="155" cy="185" r="3" fill="#64b5f6"/><circle cx="172" cy="205" r="3" fill="#64b5f6"/>
          </g>

          <!-- Free ribosomes -->
          <circle cx="350" cy="420" r="4" fill="rgba(100,181,246,0.6)" filter="url(#glow-3d)"/>
          <circle cx="380" cy="440" r="3.5" fill="rgba(100,181,246,0.5)"/>
          <circle cx="120" cy="150" r="3" fill="rgba(100,181,246,0.5)"/>
          <circle cx="400" cy="200" r="3" fill="rgba(100,181,246,0.4)"/>
        </svg>


        <svg v-if="activeCellType === 'vegetal'" viewBox="0 0 500 500" class="cell-svg">
          <defs>
            <radialGradient id="veg-bg-3d" cx="50%" cy="45%" r="60%">
              <stop offset="0%" stop-color="rgba(0,120,0,0.25)"/>
              <stop offset="50%" stop-color="rgba(0,60,0,0.15)"/>
              <stop offset="100%" stop-color="#001a00"/>
            </radialGradient>
            <linearGradient id="chloro-grad-3d" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#2e7d32"/><stop offset="40%" stop-color="#00ff41"/><stop offset="100%" stop-color="#69f0ae"/>
            </linearGradient>
            <linearGradient id="veg-mito-grad-3d" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#e65100"/><stop offset="50%" stop-color="#ff6f00"/><stop offset="100%" stop-color="#ff9100"/>
            </linearGradient>
            <filter id="glow-veg-3d"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
            <filter id="glow-veg-3d-strong"><feGaussianBlur stdDeviation="8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
          </defs>
          
          <!-- Pared Celular (Rigida y cúbica) -->
          <rect x="25" y="25" width="450" height="450" rx="15" fill="url(#veg-bg-3d)" stroke="#76ff03" stroke-width="9" stroke-dasharray="20 10" filter="url(#shadow-3d)"
            class="organelle" :class="{ active: activeOrganelleId === 'pared' }"
            @click.stop="selectOrganelle('vegetal', 'pared')" />
          
          <!-- Membrana Celular (debajo de la pared) -->
          <rect x="45" y="45" width="410" height="410" rx="12" fill="none" stroke="rgba(0,229,255,0.6)" stroke-width="3.5" stroke-dasharray="8 5"
            class="organelle" :class="{ active: activeOrganelleId === 'membrana' }"
            @click.stop="selectOrganelle('vegetal', 'membrana')" />

          <!-- Gran Vacuola Central -->
          <g class="organelle" :class="{ active: activeOrganelleId === 'vacuola' }" @click.stop="selectOrganelle('vegetal', 'vacuola')">
            <ellipse cx="250" cy="250" rx="140" ry="130" fill="rgba(0,229,255,0.15)" stroke="rgba(0,229,255,0.6)" stroke-width="3" filter="url(#glow-veg-3d-strong)"/>
            <!-- Water content shimmer -->
            <path d="M 130 200 Q 250 180 370 200" fill="none" stroke="rgba(0,229,255,0.12)" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M 120 260 Q 250 240 380 260" fill="none" stroke="rgba(0,229,255,0.1)" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M 140 310 Q 250 300 360 310" fill="none" stroke="rgba(0,229,255,0.08)" stroke-width="1.5" stroke-linecap="round"/>
          </g>

          <!-- Núcleo (desplazado por la vacuola) -->
          <g class="organelle" :class="{ active: activeOrganelleId === 'nucleo' }" @click.stop="selectOrganelle('vegetal', 'nucleo')">
            <circle cx="400" cy="400" r="50" fill="none" stroke="rgba(188,134,252,0.4)" stroke-width="2.5" stroke-dasharray="6 4"/>
            <circle cx="400" cy="400" r="44" fill="#7c4dff" stroke="#d500f9" stroke-width="3.5" filter="url(#glow-veg-3d-strong)"/>
            <!-- Chromatin -->
            <path d="M 385 385 Q 400 375 415 390" fill="none" stroke="rgba(210,140,255,0.4)" stroke-width="2" stroke-linecap="round"/>
            <!-- Nucleolus -->
            <circle cx="408" cy="395" r="14" fill="#6a1b9a" stroke="rgba(213,0,249,0.6)" stroke-width="1.5" filter="url(#glow-veg-3d)"/>
          </g>

          <!-- Cloroplastos (organelo clave de plantas) -->
          <g class="organelle" :class="{ active: activeOrganelleId === 'cloroplasto' }" @click.stop="selectOrganelle('vegetal', 'cloroplasto')">
            <!-- Chloroplast 1 - Upper left -->
            <ellipse cx="95" cy="420" rx="38" ry="22" fill="url(#chloro-grad-3d)" stroke="#76ff03" stroke-width="3" transform="rotate(-20,95,420)" filter="url(#glow-veg-3d)"/>
            <!-- Grana stacks -->
            <line x1="75" y1="418" x2="75" y2="422" stroke="#00ff00" stroke-width="5" transform="rotate(-20,95,420)" stroke-linecap="round"/>
            <line x1="87" y1="415" x2="87" y2="425" stroke="#00ff00" stroke-width="5" transform="rotate(-20,95,420)" stroke-linecap="round"/>
            <line x1="99" y1="415" x2="99" y2="425" stroke="#00ff00" stroke-width="5" transform="rotate(-20,95,420)" stroke-linecap="round"/>
            <line x1="111" y1="418" x2="111" y2="422" stroke="#00ff00" stroke-width="5" transform="rotate(-20,95,420)" stroke-linecap="round"/>
            
            <!-- Chloroplast 2 - Upper right -->
            <ellipse cx="385" cy="75" rx="42" ry="24" fill="url(#chloro-grad-3d)" stroke="#76ff03" stroke-width="3" transform="rotate(35,385,75)" filter="url(#glow-veg-3d)"/>
            <line x1="363" y1="73" x2="363" y2="77" stroke="#00ff00" stroke-width="5" transform="rotate(35,385,75)" stroke-linecap="round"/>
            <line x1="376" y1="70" x2="376" y2="80" stroke="#00ff00" stroke-width="5" transform="rotate(35,385,75)" stroke-linecap="round"/>
            <line x1="389" y1="70" x2="389" y2="80" stroke="#00ff00" stroke-width="5" transform="rotate(35,385,75)" stroke-linecap="round"/>
            <line x1="402" y1="73" x2="402" y2="77" stroke="#00ff00" stroke-width="5" transform="rotate(35,385,75)" stroke-linecap="round"/>
            
            <!-- Chloroplast 3 - Left side (small) -->
            <ellipse cx="75" cy="190" rx="28" ry="16" fill="url(#chloro-grad-3d)" stroke="#76ff03" stroke-width="2.5" transform="rotate(50,75,190)" filter="url(#glow-veg-3d)"/>
            <line x1="62" y1="188" x2="62" y2="192" stroke="#00ff00" stroke-width="4" transform="rotate(50,75,190)"/>
            <line x1="75" y1="185" x2="75" y2="195" stroke="#00ff00" stroke-width="4" transform="rotate(50,75,190)"/>
            <line x1="88" y1="188" x2="88" y2="192" stroke="#00ff00" stroke-width="4" transform="rotate(50,75,190)"/>
          </g>

          <!-- Mitocondrias (para noche/oscuridad) -->
          <g class="organelle" :class="{ active: activeOrganelleId === 'mitocondria' }" @click.stop="selectOrganelle('vegetal', 'mitocondria')">
            <!-- Mito 1 -->
            <ellipse cx="420" cy="240" rx="32" ry="18" fill="url(#veg-mito-grad-3d)" stroke="#ffb74d" stroke-width="2.5" transform="rotate(65,420,240)" filter="url(#glow-veg-3d)"/>
            <path d="M 405 235 Q 420 222 435 235" fill="none" stroke="#ffe0b2" stroke-width="2" transform="rotate(65,420,240)" stroke-linecap="round"/>
            <path d="M 413 245 Q 420 235 427 245" fill="none" stroke="#ffe0b2" stroke-width="1.5" transform="rotate(65,420,240)"/>
            
            <!-- Mito 2 (smaller) -->
            <ellipse cx="100" cy="100" rx="22" ry="12" fill="url(#veg-mito-grad-3d)" stroke="#ffb74d" stroke-width="2" transform="rotate(40,100,100)" filter="url(#glow-veg-3d)"/>
            <path d="M 90 96 Q 100 86 110 96" fill="none" stroke="#ffe0b2" stroke-width="1.5" transform="rotate(40,100,100)"/>
          </g>
        </svg>
      </div>

      <!-- Panel de Información -->
      <transition name="slide-fade" mode="out-in">
        <div class="info-panel" v-if="activeOrganelle" :key="activeOrganelleId">
          <div class="organelle-image-container" v-if="activeOrganelle.image">
            <img :src="activeOrganelle.image" :alt="activeOrganelle.name" class="organelle-real-img" />
          </div>
          <div class="info-header">
            <div class="info-icon">
              <i :class="activeOrganelle.icon"></i>
            </div>
            <h3>{{ activeOrganelle.name }}</h3>
          </div>
          <div class="info-body">
            <p>{{ activeOrganelle.description }}</p>
            <div class="info-fact">
              <i class="mdi mdi-lightbulb-on-outline"></i>
              <span>{{ activeOrganelle.fact }}</span>
            </div>
          </div>
        </div>
        <div class="info-panel placeholder-info" v-else key="empty">
          <div class="placeholder-content">
            <i class="mdi mdi-cursor-default-click-outline pulse-icon"></i>
            <h3>Interacción Celular</h3>
            <p>Haz clic en cualquier organelo de la célula a tu izquierda para descubrir su nombre y función específica.</p>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const activeCellType = ref('animal')
const activeOrganelleId = ref(null)

const organelleData = {
  animal: {
    membrana: {
      name: 'Membrana Celular',
      icon: 'mdi-shield-outline',
      description: 'Es una barrera semipermeable y flexible compuesta por una doble capa de fosfolípidos. Su función principal es proteger la célula y regular estrictamente qué nutrientes entran y qué sustancias de desecho salen, manteniendo el equilibrio interno (homeostasis).',
      fact: 'Es como el guardia de seguridad fronterizo de la célula.'
    },
    citoplasma: {
      name: 'Citoplasma',
      icon: 'mdi-water',
      description: 'El citoplasma es la matriz gelatinosa que llena el interior de la célula. Está formado principalmente por agua, sales y proteínas. Es el escenario donde ocurren la mayoría de las reacciones químicas vitales y donde "flotan" todos los demás organelos.',
      fact: 'Si la célula fuera una piscina, el citoplasma sería el agua donde nadan los organelos.'
    },
    nucleo: {
      name: 'Núcleo Celular',
      icon: 'mdi-nucleus',
      image: '/images/nucleus_render.png',
      description: 'El núcleo es el orgánulo más prominente y actúa como el centro de mando. Alberga el ADN, que contiene todas las instrucciones genéticas necesarias para el crecimiento, desarrollo y reproducción de la célula. Está protegido por su propia membrana nuclear.',
      fact: 'Funciona como el "cerebro" o la biblioteca central de la célula.'
    },
    mitocondria: {
      name: 'Mitocondria',
      icon: 'mdi-flash',
      image: '/images/mitochondria_render.png',
      description: 'La mitocondria es responsable de la respiración celular. Absorbe los nutrientes (como la glucosa) y el oxígeno, y los transforma en ATP, la molécula de energía que utiliza la célula para realizar todas sus funciones vitales. Tienen su propio ADN.',
      fact: 'Son conocidas mundialmente como las "centrales eléctricas" de la célula.'
    },
    golgi: {
      name: 'Aparato de Golgi',
      icon: 'mdi-layers-outline',
      image: '/images/golgi_render.png',
      description: 'Este complejo sistema de sacos aplanados se encarga de modificar, clasificar y empaquetar proteínas y lípidos producidos por el retículo endoplasmático. Luego, los distribuye en vesículas hacia su destino final, ya sea dentro o fuera de la célula.',
      fact: 'Es como la oficina central de correos y logística celular.'
    },
    reticulo: {
      name: 'Retículo Endoplasmático',
      icon: 'mdi-chart-timeline-variant-shimmer',
      description: 'Es una extensa red de membranas interconectadas. El retículo "rugoso" (cubierto de ribosomas) sintetiza proteínas, mientras que el retículo "liso" se encarga de la síntesis de lípidos (grasas) y la desintoxicación de sustancias químicas.',
      fact: 'Es como la gran fábrica de ensamblaje de la célula.'
    },
    lisosoma: {
      name: 'Lisosoma',
      icon: 'mdi-delete-empty-outline',
      description: 'Son vesículas esféricas que contienen potentes enzimas digestivas. Su misión es descomponer macromoléculas, destruir bacterias invasoras y reciclar componentes celulares viejos o dañados, manteniendo la célula limpia.',
      fact: 'Funcionan como los centros de reciclaje y eliminación de residuos.'
    }
  },
  vegetal: {
    pared: {
      name: 'Pared Celular',
      icon: 'mdi-wall',
      description: 'Estructura rígida y gruesa compuesta de celulosa que se encuentra solo en las células vegetales (y algunos otros organismos). Su función es proporcionar soporte estructural, dar forma y proteger a la planta de presiones mecánicas.',
      fact: 'Es la razón por la que los árboles pueden crecer tan altos sin huesos.'
    },
    membrana: {
      name: 'Membrana Celular',
      icon: 'mdi-shield-outline',
      description: 'Situada justo debajo de la rígida pared celular, esta barrera de lípidos regula minuciosamente el paso de sustancias vitales y desechos.',
      fact: 'Actúa como la segunda línea de defensa.'
    },
    vacuola: {
      name: 'Gran Vacuola Central',
      icon: 'mdi-water-outline',
      description: 'Es una enorme vesícula llena de líquido (agua, enzimas y nutrientes). Mantiene la presión de turgencia, que es lo que mantiene a las plantas erguidas. Si la vacuola pierde agua, la planta se marchita.',
      fact: 'Puede llegar a ocupar hasta el 90% del volumen total de la célula vegetal.'
    },
    nucleo: {
      name: 'Núcleo',
      icon: 'mdi-nucleus',
      image: '/images/nucleus_render.png',
      description: 'Contiene todo el material genético de la planta y coordina las actividades de síntesis de proteínas y división celular.',
      fact: 'En las plantas adultas, la enorme vacuola suele empujar al núcleo hacia una esquina.'
    },
    cloroplasto: {
      name: 'Cloroplasto',
      icon: 'mdi-leaf',
      image: '/images/chloroplast_render.png',
      description: 'Estos fascinantes organelos contienen clorofila, el pigmento verde que capta la luz del sol. Realizan la fotosíntesis, un proceso vital donde combinan luz solar, agua y dióxido de carbono para producir oxígeno y glucosa (el alimento de la planta).',
      fact: 'Son la razón fundamental del color verde de la naturaleza.'
    },
    mitocondria: {
      name: 'Mitocondria',
      icon: 'mdi-flash',
      image: '/images/mitochondria_render.png',
      description: 'Al igual que en los animales, las mitocondrias de las plantas toman el alimento (producido en los cloroplastos) y lo convierten en energía utilizable (ATP) durante la noche o cuando no hay luz solar directa.',
      fact: 'Incluso las plantas "respiran" y necesitan de estas centrales eléctricas.'
    }
  }
}

const activeOrganelle = computed(() => {
  if (!activeOrganelleId.value) return null
  return organelleData[activeCellType.value][activeOrganelleId.value]
})

const setActiveCell = (type) => {
  activeCellType.value = type
  activeOrganelleId.value = null // reset info
}

const selectOrganelle = (type, id) => {
  if (activeCellType.value !== type) return
  activeOrganelleId.value = id
}
</script>

<style scoped>
.interactive-cells-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  height: 100%;
}

.cells-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--bg-card);
  padding: 20px 30px;
  border-radius: 12px;
  border: 1px solid var(--border-color);
}

.section-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 24px;
  margin-bottom: 8px;
}
.section-title .highlight { color: var(--cyan); }
.section-desc { color: var(--text-muted); font-size: 14px; }

.cell-type-selector {
  display: flex;
  gap: 12px;
  background: rgba(0, 0, 0, 0.3);
  padding: 6px;
  border-radius: 12px;
}

.type-btn {
  background: transparent;
  color: var(--text-muted);
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
}

.type-btn:hover { color: var(--text-main); }
.type-btn.active {
  background: var(--cyan);
  color: var(--bg-main);
}

.cell-workspace {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
  flex: 1;
}

/* VISOR DE CELULAS */
.cell-svg-container {
  background: radial-gradient(circle at center, rgba(0, 229, 255, 0.08) 0%, rgba(2, 11, 24, 0.95) 100%);
  border: 1px solid rgba(0, 229, 255, 0.2);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  min-height: 500px;
  box-shadow: inset 0 0 80px rgba(0, 229, 255, 0.05), 0 10px 30px rgba(0,0,0,0.5);
}

.cell-svg-container::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(0,229,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,229,255,0.03) 1px, transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
}

.cell-svg {
  width: 90%;
  max-width: 500px;
  max-height: 90%;
  filter: drop-shadow(0 0 25px rgba(0,229,255,0.15));
  animation: floatCell 6s ease-in-out infinite;
}

@keyframes floatCell {
  0%, 100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-12px) scale(1.01); }
}

.svg-hint {
  position: absolute;
  top: 20px;
  left: 20px;
  background: rgba(0, 229, 255, 0.15);
  border: 1px solid var(--cyan);
  color: var(--cyan);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  animation: pulse-border 2s infinite;
}

@keyframes pulse-border {
  0% { box-shadow: 0 0 0 0 rgba(0, 229, 255, 0.4); }
  70% { box-shadow: 0 0 0 10px rgba(0, 229, 255, 0); }
  100% { box-shadow: 0 0 0 0 rgba(0, 229, 255, 0); }
}

.cell-svg {
  width: 90%;
  max-width: 500px;
  max-height: 90%;
}

.organelle {
  cursor: pointer;
  transition: all 0.3s ease;
  transform-origin: center;
}

.organelle:hover {
  filter: brightness(1.3) drop-shadow(0 0 10px rgba(255,255,255,0.3));
}

.organelle.active {
  filter: brightness(1.5) drop-shadow(0 0 15px rgba(255,255,255,0.5));
}

.organelle-bg {
  cursor: pointer;
}
.organelle-bg:hover { fill: rgba(255,255,255,0.02); }

/* PANEL DE INFORMACION */
.info-panel {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.organelle-image-container {
  width: 100%;
  height: 220px;
  background: #000;
  border-bottom: 2px solid var(--cyan);
  overflow: hidden;
  position: relative;
}

.organelle-real-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.organelle-image-container:hover .organelle-real-img {
  transform: scale(1.05);
}

.info-header {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 24px 30px 16px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.info-icon {
  width: 50px;
  height: 50px;
  background: rgba(0, 229, 255, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  color: var(--cyan);
}

.info-header h3 {
  font-size: 22px;
  color: var(--text-main);
  margin: 0;
}

.info-body {
  padding: 20px 30px 30px;
}

.info-body p {
  font-size: 14px;
  line-height: 1.7;
  color: var(--text-muted);
  margin-bottom: 24px;
}

.info-fact {
  background: linear-gradient(90deg, rgba(118, 255, 3, 0.1) 0%, transparent 100%);
  border-left: 3px solid var(--lime);
  padding: 16px;
  border-radius: 0 8px 8px 0;
  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.info-fact i {
  color: var(--lime);
  font-size: 20px;
  margin-top: -2px;
}

.info-fact span {
  font-size: 13px;
  color: var(--text-main);
  line-height: 1.5;
  font-style: italic;
}

.placeholder-info {
  align-items: center;
  justify-content: center;
  text-align: center;
  background: linear-gradient(180deg, var(--bg-card) 0%, rgba(2,11,24,0.5) 100%);
}

.placeholder-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  opacity: 0.6;
}

.pulse-icon {
  font-size: 60px;
  color: var(--cyan);
  margin-bottom: 20px;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0); }
}

.placeholder-content h3 {
  font-family: 'Orbitron', sans-serif;
  color: var(--text-main);
  margin-bottom: 12px;
}

.placeholder-content p {
  font-size: 14px;
  color: var(--text-muted);
  max-width: 250px;
}

/* Transiciones */
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}
.slide-fade-leave-active {
  transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>
