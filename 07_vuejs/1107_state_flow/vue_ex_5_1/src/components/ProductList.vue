<template>
  <ul>
    <li v-for="product in products" :key="product.id">
      {{ product.name }} - {{  product.price }}원
    </li>
  </ul>
</template>

<script setup>
const props = defineProps({
  products: Array
})

console.log(props.products)
</script>

<style scoped>

</style>