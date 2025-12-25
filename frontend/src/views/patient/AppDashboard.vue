<template>
  <div class="container">
    <h2>Patient Dashboard</h2>
    <ul>
      <li v-for="a in appointments" :key="a.appointment_id">
        {{ a.date }} {{ a.time }} - {{ a.status }}
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
    const res = await api.get("/patient/dashboard")
    this.appointments = res.data
  }
}
</script>
