import Vue, { createApp } from '@vue/compat';
import BootstrapVue from "bootstrap-vue";
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')