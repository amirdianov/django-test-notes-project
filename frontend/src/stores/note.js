import {defineStore} from 'pinia'
import {getNotes} from "../../services/api";


export const useNotesStore = defineStore('notes', {
    state: () => {
        return {
            isLoading: false,
            error: null,
            results: [],
            count: null
        }
    },
    actions: {
        async load() {
            this.isLoading = true;
            this.error = null;
            try {
                const responseData = await getNotes();
                this.results = responseData.results;
                this.count = responseData.count;
            } catch (e) {
                this.error = e.message;
            }
            this.isLoading = false;
        },
    },
});