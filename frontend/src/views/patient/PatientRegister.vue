<template>
  <div class="container mt-5">
    <h3>Register Form</h3>
    <input v-model="email" class="form-control" placeholder="Email" />
    <input v-model="password" type="password" class="form-control mt-2" placeholder="Password" />
    <input v-model="age" type="Number" placeholder="age">
    <input v-model="contact_no"  type="text" placeholder="contact_no">
    <input v-model="address" type="text" placeholder="address">
    <button class="btn btn-primary mt-3" @click="Register">Register</button>
  </div>
</template>

<script>
import { patientRegisterAPI } from '@/api/patient';

export default {
  data() {
    return { email: "", password: "" , age:"",  contact_no: "" ,address:"" }
  },
  methods: {
    async Register() {
      const res = await patientRegisterAPI({
        email: this.email,
        password: this.password,
        age: this.age,
        contact_no:this.contact_no,
        address:this.address
      })
      console.log(res)
      this.$router.push(`/`)
    }
  }
}
</script>
