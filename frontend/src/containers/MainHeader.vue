<template>
    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-container>
            <b-navbar-brand to="/">Notes</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item :to="{name: 'home'}">Home</b-nav-item>
                    <b-nav-item v-if="!user" :to="{name: 'login'}">Вход</b-nav-item>
                </b-navbar-nav>
            </b-collapse>

            <b-navbar-nav class="ml-auto">
                <b-nav-item v-if="user" :to="{name: 'profile'}">{{user.email}}</b-nav-item>
            </b-navbar-nav>
        </b-container>
    </b-navbar>
</template>

<script>
import {useAuthStore} from "@/stores/auth";
import {mapState} from "pinia";

export default {
    name: "MainHeader",
    computed: mapState(useAuthStore, ['user'])
}
</script>

<style scoped>

</style>