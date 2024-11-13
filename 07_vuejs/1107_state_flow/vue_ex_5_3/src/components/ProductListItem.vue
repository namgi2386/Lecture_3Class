<template>
  <li>
    {{ product.name }} - {{ product.price }}원
    <button @click="addToCart(product)">장바구니에 추가</button>
  </li>
</template>

<script setup>
const props = defineProps({
  product: Object
})

// addToCart 라는 이름의 이벤트가 있어요 라고 선언
// 이 이벤트 이름은 밑에 있는 함수 이름과 달라도 상관 없다!
const emit = defineEmits(['addToCart'])

// 이 상품이 장바구니에 추가되었다!!! 라고 부모 컴포넌트한테 알려주기 => emit event
const addToCart = function(product) {
  // addToCart 라는 이름의 이벤트 발생 시키기 => 부모컴포넌트한테 알리기
  // 이벤트 발생 시키고 전달할 값이 있다면 두번째 인자로
  emit("addToCart" , product)
}
</script>

<style scoped>

</style>
