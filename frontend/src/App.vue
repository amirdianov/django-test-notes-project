<script setup>
import {RouterView} from 'vue-router'
</script>

<template>
    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-container>
            <b-navbar-brand to="/">Notes</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item :to="{name: 'home'}">Home</b-nav-item>
                    <b-nav-item :to="{name: 'login'}">Вход</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-container>
    </b-navbar>
    <b-container>
        <RouterView/>
    </b-container>
</template>