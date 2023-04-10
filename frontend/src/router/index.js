import {createRouter, createWebHistory} from 'vue-router'
import {useAuthStore} from "@/stores/auth";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('../views/HomeView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/ProfileView.vue')
        }
    ]
});

router.beforeEach((to, from) => {
    const authStore = useAuthStore();
    const isUnauthorizedAccessAllowed = to.meta?.unauthorizedAccess === true;
    if (!authStore.isAuth && !isUnauthorizedAccessAllowed && from.name !== 'login') {
        return {name: "login"};
    }
})

export default router