<template>
  <div class="dashboard">

    <!-- HEADER -->
    <header class="dashboard-header">
      <h2>Welcome {{ patientName }}</h2>

      <nav class="header-actions">
        <span @click="editProfile">edit profile</span> |
        <span @click="viewHistory">History</span> |
        <span @click="logout">logout</span>
      </nav>
    </header>

    <!-- DEPARTMENTS -->
    <section class="card">
      <h3>Departments</h3>

      <div
        class="department-row"
        v-for="dept in departments"
        :key="dept.id"
      >
        <span class="dept-name">{{ dept.name }}</span>

        <button
          class="btn btn-primary"
          @click="viewDepartment(dept.id)"
        >
          view details
        </button>
      </div>
    </section>

    <!-- UPCOMING APPOINTMENTS -->
    <section class="card">
      <h3>Upcoming Appointments</h3>

      <table class="appointments-table">
        <thead>
          <tr>
            <th>Sr No.</th>
            <th>Doctor Name</th>
            <th>Deptt</th>
            <th>Date</th>
            <th>Time</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="(ap, index) in upcomingAppointments"
            :key="ap.id"
          >
            <td>{{ index + 1 }}</td>
            <td>{{ ap.doctor }}</td>
            <td>{{ ap.department }}</td>
            <td>{{ ap.date }}</td>
            <td>{{ ap.time }}</td>
            <td>
              <button
                class="btn btn-danger"
                @click="cancelAppointment(ap.id)"
              >
                cancel
              </button>
            </td>
          </tr>

          <tr v-if="upcomingAppointments.length === 0">
            <td colspan="6" class="empty-state">
              No upcoming appointments
            </td>
          </tr>
        </tbody>
      </table>
    </section>

  </div>
</template>

<script>
import api from '@/api/axios';

export default {
  name: "PatientDashboard",

  data() {
    return {
      patientName: "Pqrst",

      departments: [],

      upcomingAppointments: [
        {
          id: 1,
          doctor: "Dr. abcde",
          department: "General",
          date: "24/09/2025",
          time: "08 am - 12 pm"
        }
      ]
    };
  },

  created() {
    this.getPatientDashboard()
  },

  methods: {
    async getPatientDashboard(){
      const patientDashboardres = await api.get("/patient/dashboard")
      this.departments = patientDashboardres.data.all_departments
    },
    // HEADER
    editProfile() {
      console.log("Edit profile");
    },

    viewHistory() {
      console.log("View history");
    },

    logout() {
      console.log("Logout");
    },

    // DEPARTMENTS
    viewDepartment(deptId) {
      this.$router.push(`/department/${deptId}`)
      console.log("View department:", deptId);
    },

    // APPOINTMENTS
    cancelAppointment(appointmentId) {
      console.log("Cancel appointment:", appointmentId);
    }
  }
};
</script>

<style scoped>
/* GENERAL */
.dashboard {
  padding: 20px;
  font-family: Arial, sans-serif;
}

/* HEADER */
.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #ddd;
  padding-bottom: 10px;
  margin-bottom: 25px;
}

.header-actions span {
  cursor: pointer;
  color: #333;
  font-size: 14px;
}

.header-actions span:hover {
  text-decoration: underline;
}

/* CARD */
.card {
  border: 1px solid #ccc;
  padding: 15px;
  margin-bottom: 25px;
  border-radius: 4px;
}

/* DEPARTMENTS */
.department-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 4px;
}

.dept-name {
  font-size: 15px;
}

/* TABLE */
.appointments-table {
  width: 100%;
  border-collapse: collapse;
}

.appointments-table th,
.appointments-table td {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: left;
}

/* BUTTONS */
.btn {
  padding: 6px 14px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  font-size: 14px;
}

.btn-primary {
  background-color: #2196f3;
  color: #fff;
}

.btn-danger {
  background-color: #f44336;
  color: #fff;
}

/* EMPTY STATE */
.empty-state {
  text-align: center;
  color: #888;
  padding: 15px;
}
</style>
