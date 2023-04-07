<script setup>
import {RouterView} from 'vue-router'
import MainHeader from "@/containers/MainHeader.vue";
</script>

<template>
    <MainHeader/>
    <b-container>
        <RouterView/>
    </b-container>
</template>