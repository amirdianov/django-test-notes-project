import {defineStore} from 'pinia'
import {storeToken} from "../../services/localData";
import {login as ApiLogin} from "../../services/api";


export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            token: null,
            isLoading: false,
            isSuccess: false,
            error: null
        }
    },
    actions: {
        async login(email, password) {
            this.isLoading = true;
            this.error = null;
            try {
                const token = await ApiLogin(email, password);
                storeToken(token);
                this.isSuccess = true;
            } catch (e) {
                this.error = e.message;
            }
            this.isLoading = false;
        }
    },
});