import { loginAPI } from "@/api/auth"

const state = {
  token: localStorage.getItem("token"),
  role: localStorage.getItem("role"),
}

const mutations = {
  SET_AUTH(state, data) {
    state.token = data.token
    state.role = data.role
    state.email = data.email
    localStorage.setItem("token", data.token)
    localStorage.setItem("role", data.role)
  },
  LOGOUT(state) {
    state.token = null
    state.role = null
    state.email = null
    localStorage.clear()
  }
}

const actions = {
  async login({ commit }, payload) {
    const res = await loginAPI(payload)
    commit("SET_AUTH", {
      token: res.data.access_token,
      role: res.data.role
    })
  },
  logout({ commit }) {
    commit("LOGOUT")
  }
}

export default { namespaced: true, state, mutations, actions }
