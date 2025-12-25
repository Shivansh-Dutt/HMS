import api from "./axios"

export const patientRegisterAPI = (payload)=>{
    return api.post("/patient/register",payload,{
        headers:{
            "Content-Type":"application/json"
        }
    })
}