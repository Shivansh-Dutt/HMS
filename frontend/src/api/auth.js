import api from "./axios"

export const loginAPI = (payload) => {
    return api.post("/auth/login", payload)
}