<template>
  <div class="department-page">

    <!-- HEADER -->
    <header class="page-header">
      <h2>Department of {{ department.name }}</h2>

      <div class="header-actions">
        <span @click="viewHistory">History</span>
        <span @click="logout">logout</span>
      </div>
    </header>

    <!-- OVERVIEW -->
    <section class="card">
      <h3>Overview</h3>
      <p class="overview-text">
        {{ department.overview }}
      </p>
    </section>

    <!-- DOCTORS LIST -->
    <section class="card">
      <h3>Doctors' list</h3>

      <div
        class="doctor-row"
        v-for="doctor in doctors"
        :key="doctor.id"
      >
        <span class="doctor-name">
          {{ doctor.name }}
        </span>

        <div class="doctor-actions">
          <button
            class="btn btn-outline"
            @click="checkAvailability(doctor.id)"
          >
            check availability
          </button>

          <button
            class="btn btn-primary"
            @click="viewDoctorDetails(doctor.id)"
          >
            view details
          </button>
        </div>
      </div>

      <div v-if="doctors.length === 0" class="empty-state">
        No doctors available
      </div>
    </section>

  </div>
</template>

<script>
export default {
  name: "DepartmentDetails",

  data() {
    return {
      department: {
        name: "Oncology",
        overview:
          "The Oncology Department in a hospital is dedicated to the diagnosis, treatment, and care of patients with cancer. It houses a team of specialized doctors, such as medical oncologists, surgical oncologists, and radiation oncologists, who work together to provide comprehensive cancer care."
      },

      doctors: [
        { id: 1, name: "Dr. abcde" },
        { id: 2, name: "Dr. pqrst" },
        { id: 3, name: "Dr. mnop" }
      ]
    };
  },

  created() {
    const deptId = this.$route.params.id;
    console.log("Department ID:", deptId);
    // 🔹 fetch department & doctors using deptId (API later)
  },

  methods: {
    viewHistory() {
      console.log("View history");
    },

    logout() {
      console.log("Logout");
    },

    checkAvailability(doctorId) {
      console.log("Check availability:", doctorId);
      // route to availability page later
    },

    viewDoctorDetails(doctorId) {
      console.log("View doctor details:", doctorId);
      // this.$router.push(`/doctor/${doctorId}`)
    }
  }
};
</script>

<style scoped>
/* PAGE */
.department-page {
  padding: 20px;
  font-family: Arial, sans-serif;
}

/* HEADER */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #ddd;
  padding-bottom: 10px;
  margin-bottom: 25px;
}

.header-actions span {
  margin-left: 15px;
  cursor: pointer;
  color: #333;
}

.header-actions span:hover {
  text-decoration: underline;
}

/* CARD */
.card {
  border: 1px solid #ccc;
  padding: 18px;
  margin-bottom: 25px;
  border-radius: 4px;
}

.overview-text {
  margin-top: 10px;
  line-height: 1.6;
  color: #333;
}

/* DOCTORS */
.doctor-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #bbb;
  padding: 12px;
  margin-bottom: 12px;
  border-radius: 4px;
}

.doctor-name {
  font-size: 15px;
}

/* BUTTONS */
.doctor-actions button {
  margin-left: 10px;
}

.btn {
  padding: 6px 14px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
}

.btn-outline {
  background: #fff;
  border: 2px solid #2196f3;
  color: #2196f3;
}

.btn-primary {
  background-color: #2196f3;
  border: none;
  color: #fff;
}

/* EMPTY */
.empty-state {
  text-align: center;
  color: #888;
  padding: 15px;
}
</style>
