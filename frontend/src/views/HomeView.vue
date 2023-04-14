<script setup>
import NotesContainer from "@/containers/notes/NotesContainer.vue";
import NoteFiltersContainer from "@/containers/notes/NoteFiltersContainer.vue";
</script>

<template>
    <main>
        <h1>Заметки</h1>
        <b-row>
            <b-col md="3">
                <NoteFiltersContainer/>
            </b-col>
            <b-col md="9">
                <NotesContainer/>
            </b-col>
        </b-row>
    </main>
</template>
