<script setup>
import MyButton from "@/components/MyButton.vue";
</script>
<template>
  <MyButton>{{count}}</MyButton>
</template>
<script>
  export default {
    data(){
      return {
        count: window.COUNT
      }
    }
  }
</script>