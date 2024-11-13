<template>
  <ul>
    <ProductListItem 
      v-for="product in products" 
      :key="product.id" 
      :product="product"
      @add-to-cart="addToCart"
    />
    <!-- addToCart 라는 이름의 이벤트가 자식 컴포넌트에서 발생 했을때 처리할 함수 작성 -->
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'

defineProps({
  products: Array
})
const emit = defineEmits(['addToCart'])

// 이 상품이 장바구니에 추가되었다!!! 라고 부모 컴포넌트한테 알려주기 => emit event
const addToCart = function(product) {
  // addToCart 라는 이름의 이벤트 발생 시키기 => 부모컴포넌트한테 알리기
  // 이벤트 발생 시키고 전달할 값이 있다면 두번째 인자로
  emit("addToCart" , product)
}
</script>
