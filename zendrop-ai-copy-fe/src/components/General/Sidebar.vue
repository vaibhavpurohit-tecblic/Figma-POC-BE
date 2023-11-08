<script setup>
import SidebarTitle from "./SidebarTitle.vue";

defineProps({
  title: String,
});
</script>

<template>
  <div class="sidebar-container py-5 px-6">
    <div class="flex flex-col gap-4">
      <div class="flex gap-4">
        <div
          class="rounded-xl border-2 border-secondary py-2 px-6 flex items-center gap-3"
        >
          <img src="../../assets/logos/addIcon.svg" alt="" class="h-4 w-4" />
          <p class="text-base text-primary font-medium">{{ title }}</p>
        </div>
        <div class="p-3 rounded-xl border-2 border-secondary">
          <img
            src="../../assets/logos/sidebarIcon.svg"
            alt="Sidebar Logo"
            class="w-6 h-6"
          />
        </div>
      </div>
      <div class="flex flex-col">
        <div class="flex flex-col gap-3">
          <SidebarTitle :active="true" title="Lorem Ipsum is simple" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sidebar-container {
  border-radius: 21.836px;
  background: #fff;
  box-shadow: 0px 0px 8.73458px 0px rgba(110, 94, 202, 0.15);
}
</style>
