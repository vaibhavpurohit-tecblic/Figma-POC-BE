<script setup>
import { onMounted, ref } from "vue";
import SidebarTitle from "./SidebarTitle.vue";
import { AdCopyListApiFunction } from "../../api/AdCopyApis/index.js";
import { ExpertBotListApiFunction } from "../../api/ExpertBotApis/index.js";
import { GetPagePath, RedirectPage } from "../Constants/index.js";
import moment from "moment";

const props = defineProps({
  title: String,
  sidebarClose: Boolean,
  SidebarCloseStartFunction: Function,
  SidebarCloseStopFunction: Function,
});

function SideBarButtonFunction() {
  if (props.sidebarClose) {
    props.SidebarCloseStartFunction();
  } else {
    props.SidebarCloseStopFunction();
  }
}

const sideBarChatList = ref([]);

function RedirectLinkFunction() {
  if (GetPagePath() === "/ad-copy") {
    RedirectPage("/ad-copy");
  } else if (GetPagePath() === "/expert-bot") {
    RedirectPage("/expert-bot");
  }
}

function ChatDataSortingFunction(data) {
  var tempArray = [
    { title: "Today", chat: [] },
    { title: "Yesterday", chat: [] },
    { title: "Past 7 Days", chat: [] },
    { title: "Past 30 Days", chat: [] },
    { title: "Later Than 30 Days", chat: [] },
  ];

  var sortChat = data.sort(function (a, b) {
    return (
      moment(b.createdAt, "ddd, DD MMM YYYY HH:mm:ss [GMT]").valueOf() -
      moment(a.createdAt, "ddd, DD MMM YYYY HH:mm:ss [GMT]").valueOf()
    );
  });

  const currentDate = moment().format("LL");

  const yesterdayDate = moment(moment().subtract(1, "days")).format("LL");

  const weekDate = moment(moment().subtract(7, "days")).format("LL");

  const monthDate = moment(moment().subtract(30, "days")).format("LL");

  for (let i = 0; i < sortChat.length; i++) {
    var tempDate = moment(sortChat[i].createdAt).format("LL");
    if (moment(tempDate).isSame(currentDate)) {
      tempArray[0].chat = [...tempArray[0].chat, sortChat[i]];
    } else if (moment(tempDate).isSame(yesterdayDate)) {
      tempArray[1].chat = [...tempArray[1].chat, sortChat[i]];
    } else if (moment(tempDate).isAfter(weekDate)) {
      tempArray[2].chat = [...tempArray[2].chat, sortChat[i]];
    } else if (moment(tempDate).isAfter(monthDate)) {
      tempArray[3].chat = [...tempArray[3].chat, sortChat[i]];
    } else {
      tempArray[4].chat = [...tempArray[4].chat, sortChat[i]];
    }
  }

  sideBarChatList.value = tempArray?.filter((item) => item?.chat?.length > 0);
}

async function AdCopyChatListFunction() {
  const result = await AdCopyListApiFunction();

  if (result.status === 200) {
    ChatDataSortingFunction(result?.data?.chats || []);
  } else {
    sideBarChatList.value = [];
  }
}

async function ExpertBotChatListFunction() {
  const result = await ExpertBotListApiFunction();

  if (result.status === 200) {
    ChatDataSortingFunction(result?.data?.chats || []);
  } else {
    sideBarChatList.value = [];
  }
}

function SideBarDataFunction() {
  if (GetPagePath() === "/ad-copy") {
    AdCopyChatListFunction();
  } else if (GetPagePath() === "/expert-bot") {
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
          v-if="props.sidebarClose"
        >
          <img src="../../assets/logos/addIcon.svg" alt="" class="h-4 w-4" />
          <p class="text-base text-primary font-medium">{{ props.title }}</p>
        </div>
        <div
          class="p-3 rounded-xl border-2 border-secondary flex-none cursor-pointer"
          @click="() => SideBarButtonFunction()"
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
        v-if="props.sidebarClose"
      >
        <div class="" v-for="item in sideBarChatList" :key="item.id">
          <p class="text-sm text-gray-500 font-normal">{{ item.title }}</p>
          <div
            class="flex flex-col gap-3"
            v-for="item2 in item.chat"
            :key="item2.id"
          >
            <SidebarTitle :title="item2.title" :id="item2.id" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
