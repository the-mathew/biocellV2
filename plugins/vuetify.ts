import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    ssr: true,
    theme: {
      defaultTheme: 'bioCellDark',
      themes: {
        bioCellDark: {
          dark: true,
          colors: {
            background: '#020b18',
            surface: '#040f1e',
            primary: '#00e5ff',
            secondary: '#76ff03',
            accent: '#00bfa5',
          },
        },
      },
    },
  })
  app.vueApp.use(vuetify)
})
