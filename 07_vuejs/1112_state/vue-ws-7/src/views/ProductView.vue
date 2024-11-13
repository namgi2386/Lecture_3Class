<template>
  <div>
    <h1 class="mt-5">상품 목록 페이지</h1>
    <div class="row g-4 row-cols-3">
      <ProductDetail v-for="product in store.products" :key="product.name" :product="product"/>
    </div>
  </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue';
import { useProductStore } from '@/stores/product';

const store = useProductStore()
</script>

<style scoped>

</style>