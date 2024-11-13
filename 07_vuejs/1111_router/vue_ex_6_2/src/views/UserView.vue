<template>
  <div>
    <h2>User Profile</h2>
    <p>Username : {{ username }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRoute } from "vue-router"

const route = useRoute()
const username = ref(route.params.username)

</script>

<style scoped></style>