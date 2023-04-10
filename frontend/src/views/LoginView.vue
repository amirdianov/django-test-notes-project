<template>
    <h1>Вход</h1>
    <b-alert v-if="error" variant="danger" show>{{ error }}</b-alert>
    <b-form @submit.prevent="submit">
        <b-form-group
                id="input-group-1"
                label="Электронная почта:"
                label-for="input-1"
        >
            <b-form-input
                    id="input-1"
                    v-model="form.email"
                    type="email"
                    placeholder="Введите email"
                    required
            ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Пароль:" label-for="input-2">
            <b-form-input
                    id="input-2"
                    v-model="form.password"
                    placeholder="Введите пароль"
                    required
                    type="password"

            ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Войти</b-button>
    </b-form>
</template>

<script>


import {mapActions, mapState} from "pinia";
import {useAuthStore} from "@/stores/auth";

export default {
    data() {
        return {
            form: {
                email: "",
                password: null
            },
        }
    },
    methods: {
        ...mapActions(useAuthStore, ['login']),
        async submit() {
            await this.login(this.form.email, this.form.password);
            this.$router.push({name: "profile"});

        }
    },
    computed: {
        ...mapState(useAuthStore, ['error', 'isLoading']),
    }
}

</script>

<style>
</style>