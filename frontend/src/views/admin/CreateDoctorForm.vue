<template>
  <div class="container my-4">
    <h4 class="mb-3">Create Doctor</h4>

    <form @submit.prevent="submit">
      <!-- Email -->
      <div class="mb-3">
        <label class="form-label">Email</label>
        <input
          v-model="doctor.email"
          type="email"
          class="form-control"
          required
        />
      </div>

      <!-- Password -->
      <div class="mb-3">
        <label class="form-label">Password</label>
        <input
          v-model="doctor.password"
          type="password"
          class="form-control"
          minlength="8"
          required
        />
      </div>

      <!-- Specialization -->
      <div class="mb-3">
        <label class="form-label">Specialization</label>
        <input
          v-model="doctor.specialization"
          class="form-control"
          placeholder="e.g. Cardiologist"
        />
      </div>

      <!-- Department ID -->
      <div class="mb-3">
        <label class="form-label">Department ID</label>
        <input
          v-model.number="doctor.department_id"
          type="number"
          class="form-control"
          required
        />
      </div>

      <button class="btn btn-primary">Create</button>
      <button
        type="button"
        class="btn btn-secondary ms-2"
        @click="$router.back()"
      >
        Cancel
      </button>
    </form>
  </div>
</template>

<script>
import { createDoctor } from "@/api/admin";

export default {
  name: "CreateDoctor",

  data() {
    return {
      doctor: {
        email: "",
        password: "",
        specialization: "",
        department_id: null
      }
    };
  },

  methods: {
    async submit() {
      try {
        await createDoctor(this.doctor);
        this.$router.push("/admin"); // optional redirect
      } catch (err) {
        console.error("Create doctor failed", err);
        alert(err?.response?.data?.error || "Failed to create doctor");
      }
    }
  }
};
</script>
