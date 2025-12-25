<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">HMS</a>

    <div class="collapse navbar-collapse">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item" v-if="role">
          <a class="nav-link" href="#" @click.prevent="logout">Logout</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  computed: {
    role() {
      return this.$store.state.auth.role
    }
  },
  methods: {
    logout() {
      this.$store.dispatch("auth/logout")
      this.$router.push("/")
    }
  }
}
</script>
