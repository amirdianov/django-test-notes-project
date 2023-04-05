
<script setup>
import {RouterLink, RouterView} from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <b-container>
    <b-jumbotron
        header="Bootstrap-Vue"
        lead="Bootstrap v4 Components for Vue.js 2"
    >
      <p>Now running on @vue/compat and Vue.js 3</p>
      <b-button variant="primary" @click="showModal"> Click me!</b-button>
    </b-jumbotron>
  </b-container>

  <RouterView/>
</template>