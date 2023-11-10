<script setup></script>

<template>
  <div
    class="border border-secondary rounded-xl flex gap-2 bg-secondary/[0.10] py-3 px-6"
  >
    <div class="">
      <img
        src="../../assets/logos/textAreaChat.svg"
        alt="Chat icon"
        class="h-4 w-4"
      />
    </div>
    <div class="flex-1">
      <textarea
        rows="3"
        class="bg-transparent w-full focus-visible:outline-none text-primary text-base font-normal"
      />
    </div>
    <div class="self-end">
      <img
        src="../../assets/logos/textAreaEnter.svg"
        alt="Enter icon"
        class="h-4 w-4"
      />
    </div>
  </div>
</template>

<style scoped></style>
