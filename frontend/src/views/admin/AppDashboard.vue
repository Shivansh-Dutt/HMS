<template>
  <div class="container my-4">
    <!-- HEADER -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h4>Welcome Admin</h4>

      <div class="d-flex">
        <input
          type="text"
          class="form-control me-2"
          placeholder="Search doctor, patient, department..."
          v-model="searchTerm"
        />
        <button class="btn btn-primary" @click="searchItems">Search</button>
      </div>
    </div>

    <!-- REGISTERED DOCTORS -->
    <div class="mb-4">
      <div class="d-flex justify-content-between align-items-center mb-2">
        <h5>Registered Doctors</h5>
        <button class="btn btn-success btn-sm" @click="$router.push('/admin/doctors/create')">Create</button>
      </div>

      <div v-if="doctors.length === 0" class="alert alert-warning">No doctors registered.</div>
      <div
        class="border rounded p-2 mb-2 d-flex justify-content-between align-items-center"
        v-for="doctor in filteredDoctors"
        :key="doctor.id"
      >
        <span>{{ doctor.email }}</span>
        <div>
          <button class="btn btn-warning btn-sm me-2" @click="editDoctor(doctor)">Edit</button>
          <button class="btn btn-danger btn-sm me-2" @click="deleteDoctor(doctor.id)">Delete</button>
          <button class="btn btn-secondary btn-sm" @click="blacklistDoctor(doctor.id)">Blacklist</button>
        </div>
      </div>
    </div>

    <!-- REGISTERED PATIENTS -->
    <div class="mb-4">
      <h5 class="mb-2">Registered Patients</h5>

      <div v-if="patients.length === 0" class="alert alert-warning">No patients registered.</div>
      <div
        class="border rounded p-2 mb-2 d-flex justify-content-between align-items-center"
        v-for="patient in filteredPatients"
        :key="patient.id"
      >
        <span>{{ patient.email }}</span>
        <div>
          <button class="btn btn-warning btn-sm me-2" @click="editPatient(patient)">Edit</button>
          <button class="btn btn-danger btn-sm me-2" @click="deletePatient(patient.id)">Delete</button>
          <button class="btn btn-secondary btn-sm" @click="blacklistPatient(patient.id)">Blacklist</button>
        </div>
      </div>
    </div>

    <!-- UPCOMING APPOINTMENTS -->
    <div>
      <h5 class="mb-2">Upcoming Appointments</h5>

      <div v-if="appointments.length === 0" class="alert alert-warning">No upcoming appointments.</div>
      <table class="table table-bordered">
        <thead class="table-light">
          <tr>
            <th>Sr No.</th>
            <th>Patient Name</th>
            <th>Doctor Name</th>
            <th>Department</th>
            <th>Patient History</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(appt, index) in filteredAppointments" :key="appt.id">
            <td>{{ index + 1 }}</td>
            <td>{{ appt.patient }}</td>
            <td>{{ appt.doctor }}</td>
            <td>{{ appt.department }}</td>
            <td>
              <button class="btn btn-outline-primary btn-sm">
                View
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { getDashboard } from '@/api/admin';

export default {
  name: "AdminDashboard",

  data() {
    return {
      doctors: [],
      patients: [],
      appointments: [],
      searchTerm: "",
    };
  },

  computed: {
    filteredDoctors() {
      return this.doctors.filter(doctor => {
        return (
          doctor.email.toLowerCase().includes(this.searchTerm.toLowerCase())
        );
      });
    },

    filteredPatients() {
      return this.patients.filter(patient => {
        return (
          patient.email.toLowerCase().includes(this.searchTerm.toLowerCase())
        );
      });
    },

    filteredAppointments() {
      return this.appointments.filter(appt => {
        return (
          appt.patient.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
          appt.doctor.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
          appt.department.toLowerCase().includes(this.searchTerm.toLowerCase())
        );
      });
    },
  },

  created() {
    this.fetchDashboardData();
  },

  methods: {
    async fetchDashboardData() {
      try {
        const DashboardRes = await getDashboard();
        console.log(DashboardRes.data);
        this.doctors = DashboardRes.data.total_doctors;
        this.patients = DashboardRes.data.total_patients;
        this.appointments = DashboardRes.data.upcoming_appointments;
      } catch (error) {
        console.error("Failed to fetch dashboard data:", error);
      }
    },

    searchItems() {
      // Optionally, trigger more specific search actions here
      console.log("Search term:", this.searchTerm);
    },

    editDoctor(doctor) {
      // Logic for editing the doctor's details (possibly navigate to a form page)
      console.log("Edit doctor:", doctor);
    },

    deleteDoctor(doctorId) {
      // Logic for deleting a doctor
      console.log("Delete doctor:", doctorId);
    },

    blacklistDoctor(doctorId) {
      // Logic for blacklisting a doctor
      console.log("Blacklist doctor:", doctorId);
    },

    editPatient(patient) {
      // Logic for editing the patient's details (possibly navigate to a form page)
      console.log("Edit patient:", patient);
    },

    deletePatient(patientId) {
      // Logic for deleting a patient
      console.log("Delete patient:", patientId);
    },

    blacklistPatient(patientId) {
      // Logic for blacklisting a patient
      console.log("Blacklist patient:", patientId);
    },
  },
};
</script>
