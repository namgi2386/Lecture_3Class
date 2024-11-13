import AboutView from '@/views/AboutView.vue'
import HomeView from '@/views/HomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // 홈페이지 router
      path: "/",
      name: "home",
      component : HomeView
    },
    {
      // About router
      path: "/about",
      name: "about",
      component : AboutView
    }
  ]
})

export default router
