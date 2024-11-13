import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"

export const useProductStore = defineStore('product', () => {
  // 중앙 저장소에서 관리하는 상태(상품 정보들) state
  // const products = ref([
  //   { id: 1, title: 'Product 1', body: 'quia et suscipit suscipit recusandae' },
  //   { id: 2, title: 'Product 2', body: 'quo iure voluptatem occaecati omnis' },
  //   { id: 3, title: 'Product 3', body: 'repudiandae veniam quaerat sunt' }
  // ])
  
  const products = ref([])

  // 상품정보를 요청하는 기능
  const getProductData = function() {
    axios({
      method: "get",
      url: "https://jsonplaceholder.typicode.com/posts"
    })
    .then((response) => {
      products.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  // 상품의 개수를 계산해서 return 하는 getters
  const productCount = computed(() => {
    return products.value.length
  })
  
  // 중앙 저장소의 데이터(상품 정보)를 삭제하는 기능 actions
  const deleteProduct = function (id) {
    // Array Helper 메서드를 통해 배열 수정/삭제

    // 삭제할 상품 정보의 index 검색
    const idx = products.value.findIndex((product) => { return product.id === id })

    if (idx !== -1) {
      products.value.splice(idx, 1)
    }

  }

  return { products, deleteProduct, productCount, getProductData }
})
