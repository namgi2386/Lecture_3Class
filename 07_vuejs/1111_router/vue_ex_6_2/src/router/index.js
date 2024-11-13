import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import UserView from '@/views/UserView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: "/user/:username",
      name: "user",
      component: UserView,
      beforeEnter: (to) => {
        // 유저이름을 검사
        const requestUsername = to.params.username
        if (requestUsername !== "admin"){
          window.alert("admin이 아니면 접근 불가")
          return { name: 'home' }
        }
      }
    }
  ]
})

export default router
