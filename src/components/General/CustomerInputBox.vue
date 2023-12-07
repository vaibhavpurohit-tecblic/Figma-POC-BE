<script setup>
import { ref } from "vue";
import { AdCopyChatMessagesAddApiFunction } from "../../api/AdCopyApis/index.js";
import { ExpertBotChatMessagesAddApiFunction } from "../../api/ExpertBotApis/index.js";

const props = defineProps({
  active: Boolean,
  loading: Boolean,
  loadingStartFunction: Function,
  loadingStopFunction: Function,
});

const textMessage = ref("");

function textMessageChange(e) {
  textMessage.value = e.target.value;
}

function clearTextareaOnEnter(e) {
  if (e.key === "Enter") {
    SideBarDataFunction();
  }
}

async function AdCopyChatMessagesAddFunction() {
  const result = await AdCopyChatMessagesAddApiFunction({
    id: window?.location?.search?.slice(1) || "",
    messageContent: textMessage.value,
  });

  if (result.status === 200) {
    props.loadingStopFunction();
    textMessage.value = "";
  }
}

async function ExpertBotChatMessagesAddFunction() {
  const result = await ExpertBotChatMessagesAddApiFunction({
    id: window?.location?.search?.slice(1) || "",
    messageContent: textMessage.value,
  });

  if (result.status === 200) {
    props.loadingStopFunction();
    textMessage.value = "";
  }
}

function SideBarDataFunction() {
  if (textMessage.value.length > 0 && props.active && !props.loading) {
    props.loadingStartFunction();
    if (window.location.pathname === "/ad-copy") {
      AdCopyChatMessagesAddFunction();
    } else if (window.location.pathname === "/expert-bot") {
      ExpertBotChatMessagesAddFunction();
    }
  }
}
</script>

<template>
  <div
    :class="{
      'border border-secondary rounded-xl flex gap-2 bg-secondary/[0.10] py-3 px-6':
        props.active && !props.loading,
      'border border-secondary rounded-xl flex gap-2 bg-secondary/[0.10] py-3 px-6 opacity-60':
        !props.active || props.loading,
    }"
  >
    <div class="pt-1">
      <img
        src="../../assets/logos/textAreaChat.svg"
        alt="Chat icon"
        class="h-4 w-4"
      />
    </div>
    <div class="flex-1">
      <textarea
        rows="3"
        class="bg-transparent w-full focus-visible:outline-none text-primary text-base font-normal resize-none"
        placeholder="Type here to chat ..."
        :disabled="!props.active || props.loading"
        :value="textMessage"
        @input="textMessageChange"
        @keydown.enter.prevent="clearTextareaOnEnter"
      />
    </div>
    <div class="self-end">
      <img
        src="../../assets/logos/textAreaEnter.svg"
        alt="Enter icon"
        class="h-4 w-4 cursor-pointer"
        @click="() => SideBarDataFunction()"
      />
    </div>
  </div>
</template>

<style scoped></style>
