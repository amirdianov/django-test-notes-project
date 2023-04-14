<template>
    <b-overlay :show="isLoading">
        <b-form-select :options="options" :value="null" />
    </b-overlay>
</template>

<script>


import {getTags} from "../../../services/api";

export default {
    name: "TagsFilterContainer",
    data() {
        return {
            results: [],
            isLoading: true
        };
    },
    methods: {
        async load() {
            this.isLoading = true;
            this.results = await getTags();
            this.isLoading = false;
        }
    },
    created() {
        this.load();
    },
    computed: {
        options() {
            return [
                {value: null, text: "Выберите тег"},
                ...this.results.map(x => ({value: x.id, text: x.title}))
            ]
        }
    }
}
</script>