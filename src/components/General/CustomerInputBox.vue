<script setup>
import { ref } from "vue";
import { AdCopyChatMessagesAddApiFunction } from "../../api/AdCopyApis/index.js";
import {
  ExpertBotChatCreateApiFunction,
  ExpertBotChatMessagesAddApiFunction,
  CheckTaskStatusApiFunction,
  ExpertBotSendResultApiFunction,
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
  loadingUserViewingStartFunction: Function,
  loadingUserViewingStopFunction: Function,
});

const textMessage = ref("");

const chatId = ref("");

const viewText = ref("");

function nextStepProgress() {
  props.loadingUserViewingStopFunction();
  props.loadingStopFunction();
  textMessage.value = "";
  viewText.value = "";
}

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
    messageContent: viewText.value,
  });

  if (result.status === 200) {
    nextStepProgress();
  } else {
    nextStepProgress();
  }
}

async function ExpertBotChatCreateFunction() {
  const result = await ExpertBotChatCreateApiFunction({
    messageContent: viewText.value,
  });

  if (result.status === 200) {
    chatId.value = result.data.chat.id;
    ExpertBotChatMessagesAddFunction({
      id: result.data.chat.id,
      messageContent: result.data.chat.title || "",
    });
  } else {
    nextStepProgress();
  }
}

async function ExpertBotChatMessagesAddFunction(data) {
  const result = await ExpertBotChatMessagesAddApiFunction(data);

  if (result.status === 202) {
    CheckTaskStatusFunction({ id: result?.data?.taskId || 0 });
  } else {
    nextStepProgress();
  }
}

async function CheckTaskStatusFunction(data) {
  const result = await CheckTaskStatusApiFunction(data);
  if (result.status === "SUCCESS") {
    ExpertBotSendResultFunction({
      id: chatId.value,
      messageContent: result.data || "",
    });
  } else {
    nextStepProgress();
  }
}

async function ExpertBotSendResultFunction(data) {
  const result = await ExpertBotSendResultApiFunction(data);
  if (result.status === 200) {
    if (GetPageSearch()?.length > 0) {
      nextStepProgress();
    } else {
      RedirectPage("/expert-bot?" + result?.data?.message?.chatId);
    }
  } else {
    nextStepProgress();
  }
}

function SideBarDataFunction() {
  if (textMessage.value.length > 0 && props.active && !props.loading) {
    props.loadingStartFunction();
    props.loadingUserViewingStartFunction(textMessage.value);
    viewText.value = textMessage.value;

    textMessage.value = "";

    if (GetPagePath() === "/ad-copy") {
      AdCopyChatMessagesAddFunction();
    } else if (GetPagePath() === "/expert-bot") {
      if (GetPageSearch()?.length > 0) {
        chatId.value = GetPageSearch() || "";
        console.log(viewText.value, "viewText.value");
        ExpertBotChatMessagesAddFunction({
          id: GetPageSearch() || "",
          messageContent: viewText.value,
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
