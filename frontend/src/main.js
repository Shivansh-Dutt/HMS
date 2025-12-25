import Vue from "vue"
import App from "./App.vue"
import router from "./router"
import store from "./store"
import VueRouter from "vue-router"

Vue.use(VueRouter)
Vue.config.productionTip = false

new Vue({
  router,
  store, // ✅ THIS LINE FIXES IT
  render: h => h(App),
}).$mount("#app")
