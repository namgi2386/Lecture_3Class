<template>
  <div>
    <div class="sticky-top bg-dark d-flex justify-content-center align-items-center">
      <RouterLink class="fw-bold text-white text-decoration-none m-3" v-for="link in links" :key="link.name" :to="{ name: link.name }">{{ link.name.toUpperCase() }}</RouterLink>
    </div>
    <div class="container">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { ref } from "vue"

const links = ref([
  { name: "home" },
  { name: "products" },
  { name: "favorite" },
])

</script>

<style scoped></style>