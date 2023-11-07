<script setup>
defineProps({
  auth: Boolean,
  active: String,
});
</script>

<template>
  <div
    class="container my-6 px-5 mx-auto flex justify-between gap-5 items-center"
  >
    <div class="">
      <img
        src="../../assets/logos/logo.svg"
        alt="ZenDrop Logo"
        class="h-[30px] w-[200px]"
      />
    </div>
    <div class="flex justify-end items-center gap-5">
      <div
        class="box-shadow-header-container px-3 py-2 flex gap-2 items-center"
        v-if="auth"
      >
        <div
          :class="{
            'py-2 px-10 border-2 cursor-pointer border-transparent hover:border-secondary rounded-[100px]':
              active !== 'ad-copy',
            'py-2 px-10 border-2 cursor-pointer border-secondary rounded-[100px]':
              active === 'ad-copy',
          }"
        >
          <h5 class="text-primary font-normal text-base">Ad Copy</h5>
        </div>
        <div
          :class="{
            'py-2 px-10 border-2 cursor-pointer border-transparent hover:border-secondary rounded-[100px]':
              active !== 'video-creator',
            'py-2 px-10 border-2 cursor-pointer border-secondary rounded-[100px]':
              active === 'video-creator',
          }"
        >
          <h5 class="text-primary font-normal text-base">Video Creator</h5>
        </div>
        <div
          :class="{
            'py-2 px-10 border-2 cursor-pointer border-transparent hover:border-secondary rounded-[100px]':
              active !== 'expert-bot',
            'py-2 px-10 border-2 cursor-pointer border-secondary rounded-[100px]':
              active === 'expert-bot',
          }"
        >
          <h5 class="text-primary font-normal text-base">Expert Bot</h5>
        </div>
      </div>
      <div
        class="box-shadow-header-container p-1 flex pl-9 gap-3 items-center cursor-pointer"
      >
        <p class="text-primary font-normal text-base">John Smith</p>
        <img
          src="../../assets/logos/downArrow.svg"
          alt="Profile Pic"
          class="rounded-full h-[15px] w-[15px]"
        />
        <img
          src="../../assets/images/ProfilePhoto.png"
          alt="Profile Pic"
          class="rounded-full h-[45px] w-[45px]"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.box-shadow-header-container {
  border-radius: 100px;
  background: #fff;
  box-shadow: 0px 4px 35px 0px rgba(133, 115, 238, 0.2);
}
</style>
