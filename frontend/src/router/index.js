import Vue from "vue"
import Router from "vue-router"
import Login from "@/views/AppLogin.vue"
import AdminDashboard from "@/views/admin/AppDashboard.vue"
import DoctorDashboard from "@/views/doctor/AppDashboard.vue"
import PatientDashboard from "@/views/patient/AppDashboard.vue"
import PatientRegister from "@/views/patient/PatientRegister.vue"

Vue.use(Router)

const router = new Router({
  routes: [
    { path: "/", component: Login },
    { path:"/register", component: PatientRegister},
    { path: "/admin", component: AdminDashboard, meta: { role: "ADMIN" }},
    { path: "/doctor", component: DoctorDashboard, meta: { role: "DOCTOR" }},
    { path: "/patient", component: PatientDashboard, meta: { role: "PATIENT" }},
  ]
})

router.beforeEach((to, from, next) => {
  const role = localStorage.getItem("role")
  if (to.meta.role && to.meta.role !== role) {
    next("/")
  } else {
    next()
  }
})

export default router
