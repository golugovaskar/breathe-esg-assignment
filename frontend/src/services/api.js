import axios from "axios";

const api = axios.create({
baseURL: "https://breathe-esg-backend-7usx.onrender.com/api"});

export default api;