<template>
  <div>
    <h3>{{ username }}이 작성한 게시글</h3>
    <ol>
      <PostListItem v-for="post in posts" :key="post.id" :post="post"/>
    </ol>
    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRoute, RouterView } from "vue-router";
import PostListItem from "./PostListItem.vue";

// 게시글 정보
const posts = ref([
  {id : 1, title: "Post 1", content: "Content 1"},
  {id : 2, title: "Post 2", content: "Content 2"},
  {id : 3, title: "Post 3", content: "Content 3"}
])

const route = useRoute()
const username = ref(route.params.username)

</script>

<style scoped></style>