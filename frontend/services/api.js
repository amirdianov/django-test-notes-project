import {API_URL} from "./consts";
import axios from "axios";
import {useAuthStore} from "@/stores/auth";

const instance = axios.create({
    baseURL: API_URL,
});
instance.interceptors.request.use(function (config) {
    const auth = useAuthStore();
    if (auth.token) {
        config.headers['Authorization'] = `Token ${auth.token}`;
    }
    return config;
}, function (error) {
    return Promise.reject(error);
});

export async function login(email, password) {
    const response = await instance.post('/auth/', {email, password});
    if (response.status === 500) {
        console.error(response);
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data.token;
}

export async function getProfile() {
    const response = await instance.get('/profile/');
    return response.data;
}

export async function getNotes(params) {
    const response = await instance.get("/notes/", {params});
    return response.data;
}

export async function getTags() {
    const response = await instance.get("/tags/");
    return response.data;
}
