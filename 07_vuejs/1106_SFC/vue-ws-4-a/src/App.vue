<template>
  <HeaderComponent />

  <main class="container p-3">
    <GalleryList />
  </main>
</template>

<script setup>
import GalleryList from './components/GalleryList.vue';
import HeaderComponent from './components/HeaderComponent.vue';
</script>

<style scoped>
  .my {
    border: 1px solid red;
  }
</style>