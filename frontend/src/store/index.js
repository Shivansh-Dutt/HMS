import Vue from "vue"
import Vuex from "vuex"
import auth from "./modules/auth"
// import admin from "./modules/admin"
// import doctor from "./modules/doctor"
// import patient from "./modules/patient"

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { auth }
})
