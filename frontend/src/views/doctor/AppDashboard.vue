<template>
  <div class="dashboard">

    <!-- HEADER -->
    <header class="dashboard-header">
      <h2>Welcome Dr. {{ doctorName }}</h2>
      <button class="logout-btn" @click="logout">Logout</button>
    </header>

    <!-- UPCOMING APPOINTMENTS -->
    <section class="card">
      <h3>Upcoming Appointments</h3>

      <table class="appointments-table">
        <thead>
          <tr>
            <th>Sr No.</th>
            <th>Patient Name</th>
            <th>Patient History</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(ap, index) in upcomingAppointments" :key="ap.appointment_id">
            <td>{{ index + 1 }}</td>
            <td>{{ ap.patient_email }}</td>
            <td>
              <button class="btn btn-primary" @click="updateHistory(ap.id)">
                Update
              </button>
            </td>
            <td class="action-buttons">
              <button
                class="btn btn-success"
                @click="markComplete(ap.id)"
              >
                Mark as complete
              </button>
              <button
                class="btn btn-danger"
                @click="cancelAppointment(ap.id)"
              >
                Cancel
              </button>
            </td>
          </tr>

          <tr v-if="upcomingAppointments.length === 0">
            <td colspan="4" class="empty-state">
              No upcoming appointments
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- ASSIGNED PATIENTS -->
    <section class="card">
      <h3>Assigned Patients</h3>

      <div
        class="patient-row"
        v-for="patient in assignedPatients"
        :key="patient.id"
      >
        <span>{{ patient.name }}</span>
        <button
          class="btn btn-primary"
          @click="viewPatient(patient.id)"
        >
          View
        </button>
      </div>

      <div v-if="assignedPatients.length === 0" class="empty-state">
        No assigned patients
      </div>
    </section>

    <!-- PROVIDE AVAILABILITY -->
    <div class="availability">
      <button class="btn btn-success" @click="provideAvailability">
        Provide Availability
      </button>
    </div>

  </div>
</template>

<script>
import api from '@/api/axios';

export default {
  name: "AppDashboard",

  data() {
    return {
      doctorName: this.$store.state.auth.email,

      upcomingAppointments: [],

      assignedPatients: [
        { id: 1, name: "Mr. abcde" },
        { id: 2, name: "Miss. Pqrst" }
      ]
    };
  },

  created() {
    this.getupcomingAppointments();
  },

  methods: {
    // HEADER
    logout() {
      // TODO: logout API + redirect
      console.log("Logout clicked");
    },

    // UPCOMING APPOINTMENTS
    async getupcomingAppointments(){
      try {
        const upcomingAppointmentsres = await api.get("/doctor/dashboard")
        this.upcomingAppointments = upcomingAppointmentsres.data
        console.log(upcomingAppointmentsres.data)
      } catch (error) {
        console.log("Failed to fetch upcoming appointments" , error)
      }
    },

    updateHistory(appointmentId) {
      console.log("Update history:", appointmentId);
    },

    markComplete(appointmentId) {
      console.log("Mark complete:", appointmentId);
    },

    cancelAppointment(appointmentId) {
      console.log("Cancel appointment:", appointmentId);
    },

    // ASSIGNED PATIENTS
    viewPatient(patientId) {
      console.log("View patient:", patientId);
    },

    // AVAILABILITY
    provideAvailability() {
      console.log("Provide availability");
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

.card {
  border: 1px solid #ccc;
  padding: 15px;
  margin-bottom: 25px;
  border-radius: 4px;
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

.logout-btn {
  background: none;
  border: none;
  color: #333;
  cursor: pointer;
  font-size: 16px;
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

.action-buttons button {
  margin-right: 8px;
}

/* PATIENT LIST */
.patient-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 4px;
}

/* BUTTONS */
.btn {
  padding: 6px 12px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}

.btn-primary {
  background-color: #2196f3;
  color: #fff;
}

.btn-success {
  background-color: #4caf50;
  color: #fff;
}

.btn-danger {
  background-color: #f44336;
  color: #fff;
}

/* AVAILABILITY */
.availability {
  display: flex;
  justify-content: flex-end;
}

/* EMPTY STATE */
.empty-state {
  text-align: center;
  color: #888;
  padding: 15px;
}
</style>
