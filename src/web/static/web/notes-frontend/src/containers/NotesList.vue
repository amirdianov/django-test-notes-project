<template>
  <p v-if="isLoading" class="alert alert-info">Загрузка заметок...</p>
  <p v-if="error" class="alert alert-danger">{{ error }}</p>
  <ul>
    <li v-for="note in notes" :key="note.id">
      <b><a :href="`/notes/rere/${note.id}`">{{note.title}}</a></b>
    </li>
  </ul>
</template>

<script>
export default {
  name: "NotesList",
  data() {
    return {
      isLoading: true,
      notes: [],
      error: null
    }
  },
  methods: {
    async load() {
      this.isLoading = true;
      try {
        const response = await fetch("/api/notes/")
        const data = await response.json();
        this.notes = data.results;
      }
      catch (e) {
        this.error = "Произошла ошибка при запросе данных, попробуйте еще раз"
      }
      this.isLoading = false;
    }
  },
  created() {
    this.load();
  }
}
</script>

<style scoped>

</style>