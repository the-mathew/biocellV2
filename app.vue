<template>
  <v-app>
    <NuxtPage />
  </v-app>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Exo+2:wght@300;400;500;600&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  --cyan: #00e5ff;
  --teal: #00bfa5;
  --lime: #76ff03;
  --navy: #020b18;
  --navy2: #051428;
  --bg-main: #020b18;
  --bg-sidebar: #041224;
  --bg-card: #05182e;
  --bg-card-hover: #07213d;
  --text-main: rgba(200, 240, 255, 0.9);
  --text-muted: rgba(200, 240, 255, 0.5);
  --border-color: rgba(0, 229, 255, 0.15);
  --glow-cyan: 0 0 20px rgba(0, 229, 255, 0.6), 0 0 60px rgba(0, 229, 255, 0.2);
  --glow-lime: 0 0 20px rgba(118, 255, 3, 0.5), 0 0 50px rgba(118, 255, 3, 0.15);
}

html, body {
  background-color: var(--navy);
  overflow: hidden;
  font-family: 'Exo 2', sans-serif;
  color: var(--text-main);
}
</style>
