<template>
  <div class="container">
    <h2>Admin Dashboard</h2>
    <div class="row">
      <div class="col-md-4" v-for="(v,k) in stats" :key="k">
        <div class="card p-3">{{ k }} : {{ v }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/api/axios"

export default {
  data() {
    return { stats: {} }
  },
  async mounted() {
    const res = await api.get("/admin/dashboard")
    this.stats = res.data
  }
}
</script>

