<template>
    <b-card>
        <b-input placeholder="Поиск"/>
        <TagsFilterContainer class="mt-3"/>
        <b-button block type="submit" variant="outline-primary" class="mt-3">
            Найти
        </b-button>
    </b-card>
</template>

<script>
import TagsFilterContainer from "@/containers/notes/TagsFilterContainer.vue";

export default {
    name: "NoteFiltersContainer",
    components: {TagsFilterContainer}
}
</script>

<style scoped>

</style>