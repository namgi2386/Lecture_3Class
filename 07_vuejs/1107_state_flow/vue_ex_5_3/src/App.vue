<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList :products="products" @add-to-cart="addToCart" />
    <p>총 가격 : {{ totalPrice }}</p>
    <!-- :내려줄이름="내려줄값(자바스크립트코드)" -->
    <!-- 내려줄이름="내려줄값(문자열)"  -->
    <Cart :cart="cart" @remove-item="removeItem"/>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from './components/Cart.vue';

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const cart = ref([])

const totalPrice = computed(() => {
  let total = 0
  cart.value.forEach((product) => {
    total += product.price
  })
  return total

  // cart.value.reduce((누적값, 배열원소) => { } , 초기값)
  // return cart.value.reduce((total, product) => { return total + product.price }, 0)
})

const addToCart = function(product) {
  cart.value.push(product)
}

const removeItem = function(product) {
  // 삭제할 상품의 인덱스 찾아서
  const idx = cart.value.findIndex((item) => item.id === product.id)
  // 배열에서 잘라내기(idx 위치에서 1개 삭제)
  cart.value.splice(idx, 1)
}
</script>
