<template>
  <div>
    <p>번호 : {{ post.id }}</p>
    <p>제목 : {{ post.title }}</p>
    <p>내용 : {{ post.content }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRoute, onBeforeRouteUpdate } from "vue-router";

// 게시글 목록
const posts = ref([
  { id: 1, title: "Post 1", content: "Content 1" },
  { id: 2, title: "Post 2", content: "Content 2" },
  { id: 3, title: "Post 3", content: "Content 3" }
])

const route = useRoute()
// params에서 id는 알고 있다. 위에 있는것중에 id 일치하는거 하나 찾아서 보여주기
const id = ref(route.params.id)

const post = ref(posts.value.find((post) => { return post.id === Number(id.value) }))

// Vue는 컴포넌트를 재사용 하기 때문에 setup script을 다시 실행하지 않는다.
// 컴포넌트 내부 변수가 그대로 남아 있습니다.
// 컴포넌트 네비게이션 가드를 통해서 수동으로 변수의 값을 업데이트
onBeforeRouteUpdate((to) => {
  id.value = to.params.id
  post.value = posts.value.find((post) => { return post.id === Number(id.value) })
})

</script>

<style scoped></style>