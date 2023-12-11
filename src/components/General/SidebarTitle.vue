<script setup>
import { onMounted, ref } from "vue";

const props = defineProps({
  title: String,
  id: String,
});

const active = ref(false);

function CheckIfIdMatch() {
  if ((window?.location?.search?.slice(1) || "") === props.id) {
    active.value = true;
  } else {
    active.value = false;
  }
}

function RedirectToPage() {
  if (!active.value) {
    window.location.href = window.location.pathname + "?" + props.id;
  }
}

onMounted(() => CheckIfIdMatch());
</script>

<template>
  <div
    :class="{
      'flex items-center justify-between gap-4 rounded-xl py-3 px-6 cursor-pointer':
        !active,
      'flex items-center justify-between gap-4 rounded-xl py-3 px-6 bg-secondary':
        active,
    }"
    @click="() => RedirectToPage()"
  >
    <div class="">
      <h6
        :class="{
          'text-primary text-base font-medium': !active,
          'text-white text-base font-medium': active,
        }"
      >
        {{ props.title }}
      </h6>
    </div>
    <div class="flex gap-3 flex-none">
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
