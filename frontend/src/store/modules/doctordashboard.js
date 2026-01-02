import api from "@/services/api";

const state = {
  doctorName: "",
  upcomingAppointments: [],
  assignedPatients: [],
  loading: false
};

const getters = {
  doctorName: state => state.doctorName,
  upcomingAppointments: state => state.upcomingAppointments,
  assignedPatients: state => state.assignedPatients,
  loading: state => state.loading
};

const mutations = {
  SET_LOADING(state, value) {
    state.loading = value;
  },
  SET_DOCTOR_NAME(state, name) {
    state.doctorName = name;
  },
  SET_UPCOMING_APPOINTMENTS(state, appointments) {
    state.upcomingAppointments = appointments;
  },
  SET_ASSIGNED_PATIENTS(state, patients) {
    state.assignedPatients = patients;
  }
};

const actions = {
  async fetchDashboard({ commit }) {
    try {
      commit("SET_LOADING", true);

      const [appointmentsRes, patientsRes, profileRes] =
        await Promise.all([
          api.get("/doctors/dashboard"),
          api.get("/doctors/patients"),
          api.get("/doctor/profile")
        ]);

      commit("SET_UPCOMING_APPOINTMENTS", appointmentsRes.data);
      commit("SET_ASSIGNED_PATIENTS", patientsRes.data);
      commit("SET_DOCTOR_NAME", profileRes.data.name);

    } catch (err) {
      console.error("Dashboard fetch failed", err);
    } finally {
      commit("SET_LOADING", false);
    }
  },

  async markAppointmentComplete({ dispatch }, appointmentId) {
    await api.patch(`/appointments/${appointmentId}/complete`);
    dispatch("fetchDashboard");
  },

  async cancelAppointment({ dispatch }, appointmentId) {
    await api.delete(`/appointments/${appointmentId}`);
    dispatch("fetchDashboard");
  }
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
};
