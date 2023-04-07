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
<script>
import {useAuthStore} from "@/stores/auth";
import {mapActions} from "pinia";

export default {
    name: "App",
    created() {
        this.load();
    },
    methods: mapActions(useAuthStore, ['load'])
}
</script>