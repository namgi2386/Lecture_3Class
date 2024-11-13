<template>
  <div class="row row-cols-3 g-3">
    <!-- 카드 * 4 -->
    <GalleryListItem v-for="i in numberOfItems" />
  </div>
</template>

<script setup>
import GalleryListItem from './GalleryListItem.vue';

const numberOfItems = 4
</script>

<style scoped></style>