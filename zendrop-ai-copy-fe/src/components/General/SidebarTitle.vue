<script setup>
defineProps({
  active: Boolean,
  title: String,
});
</script>

<template>
  <div
    :class="{
      'flex items-center justify-between gap-4 rounded-xl py-3 px-6 cursor-pointer':
        !active,
      'flex items-center justify-between gap-4 rounded-xl py-3 px-6 bg-secondary':
        active,
    }"
  >
    <div class="">
      <h6
        :class="{
          'text-primary text-base font-medium': !active,
          'text-white text-base font-medium': active,
        }"
      >
        {{ title }}
      </h6>
    </div>
    <div class="flex gap-3">
      <img
        src="../../assets/logos/editActive.svg"
        alt="Edit Icon"
        class="w-4 h-4 cursor-pointer"
        v-if="active"
      />
      <img
        src="../../assets/logos/editInActive.svg"
        alt="Edit Icon"
        class="w-4 h-4"
        v-else
      />
      <img
        src="../../assets/logos/deleteActive.svg"
        alt="Delete Icon"
        class="w-4 h-4 cursor-pointer"
        v-if="active"
      />
      <img
        src="../../assets/logos/deleteInActive.svg"
        alt="Delete Icon"
        class="w-4 h-4"
        v-else
      />
    </div>
  </div>
</template>

<style scoped></style>
