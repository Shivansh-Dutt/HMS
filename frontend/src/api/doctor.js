import api from "./axios"

export const getDashboard = () => {
    return api.get("doctor/dashboard",{
        headers:{
            "Content-Type":"application/json"
        }
    });
}