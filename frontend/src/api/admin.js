import api from "./axios"

export const getDashboard = () => {
    return api.get("admin/dashboard",{
        headers:{
            "Content-Type":"application/json"
        }
    });
}

export const createDoctor = (payload) => {
  // ✅ Return the Promise so 'await' works
  return api.post("/admin/doctor", payload, {
    headers: {
      "Content-Type": "application/json"
    }
  });
};
