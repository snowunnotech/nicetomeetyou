import Vue from 'vue'
import App from './App.vue'
import Router from './router'
import BootstrapVue from 'bootstrap-vue'
import {BPagination} from 'bootstrap-vue'
import axios from 'axios'

Vue.use(BootstrapVue)
Vue.config.productionTip = false

import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import "font-awesome/css/font-awesome.css"

axios.defaults.baseURL = 'https://django-nba.herokuapp.com'

Vue.component('b-pagination', BPagination)

new Vue({
  el: '#app',
  router: Router,
  components: {App},
  render: h => h(App)
})
