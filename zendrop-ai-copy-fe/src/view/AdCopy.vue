<script setup>
import Header from "../components/General/Header.vue";
import Sidebar from "../components/General/Sidebar.vue";
</script>

<template>
  <div class="flex flex-col gap-3 min-h-screen overflow-hidden">
    <Header :auth="true" active="ad-copy" />
    <div class="flex-1 flex gap-7 container p-5 mx-auto">
      <Sidebar title="Create New Ad Copy" />
    </div>
  </div>
</template>

<style scoped></style>
