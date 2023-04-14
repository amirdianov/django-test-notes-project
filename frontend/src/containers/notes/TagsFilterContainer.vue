<template>
    <b-overlay :show="isLoading">
        <b-form-select
                :options="options"
                :value="modelValue"
                @change="setValue"
        />
    </b-overlay>
</template>

<script>


import {getTags} from "../../../services/api";

export default {
    name: "TagsFilterContainer",
    emits: ['update:modelValue'],
    props: {
        modelValue: String
    },
    data() {
        return {
            results: [],
            isLoading: true
        };
    },
    methods: {
        setValue(value) {
            this.$emit("update:modelValue", value);
        },
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