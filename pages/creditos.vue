<template>
  <NuxtLayout name="dashboard">
    <div class="creditos-container">
      <div class="creditos-header">
        <h2 class="creditos-title">Créditos</h2>
        <p class="creditos-subtitle">BioCell Explorer v1.0 — Objeto Virtual de Aprendizaje</p>
      </div>

      <div class="about-section">
        <h3 class="section-title">Sobre este Proyecto</h3>
        <p class="section-desc">BioCell Explorer es una experiencia educativa interactiva diseñada para estudiantes que desean comprender el fascinante mundo de la biología celular. A través de visualizaciones 3D, videos educativos y actividades prácticas, los usuarios pueden explorar las estructuras y funciones de las células de manera inmersiva.</p>
      </div>

      <div class="team-section">
        <h3 class="section-title">Equipo de Desarrollo</h3>
        <div class="developers-grid">
          <div class="developer-card">
            <div class="card-image">
              <img src="/images/Mateo ayala.jpeg" alt="Mateo Ayala" class="dev-photo">
              <div class="card-overlay">
                <div class="overlay-content">
                  <p class="overlay-role">Desarrollador</p>
                </div>
              </div>
            </div>
            <div class="card-content">
              <h4 class="dev-name">Mateo Ayala</h4>
              <p class="dev-role">Desarrollador Front-End</p>
              <p class="dev-desc">Especializado en interfaces intuitivas y experiencias de usuario memorables.</p>
            </div>
          </div>

          <div class="developer-card">
            <div class="card-image">
              <img src="/images/Maicol pereira.jpeg" alt="Maikol Pereira" class="dev-photo">
              <div class="card-overlay">
                <div class="overlay-content">
                  <p class="overlay-role">Desarrollador</p>
                </div>
              </div>
            </div>
            <div class="card-content">
              <h4 class="dev-name">Maikol Pereira</h4>
              <p class="dev-role">Desarrollador Full-Stack</p>
              <p class="dev-desc">Experto en arquitectura de aplicaciones y soluciones escalables.</p>
            </div>
          </div>
        </div>
      </div>

      <div class="features-section">
        <h3 class="section-title">Características</h3>
        <div class="features-grid">
          <div class="feature-card">
            <i class="mdi mdi-video-outline"></i>
            <h4>Contenido Multimedia</h4>
            <p>Videos educativos de alta calidad sobre biología celular.</p>
          </div>
          <div class="feature-card">
            <i class="mdi mdi-microscope"></i>
            <h4>Laboratorio Interactivo</h4>
            <p>Experimenta con célula y sus componentes en 3D.</p>
          </div>
          <div class="feature-card">
            <i class="mdi mdi-gamepad-variant"></i>
            <h4>Actividades Prácticas</h4>
            <p>Juegos y retos para reforzar el aprendizaje.</p>
          </div>
          <div class="feature-card">
            <i class="mdi mdi-trophy-outline"></i>
            <h4>Sistema de Progreso</h4>
            <p>Sigue tu avance a través del OVA.</p>
          </div>
        </div>
      </div>

      <div class="footer-credits">
        <p class="footer-text">© 2026 BioCell Explorer. Todos los derechos reservados.</p>
        <p class="footer-version">Versión 1.0 · Multi-idioma (ES, EN, PT, FR, AR)</p>
        <NuxtLink :to="{ path: '/dashboard', query: $route.query }" class="btn-back">
          <i class="mdi mdi-arrow-left"></i> Volver al Inicio
        </NuxtLink>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
definePageMeta({ layout: false })
</script>

<style scoped>
:root {
  --bg-main: #020b18;
  --bg-card: #05182e;
  --cyan: #00e5ff;
  --teal: #00bfa5;
  --lime: #76ff03;
  --text-main: rgba(200, 240, 255, 0.9);
  --text-muted: rgba(200, 240, 255, 0.5);
  --border-color: rgba(0, 229, 255, 0.15);
}

.creditos-container {
  max-width: 1200px;
  margin: 0 auto;
}

.creditos-header {
  text-align: center;
  margin-bottom: 50px;
  padding: 30px 0;
  border-bottom: 2px solid var(--border-color);
}

.creditos-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 48px;
  font-weight: 900;
  color: var(--cyan);
  margin: 0 0 10px 0;
  text-shadow: 0 0 20px rgba(0, 229, 255, 0.3);
}

.creditos-subtitle {
  font-size: 14px;
  color: var(--text-muted);
  letter-spacing: 1px;
  margin: 0;
}

.section-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 30px;
  position: relative;
  padding-bottom: 15px;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, var(--cyan), var(--teal));
  border-radius: 2px;
}

.about-section {
  background: linear-gradient(135deg, rgba(0,229,255,0.05), rgba(0,191,165,0.03));
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 30px;
  margin-bottom: 50px;
}

.section-desc {
  font-size: 15px;
  color: var(--text-main);
  line-height: 1.8;
  margin: 0;
}

.team-section {
  margin-bottom: 50px;
}

.developers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.developer-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.developer-card:hover {
  transform: translateY(-8px);
  border-color: var(--cyan);
  box-shadow: 0 15px 40px rgba(0, 229, 255, 0.15);
}

.card-image {
  position: relative;
  width: 100%;
  height: 280px;
  overflow: hidden;
  background: linear-gradient(135deg, rgba(0,229,255,0.1), rgba(0,191,165,0.1));
}

.dev-photo {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.developer-card:hover .dev-photo {
  transform: scale(1.05);
}

.card-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(0, 229, 255, 0.1), rgba(0, 191, 165, 0.1));
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.developer-card:hover .card-overlay {
  opacity: 1;
}

.overlay-content {
  text-align: center;
}

.overlay-role {
  font-size: 14px;
  font-weight: 600;
  color: var(--cyan);
  letter-spacing: 1px;
  text-transform: uppercase;
  margin: 0;
}

.card-content {
  padding: 24px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.dev-name {
  font-family: 'Orbitron', sans-serif;
  font-size: 18px;
  font-weight: 700;
  color: var(--cyan);
  margin: 0 0 6px 0;
}

.dev-role {
  font-size: 12px;
  color: var(--lime);
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
  margin: 0 0 12px 0;
}

.dev-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.6;
  margin: 0;
  flex: 1;
}

.features-section {
  margin-bottom: 50px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.feature-card {
  background: linear-gradient(135deg, rgba(0,229,255,0.05), rgba(0,191,165,0.05));
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  transition: all 0.3s ease;
}

.feature-card:hover {
  border-color: var(--cyan);
  background: linear-gradient(135deg, rgba(0,229,255,0.1), rgba(0,191,165,0.1));
  transform: translateY(-4px);
}

.feature-card i {
  font-size: 40px;
  color: var(--cyan);
  text-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
  margin-bottom: 12px;
}

.feature-card h4 {
  font-family: 'Orbitron', sans-serif;
  font-size: 16px;
  font-weight: 700;
  color: var(--text-main);
  margin: 0 0 8px 0;
}

.feature-card p {
  font-size: 12px;
  color: var(--text-muted);
  margin: 0;
  line-height: 1.6;
}

.footer-credits {
  text-align: center;
  padding: 40px;
  border-top: 2px solid var(--border-color);
  margin-top: 50px;
}

.footer-text {
  font-size: 12px;
  color: var(--text-muted);
  margin: 0 0 4px 0;
  letter-spacing: 0.5px;
}

.footer-version {
  font-size: 11px;
  color: rgba(0, 229, 255, 0.4);
  margin: 0 0 20px 0;
  letter-spacing: 1px;
}

.btn-back {
  display: inline-flex;
  align-items: center;
  gap: 8px;
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
  text-decoration: none;
  transition: all 0.3s ease;
}

.btn-back:hover {
  background: linear-gradient(135deg, rgba(0,229,255,0.3), rgba(0,191,165,0.3));
  box-shadow: 0 0 25px rgba(0,229,255,0.3);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .creditos-title {
    font-size: 32px;
  }

  .section-title {
    font-size: 20px;
  }

  .developers-grid {
    grid-template-columns: 1fr;
  }

  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
