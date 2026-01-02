import Vue from "vue"
import Router from "vue-router"
import store from "@/store" // your Vuex store
import Login from "@/views/AppLogin.vue"
import AdminDashboard from "@/views/admin/AppDashboard.vue"
import DoctorDashboard from "@/views/doctor/AppDashboard.vue"
import PatientDashboard from "@/views/patient/AppDashboard.vue"
import PatientRegister from "@/views/patient/PatientRegister.vue"
import CreateDoctorForm from "@/views/admin/CreateDoctorForm.vue"
import DepartmentDetails from "@/views/patient/DepartmentDetails.vue"
import DoctorDetails from "@/views/patient/DoctorDetails.vue"

Vue.use(Router)

const router = new Router({
  routes: [
    { path: "/", component: Login },
    { path:"/register", component: PatientRegister},
    { path: "/admin/doctors/create",component: CreateDoctorForm,meta:{role:"ADMIN"}},
    { path: "/admin", component: AdminDashboard, meta: { role: "ADMIN" }},
    { path: "/doctor", component: DoctorDashboard, meta: { role: "DOCTOR" }},
    { path: "/patient", component: PatientDashboard, meta: { role: "PATIENT" }},
    { path: "/department/:id", component: DepartmentDetails },
    { path: "/doctor/:id", component: DoctorDetails }
  ]
})

router.beforeEach(async (to, from, next) => {
  if (!store.state.auth.loaded){
    await store.dispatch("auth/fetchUser")
  }
  const role = store.state.auth.role
  if (to.meta.role && to.meta.role !== role) {
    next("/")
  } else {
    next()
  }
})

export default router
