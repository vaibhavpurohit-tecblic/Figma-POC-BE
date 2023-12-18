<script setup>
import { ref } from "vue";
import { AdCopyChatMessagesAddApiFunction } from "../../api/AdCopyApis/index.js";
import {
  ExpertBotChatCreateApiFunction,
  ExpertBotChatMessagesAddApiFunction,
} from "../../api/ExpertBotApis/index.js";
import {
  GetPagePath,
  GetPageSearch,
  RedirectPage,
} from "../Constants/index.js";

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
    id: GetPageSearch(),
    messageContent: textMessage.value,
  });

  if (result.status === 200) {
    props.loadingStopFunction();
    textMessage.value = "";
  } else {
    props.loadingStopFunction();
    textMessage.value = "";
  }
}

async function ExpertBotChatCreateFunction() {
  const result = await ExpertBotChatCreateApiFunction({
    messageContent: textMessage.value,
  });

  if (result.status === 200) {
    ExpertBotChatMessagesAddFunction({
      id: result.data.chat.id,
      messageContent: result.data.chat.title || "",
    });
  } else {
    props.loadingStopFunction();
    textMessage.value = "";
  }
}

async function ExpertBotChatMessagesAddFunction(data) {
  const result = await ExpertBotChatMessagesAddApiFunction(data);

  if (result.status === 200 || result.status === 202) {
    if (GetPageSearch()?.length > 0) {
      props.loadingStopFunction();
      textMessage.value = "";
    } else {
      RedirectPage("/expert-bot?" + result?.data?.message?.chatId);
    }
  } else {
    props.loadingStopFunction();
    textMessage.value = "";
  }
}

function SideBarDataFunction() {
  if (textMessage.value.length > 0 && props.active && !props.loading) {
    props.loadingStartFunction();
    if (GetPagePath() === "/ad-copy") {
      AdCopyChatMessagesAddFunction();
    } else if (GetPagePath() === "/expert-bot") {
      if (GetPageSearch()?.length > 0) {
        ExpertBotChatMessagesAddFunction({
          id: GetPageSearch() || "",
          messageContent: textMessage.value,
        });
      } else {
        ExpertBotChatCreateFunction();
      }
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
