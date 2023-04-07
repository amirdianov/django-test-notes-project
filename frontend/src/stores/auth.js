import {ref} from 'vue'
import {defineStore} from 'pinia'
import {storeToken} from "../../services/localData";
import {login as ApiLogin} from "../../services/api";


export const useAuthStore = defineStore('auth', () => {
    const token = ref(null);
    const isLoading = ref(false);
    const isSuccess = ref(false);
    const error = ref(null);

    async function login(email, password) {
        isLoading.value = true;
        try {
            const token = await ApiLogin(email, password);
            storeToken(token);
            isSuccess.value = true;
        } catch (e) {
            error.value = e.message;
        }
        isLoading.value = false;
    }

    return {login, error, isLoading};
})