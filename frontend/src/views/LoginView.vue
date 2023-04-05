<template>
    <h1>Вход</h1>
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
            ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Войти</b-button>
    </b-form>
</template>

<script>
export default {
    data() {
        return {
            form: {
                email: "",
                password: null
            }
        }
    },
    methods: {
        submit() {
            console.log(this.form);
        }
    }
}
</script>

<style>
</style>