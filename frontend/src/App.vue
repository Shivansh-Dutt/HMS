<template>
  <div id="app">
    <!-- Global Navbar -->
    <AppNavbar />

    <!-- Page Content -->
    <div class="container mt-4">
      <router-view />
    </div>
  </div>
</template>

<script>
import AppNavbar from "@/components/AppNavbar.vue";

export default {
  name: "App",
  components: {
    AppNavbar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-height: 100vh;
  background-color: #f8f9fa;
}
</style>
