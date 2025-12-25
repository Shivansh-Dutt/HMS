<template>
  <div class="container">
    <h2>Doctor Dashboard</h2>
    <ul>
      <li v-for="a in appointments" :key="a.appointment_id">
        {{ a.date }} {{ a.time }} - {{ a.patient_email }}
      </li>
    </ul>
  </div>
</template>

<script>
import api from "@/api/axios"

export default {
  data() {
    return { appointments: [] }
  },
  async mounted() {
    const res = await api.get("/doctor/dashboard")
    this.appointments = res.data
  }
}
</script>
