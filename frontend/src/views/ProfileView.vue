<template>
    <p><b>Имя:</b> {{ user.name }}</p>
    <p><b>Email:</b> {{ user.email }}</p>
    <b-btn variant="outline-primary" @click="logoutClickHandler">Выйти</b-btn>
</template>

<script>
import {useAuthStore} from "@/stores/auth";
import {mapActions, mapState} from "pinia";

export default {
    name: "ProfileView",
    computed: mapState(useAuthStore, ['user']),
    methods: {
        ...mapActions(useAuthStore, ['logout']),
        logoutClickHandler() {
            this.logout();
            this.$router.push({name: "home"});
        }
    }
}
</script>