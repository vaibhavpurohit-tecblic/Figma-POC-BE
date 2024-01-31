<script setup>
const props = defineProps({
  chat: String,
  deleteModalActive: Boolean,
  deleteChatFunction: Function,
  deleteModalFlagCloseChange: Function,
});
</script>

<template>
  <div class="modal" v-if="props.deleteModalActive">
    <div class="flex flex-col justify-center h-screen">
      <div class="modal-content">
        <div class="px-8 py-5 border-b">
          <h4 class="text-primary text-xl font-semibold">Delete Chat?</h4>
        </div>
        <div class="px-8 py-5">
          <h4 class="text-primary text-lg font-normal">
            This Will Delete
            <span class="font-bold">{{ props.chat }}</span> Forever.
          </h4>
          <div class="flex justify-end gap-4 mt-3">
            <button
              class="bg-quaternary py-2 px-5 text-white rounded-xl"
              @click="() => props.deleteModalFlagCloseChange()"
            >
              Cancel
            </button>
            <button
              class="bg-red-500 py-2 px-5 text-white rounded-xl"
              @click="() => props.deleteChatFunction()"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal {
  /* display: none; */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.2);
  z-index: 60;
}

.modal-content {
  background-color: #fefefe;
  margin: auto;
  width: 400px;
  border-radius: 10px;
}
</style>
