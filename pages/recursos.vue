<template>
  <NuxtLayout name="dashboard">
    <div class="resources-container">
      <div class="header-section">
        <h2 class="page-title">Biblioteca de <span class="highlight">Recursos</span></h2>
        <p class="page-desc">Explora esta selección de materiales complementarios gratuitos y en español para profundizar tus conocimientos sobre biología celular.</p>
      </div>

      <div class="resources-grid">
        <!-- SECCIÓN: DOCUMENTOS Y ARTÍCULOS -->
        <div class="resource-category">
          <div class="category-header">
            <i class="mdi mdi-book-open-page-variant"></i>
            <h3>Documentos y Portales Educativos</h3>
          </div>
          <div class="cards-wrapper">
            
            <a href="https://es.khanacademy.org/science/biology/structure-of-a-cell" target="_blank" class="resource-card">
              <div class="card-icon docs"><i class="mdi mdi-school"></i></div>
              <div class="card-content">
                <h4>Khan Academy: Estructura Celular</h4>
                <p>Artículos detallados, cuestionarios de práctica y resúmenes completos sobre todos los organelos celulares.</p>
                <span class="resource-type">Portal Educativo</span>
              </div>
              <i class="mdi mdi-open-in-new external-icon"></i>
            </a>

            <a href="https://flexbooks.ck12.org/cbook/ck-12-conceptos-biologia/" target="_blank" class="resource-card">
              <div class="card-icon docs"><i class="mdi mdi-book-education"></i></div>
              <div class="card-content">
                <h4>CK-12: Conceptos de Biología</h4>
                <p>Libro digital de texto libre (Open Educational Resource) con un capítulo extensivo sobre biología celular.</p>
                <span class="resource-type">Libro Digital Libre</span>
              </div>
              <i class="mdi mdi-open-in-new external-icon"></i>
            </a>

            <a href="https://mmegias.webs.uvigo.es/5-celulas/1-introduccion.php" target="_blank" class="resource-card">
              <div class="card-icon docs"><i class="mdi mdi-microscope"></i></div>
              <div class="card-content">
                <h4>Atlas de Histología y Biología Celular</h4>
                <p>Creado por la Universidad de Vigo. Un recurso universitario excelente con micrografías reales y explicaciones rigurosas.</p>
                <span class="resource-type">Atlas Interactivo</span>
              </div>
              <i class="mdi mdi-open-in-new external-icon"></i>
            </a>

          </div>
        </div>

        <!-- SECCIÓN: VIDEOS SUPLEMENTARIOS -->
        <div class="resource-category">
          <div class="category-header">
            <i class="mdi mdi-youtube"></i>
            <h3>Canales y Series de Video</h3>
          </div>
          <div class="cards-wrapper">

            <a href="https://www.youtube.com/@AmoebaSistersEspanol" target="_blank" class="resource-card">
              <div class="card-icon videos"><i class="mdi mdi-animation-play"></i></div>
              <div class="card-content">
                <h4>Amoeba Sisters en Español</h4>
                <p>Canal de YouTube famoso por explicar conceptos complejos de biología usando animaciones amigables y mucho humor.</p>
                <span class="resource-type">Canal de YouTube</span>
              </div>
              <i class="mdi mdi-open-in-new external-icon"></i>
            </a>

            <a href="https://www.youtube.com/playlist?list=PL2VAlBsswL_0o7tQpB4e4-7y2b7fI0A3b" target="_blank" class="resource-card">
              <div class="card-icon videos"><i class="mdi mdi-play-network"></i></div>
              <div class="card-content">
                <h4>Crash Course Biología (Español)</h4>
                <p>Lista de reproducción oficial doblada al español del exitoso curso de biología dictado originalmente por Hank Green.</p>
                <span class="resource-type">Serie de Videos</span>
              </div>
              <i class="mdi mdi-open-in-new external-icon"></i>
            </a>

            <a href="https://www.youtube.com/@Biologiadesdecero" target="_blank" class="resource-card">
              <div class="card-icon videos"><i class="mdi mdi-video-vintage"></i></div>
              <div class="card-content">
                <h4>Biología Desde Cero</h4>
                <p>Canal enfocado en microscopía. Perfecto para ver cómo se ven las células reales, protistas y bacterias bajo el microscopio.</p>
                <span class="resource-type">Microscopía Real</span>
              </div>
              <i class="mdi mdi-open-in-new external-icon"></i>
            </a>

          </div>
        </div>

        <!-- SECCIÓN: HERRAMIENTAS INTERACTIVAS -->
        <div class="resource-category">
          <div class="category-header">
            <i class="mdi mdi-cube-scan"></i>
            <h3>Herramientas 3D e Interactivos</h3>
          </div>
          <div class="cards-wrapper">

            <a href="https://learn.genetics.utah.edu/content/cells/scale/" target="_blank" class="resource-card">
              <div class="card-icon tools"><i class="mdi mdi-ruler"></i></div>
              <div class="card-content">
                <h4>Cell Size and Scale (Utah Genetics)</h4>
                <p>Deslizador interactivo para entender la escala microscópica, desde un grano de café hasta un átomo de carbono.</p>
                <span class="resource-type">Interactiva (Inglés/Intuitivo)</span>
              </div>
              <i class="mdi mdi-open-in-new external-icon"></i>
            </a>

          </div>
        </div>

      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
definePageMeta({ layout: false })
</script>

<style scoped>
.resources-container {
  max-width: 1000px; margin: 0 auto; padding: 20px 0 60px;
}

.header-section {
  text-align: center; margin-bottom: 40px; background: var(--bg-card);
  border: 1px solid var(--border-color); border-radius: 16px; padding: 30px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.page-title { font-family: 'Orbitron', sans-serif; font-size: 32px; margin-bottom: 15px; }
.page-title .highlight { color: var(--cyan); }
.page-desc { color: var(--text-muted); font-size: 16px; max-width: 700px; margin: 0 auto; line-height: 1.5; }

.resources-grid { display: flex; flex-direction: column; gap: 40px; }

.category-header { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid var(--border-color); }
.category-header i { font-size: 28px; color: var(--cyan); }
.category-header h3 { font-family: 'Orbitron', sans-serif; font-size: 20px; color: var(--text-main); font-weight: 500; }

.cards-wrapper { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }

.resource-card {
  background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px;
  padding: 24px; display: flex; align-items: flex-start; gap: 16px; text-decoration: none;
  transition: all 0.3s ease; position: relative; overflow: hidden;
}

.resource-card:hover { border-color: var(--cyan); transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,229,255,0.1); }
.resource-card:hover::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--cyan); }

.card-icon { width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0; }
.card-icon.docs { background: rgba(0, 191, 165, 0.1); color: #00bfa5; }
.card-icon.videos { background: rgba(255, 82, 82, 0.1); color: #ff5252; }
.card-icon.tools { background: rgba(170, 0, 255, 0.1); color: #aa00ff; }

.card-content { flex: 1; }
.card-content h4 { color: var(--text-main); font-size: 16px; margin-bottom: 8px; line-height: 1.3; }
.card-content p { color: var(--text-muted); font-size: 13px; margin-bottom: 12px; line-height: 1.5; }
.resource-type { display: inline-block; padding: 4px 10px; background: rgba(255,255,255,0.05); border-radius: 4px; font-size: 11px; color: var(--cyan); text-transform: uppercase; letter-spacing: 0.5px; font-weight: bold; }

.external-icon { position: absolute; top: 20px; right: 20px; color: var(--border-color); font-size: 18px; transition: color 0.3s; }
.resource-card:hover .external-icon { color: var(--cyan); }

@media (max-width: 768px) {
  .cards-wrapper { grid-template-columns: 1fr; }
  .resource-card { padding: 20px; }
}
</style>
