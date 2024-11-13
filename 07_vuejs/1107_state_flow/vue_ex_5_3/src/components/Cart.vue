<template>
  <div v-if="cart.length > 0">
    <h2>장바구니</h2>
    <ul>
      <li v-for="product in cart" :key="product.id">
        {{ product.name }} - {{ product.price }}원
        <button @click="removeItem(product)" >삭제</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
const props = defineProps({
  cart: Array
})

const emit = defineEmits(["removeItem"])

// product 가 장바구니에서 제거되었어요!! 라고 부모한테 알림 => 이벤트 발생
const removeItem = function(product) {
  // 장바구니에서 제거 되어야 할 상품 정보도 같이 전달
  emit("removeItem", product)
}
</script>

<style scoped>

</style>