<template>
  <button>
    <slot/>
  </button>
</template>

<script>
export default {
  name: "MyButton",
}
</script>

<style scoped>
button {
  padding: 5px 10px;
  border-radius: 5px;
}

</style>
