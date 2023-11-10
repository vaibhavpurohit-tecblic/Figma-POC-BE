<script setup>
defineProps({
  active: Boolean,
});
</script>

<template>
  <p class="text-gray-400 font-normal text-sm">Select Product</p>
  <div
    :class="{
      'border border-secondary py-3 px-6 rounded-xl flex gap-4 justify-between items-center mt-1 cursor-pointer':
        active,
      'border border-gray-500 py-3 px-6 rounded-xl flex gap-4 justify-between items-center mt-1 cursor-pointer':
        !active,
    }"
  >
    <p class="flex-1 text-primary font-normal text-sm">Select your Product</p>
    <img
      src="../../assets/logos/downArrow.svg"
      alt="Profile Pic"
      class="rounded-full h-[15px] w-[15px]"
    />
  </div>
  <button
    :class="{
      'bg-quaternary py-3 w-full mt-7 text-white rounded-xl': active,
      ' bg-gray-500 py-3 w-full mt-7 text-white rounded-xl': !active,
    }"
  >
    Create Now
  </button>
</template>

<style scoped></style>
