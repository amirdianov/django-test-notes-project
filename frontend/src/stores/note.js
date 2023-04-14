import {defineStore} from 'pinia'
import {getNotes} from "../../services/api";


export const useNotesStore = defineStore('notes', {
    state: () => {
        return {
            isLoading: false,
            error: null,
            results: [],
            count: null,
            params: {
                search: null,
                tag_id: null
            }
        }
    },
    actions: {
        async load() {
            this.isLoading = true;
            this.error = null;
            try {
                const params = {
                    ...this.params,
                    title: this.params.search
                }
                const responseData = await getNotes(params);
                this.results = responseData.results;
                this.count = responseData.count;
            } catch (e) {
                this.error = e.message;
            }
            this.isLoading = false;
        },
        setParameter(key, value) {
            this.params[key] = value;
        }
    },
});