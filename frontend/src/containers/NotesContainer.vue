<template>
    <h1>Notes</h1>
    <b-spinner v-if="isLoading"/>
    <b-alert v-if="error" variant="danger" show>{{ error }}</b-alert>

    <b-list-group>
        <b-list-group-item v-for="note in results" :key="note.id">
            <b>{{ note.title }}</b>
            {{ note.text }}
        </b-list-group-item>
    </b-list-group>
</template>

<script>
import {mapActions, mapState} from "pinia";
import {useNotesStore} from "@/stores/note";

export default {
    name: "NotesContainer",
    methods: mapActions(useNotesStore, ['load']),
    computed: mapState(useNotesStore, ['results', 'count', 'isLoading', 'error']),

    created() {
        this.load();
    }
}
</script>

<style scoped>

</style>