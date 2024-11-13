
<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home' }">Home</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'about' }">About</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'user', params: {'username' : 'admin'} }">User</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
