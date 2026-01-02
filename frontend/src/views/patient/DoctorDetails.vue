<template>
  <div class="doctor-profile">

    <header class="profile-header">
      <h2>{{ doctor.name }}</h2>
    </header>

    <div class="profile-main">

      <div class="profile-info">
        <p><strong>{{ doctor.qualifications }}</strong></p>
        <p>{{ doctor.specialization }}</p>
        <p>{{ doctor.yearsExperience }} Years Experience Overall</p>
        <p>({{ doctor.yearsAsSpecialist }} years as specialist)</p>

        <p class="description">
          {{ doctor.description }}
        </p>
      </div>

      <div class="profile-photo">
        <div class="photo-placeholder">
          <span class="icon-user"></span>
        </div>
      </div>
    </div>

    <div class="actions">
      <button class="btn btn-outline" @click="checkAvailability">
        check availability
      </button>
      <button class="btn btn-primary" @click="goBack">
        Go Back
      </button>
    </div>

  </div>
</template>

<script>
export default {
  name: "DoctorProfile",

  data() {
    return {
      doctor: {
        name: "Dr. mnop",
        qualifications: "MBBS, DM - Medical Oncology",
        specialization: "Medical Oncologist",
        yearsExperience: 20,
        yearsAsSpecialist: 11,
        description:
          "Dr. mnop is a Medical Oncologist in Indiar and has an experience of 20 years in this field."
      }
    };
  },

  methods: {
    checkAvailability() {
      console.log("Check availability for", this.doctor.name);
      // Implement availability check or route to calendar page
    },

    goBack() {
      this.$router.go(-1); // Go back in history
    }
  }
};
</script>

<style scoped>
.doctor-profile {
  padding: 20px;
  font-family: Arial, sans-serif;
}

/* Header */
.profile-header {
  margin-bottom: 20px;
}

/* Main container */
.profile-main {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 25px;
}

/* Info section */
.profile-info {
  max-width: 60%;
  font-size: 14px;
  line-height: 1.5;
  color: #333;
}

/* Description paragraph */
.description {
  margin-top: 15px;
}

/* Profile photo placeholder */
.profile-photo {
  width: 100px;
  height: 100px;
  border: 2px solid #ccc;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #eee;
}

.photo-placeholder .icon-user {
  font-size: 48px;
  color: #999;
  /* Simple user icon using unicode */
}

/* Buttons */
.actions {
  display: flex;
  gap: 12px;
}

.btn {
  padding: 8px 20px;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  border: none;
}

.btn-outline {
  background: #fff;
  border: 2px solid #2196f3;
  color: #2196f3;
}

.btn-primary {
  background-color: #2196f3;
  color: #fff;
}
</style>
