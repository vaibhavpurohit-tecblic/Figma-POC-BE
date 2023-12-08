<script setup>
import { onMounted, ref } from "vue";
import SidebarTitle from "./SidebarTitle.vue";
import { AdCopyListApiFunction } from "../../api/AdCopyApis/index.js";
import { ExpertBotListApiFunction } from "../../api/ExpertBotApis/index.js";

defineProps({
  title: String,
  // :sidebarClose="sidebarClose"
  //         :SidebarCloseStartFunction="SidebarCloseStartFunction"
  //         :SidebarCloseStopFunction="SidebarCloseStopFunction"
});

const sideBarChatList = ref([]);

function RedirectLinkFunction() {
  if (window.location.pathname === "/ad-copy") {
    window.location.href = "/ad-copy";
  } else if (window.location.pathname === "/expert-bot") {
    window.location.href = "/expert-bot";
  }
}

async function AdCopyChatListFunction() {
  const result = await AdCopyListApiFunction();

  if (result.status === 200) {
    sideBarChatList.value = result?.data?.chats || [];
  } else {
    sideBarChatList.value = [];
  }
}

async function ExpertBotChatListFunction() {
  const result = await ExpertBotListApiFunction();

  if (result.status === 200) {
    sideBarChatList.value = result?.data?.chats || [];
  } else {
    sideBarChatList.value = [];
  }
}

function SideBarDataFunction() {
  if (window.location.pathname === "/ad-copy") {
    AdCopyChatListFunction();
  } else if (window.location.pathname === "/expert-bot") {
    ExpertBotChatListFunction();
  }
}

onMounted(() => {
  SideBarDataFunction();
});
</script>

<template>
  <div class="py-5 px-6">
    <div class="flex flex-col gap-4">
      <div class="flex gap-4">
        <div
          class="rounded-xl border-2 border-secondary py-2 px-6 flex items-center gap-3 w-full cursor-pointer"
          @click="() => RedirectLinkFunction()"
        >
          <img src="../../assets/logos/addIcon.svg" alt="" class="h-4 w-4" />
          <p class="text-base text-primary font-medium">{{ title }}</p>
        </div>
        <div
          class="hidden md:block p-3 rounded-xl border-2 border-secondary flex-none"
        >
          <img
            src="../../assets/logos/sidebarIcon.svg"
            alt="Sidebar Logo"
            class="w-6 h-6"
          />
        </div>
      </div>
      <div
        class="flex flex-col gap-3 h-[calc(100vh-105px)] md:h-[calc(100vh-260px)] overflow-auto"
      >
        <p class="text-sm text-gray-500 font-normal">Today</p>
        <div
          class="flex flex-col gap-3"
          v-for="item in sideBarChatList"
          :key="item.id"
        >
          <SidebarTitle :title="item.title" :id="item.id" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
