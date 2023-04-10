import {defineStore} from 'pinia'
import {clearToken, getToken, storeToken} from "../../services/localData";
import {getProfile, login as ApiLogin} from "../../services/api";


export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            token: getToken(),
            isLoading: false,
            isSuccess: false,
            error: null,
            user: null
        }
    },
    actions: {
        async login(email, password) {
            this.isLoading = true;
            this.error = null;
            try {
                const token = await ApiLogin(email, password);
                this.token = token;
                storeToken(token);
                this.load()
                this.isSuccess = true;
            } catch (e) {
                this.error = e.message;
            }
            this.isLoading = false;
        },
        async load() {
            this.isLoading = true;
            try {
                this.user = await getProfile();
            } catch (e) {
                this.error = e.message;
            }
            if (!this.user) {
                this.logout();
            }
            this.isLoading = false;
        },
        logout() {
            this.user = null;
            this.token = null;
            clearToken();
        }
    },

});