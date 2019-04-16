import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import routes from './router';
import VueFire from "vuefire";
import VueChartkick from 'vue-chartkick'
import Chart from 'chart.js'

Vue.use(VueChartkick, {adapter: Chart})
Vue.use(VueRouter)
Vue.use(VueFire);

Vue.config.productionTip = false
const router = new VueRouter({routes, mode: "history"});

new Vue({
  render: h => h(App),
  router
}).$mount('#app')