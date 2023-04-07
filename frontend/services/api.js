import {API_URL} from "./consts";
import axios from "axios";

const instance = axios.create({
    baseURL: API_URL,
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

export async function getProfile(token) {
    const response = await instance.get(`${API_URL}/profile/`, {
        headers: {
            "Authorization": `Token ${token}`
        },
    })
    return response.data;
}