<script setup>
defineProps({
  active: Boolean,
  title: String,
});
</script>

<template>
  <div class="flex items-center justify-between gap-4 rounded-xl py-2 px-6">
    <div class="">
      <h6 class="">{{ title }}</h6>
    </div>
    <div class="flex gap-3">
      <img src="../../assets/logos/editInActive.svg" alt="" class="" />
      <img src="../../assets/logos/deleteInActive.svg" alt="" class="" />
    </div>
  </div>
</template>

<style scoped></style>
