<template>
  <div class="container mt-5">
    <h3>Login</h3>
    <input v-model="email" class="form-control" placeholder="Email" />
    <input v-model="password" type="password" class="form-control mt-2" placeholder="Password" />
    <button class="btn btn-primary mt-3" @click="login">Login</button>
  </div>
</template>

<script>
export default {
  data() {
    return { email: "", password: "" }
  },
  methods: {
    async login() {
      await this.$store.dispatch("auth/login", {
        email: this.email,
        password: this.password
      })
      const role = this.$store.state.auth.role
      this.$router.push(`/${role.toLowerCase()}`)
    }
  }
}
</script>
