<template>
    <h1>Notes</h1>
</template>

<script>
import {mapActions} from "pinia";
import {useNotesStore} from "@/stores/note";

export default {
    name: "NotesContainer",
    methods: mapActions(useNotesStore, ['load']),
    created() {
        this.load();
    }
}
</script>

<style scoped>

</style>