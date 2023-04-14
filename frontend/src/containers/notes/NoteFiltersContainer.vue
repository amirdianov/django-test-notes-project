<template>
    <b-card>
        <b-input v-model="search" placeholder="Поиск"/>
        <TagsFilterContainer class="mt-3"/>
        <b-button block type="submit" variant="outline-primary" class="mt-3">
            Найти
        </b-button>
    </b-card>
</template>

<script>
import TagsFilterContainer from "@/containers/notes/TagsFilterContainer.vue";
import {mapActions, mapState} from "pinia";
import {useNotesStore} from "@/stores/note";

export default {
    name: "NoteFiltersContainer",
    components: {TagsFilterContainer},
    methods: mapActions(useNotesStore, ['setParameter']),
    computed: {
        ...mapState(useNotesStore, ['params']),
        search: {
            get() {
                return this.params.search;
            },
            set(value) {
                this.setParameter('search', value);
            }
        }

    }
}
</script>

<style scoped>

</style>