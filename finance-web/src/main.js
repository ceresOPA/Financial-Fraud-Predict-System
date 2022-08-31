import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

import 'element-plus/dist/index.css'
import ElementPlus from 'element-plus'
import router from './router.js'
import axios from 'axios'

const app = createApp(App)

app.use(router)
app.use(ElementPlus)

app.config.globalProperties.ServerUrl = 'http://localhost:5000'
app.config.globalProperties.$req = axios

app.mount('#app')
