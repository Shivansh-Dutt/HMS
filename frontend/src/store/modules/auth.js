import { loginAPI } from "@/api/auth"
import api from "@/api/axios"

const state = {
  role: null,
  email: null,
  loaded: false
}

const mutations = {
  SET_AUTH(state, data) {
    state.role = data.role
    state.email = data.email
  },
  SET_LOADED(state, value) {
    state.loaded = value
  },
  LOGOUT(state) {
    state.role = null
    state.email = null
  }
}

// const state = {
//   token: localStorage.getItem("token"),
//   role: localStorage.getItem("role"),
//   email: localStorage.getItem("email")
// }

// const mutations = {
//   SET_AUTH(state, data) {
//     state.token = data.token
//     state.role = data.role
//     state.email = data.email
//     localStorage.setItem("token", data.token)
//     localStorage.setItem("role", data.role)
//     localStorage.setItem("email", data.email)
//   },
//   LOGOUT(state) {
//     state.token = null
//     state.role = null
//     state.email = null
//     localStorage.clear()
//   }
// }

const actions = {
  async login({ commit }, payload) {
    const res = await loginAPI(payload)
    commit("SET_AUTH", {
      role: res.data.role,
      email: res.data.email
    })
  },
  async fetchUser({ commit }){
    try {
      const res = await api.get("/auth/me")
      commit("SET_AUTH", {
        role: res.data.role,
        email: res.data.email
      })
    } catch (error) {
      commit("LOGOUT")
    } finally{
      commit("SET_LOADED", true)
    }
  },
  logout({ commit }) {
    commit("LOGOUT")
  }
}

export default { namespaced: true, state, mutations, actions }
