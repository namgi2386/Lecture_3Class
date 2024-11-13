<template>
  <div>
    <div class="card h-100">
      <div class="card-header d-flex justify-content-center">
        <h3 class="card-title mt-1">{{ product.name }}</h3>
      </div>
      <img :src="product.imagePath" alt="">
      <div class="card-body align-items-center d-flex flex-column">
        <p>￦{{ product.price }}</p>
        <i @click="store.toggleFavorite(product.name)" class="bi" :class="[product.isFavorite ? 'bi-heart-fill text-danger' : 'bi-heart']"></i>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';

defineProps({
  product: Object
})

const store = useProductStore()
</script>

<style scoped></style>