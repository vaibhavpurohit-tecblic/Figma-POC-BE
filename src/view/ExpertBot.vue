<script setup>
import { onMounted, ref } from "vue";
import moment from "moment";
import MarkdownIt from "markdown-it";
import Header from "../components/General/Header.vue";
import Sidebar from "../components/General/Sidebar.vue";
import CustomerInputBox from "../components/General/CustomerInputBox.vue";
import {
  ExpertBotChatMessagesListApiFunction,
  ExpertBotChatCreateApiFunction,
  ExpertBotChatMessagesAddApiFunction,
  CheckExpertBotTaskStatusApiFunction,
  ExpertBotSendResultApiFunction,
} from "../api/ExpertBotApis/index.js";
import {
  GetPageSearch,
  RedirectPage,
  ReloadPage,
} from "../components/Constants/index.js";

const chatId = ref("");

const sidebarClose = ref(true);

function SidebarCloseStartFunction() {
  sidebarClose.value = false;
}

function SidebarCloseStopFunction() {
  sidebarClose.value = true;
}

const inputLoading = ref(false);

function scrollToElement(title) {
  var element = document.getElementById(title);

  if (element) {
    element.scrollIntoView({ behavior: "smooth" });
  }
}

function InputLoadingStartFunction() {
  inputLoading.value = true;

  setTimeout(() => {
    scrollToElement("loading-component");
  }, 500);
}

function InputLoadingStopFunction() {
  inputLoading.value = false;
  CheckPropsFunction();

  setTimeout(() => {
    scrollToElement("last-component");
  }, 3000);
}

const propsValue = ref("");

const chatDetails = ref([]);

const loadingViewText = ref("");

const loadingViewTime = ref("");

function UserViewingStartFunction(title) {
  loadingViewText.value = title;
  loadingViewTime.value = new Date();
}

function UserViewingStopFunction() {
  loadingViewText.value = "";
  loadingViewTime.value = "";
}

async function ExpertBotChatMessagesListApiFunctionFunction(data) {
  const result = await ExpertBotChatMessagesListApiFunction(data);

  if (result.status === 200) {
    chatDetails.value = result?.data?.messages || [];
  } else {
    chatDetails.value = [];
  }
}

function CheckPropsFunction() {
  propsValue.value = GetPageSearch();

  if (GetPageSearch()?.length > 0) {
    ExpertBotChatMessagesListApiFunctionFunction({
      id: GetPageSearch(),
    });
  }
}

async function ExpertBotChatCreateFunction(title) {
  loadingViewText.value = title;
  loadingViewTime.value = new Date();

  const result = await ExpertBotChatCreateApiFunction({
    messageContent: title,
  });

  if (result.status === 200) {
    chatId.value = result.data.chat.id;
    ExpertBotChatMessagesAddFunction({
      id: result.data.chat.id,
      messageContent: result.data.chat.title || "",
    });
  } else {
    ReloadPage();
  }
}

async function ExpertBotChatMessagesAddFunction(data) {
  const result = await ExpertBotChatMessagesAddApiFunction(data);

  if (result.status === 202) {
    CheckTaskStatusFunction({ id: result?.data?.taskId || 0 });
  } else {
    ReloadPage();
  }
}

async function CheckTaskStatusFunction(data) {
  const result = await CheckExpertBotTaskStatusApiFunction(data);
  if (result.status === "SUCCESS") {
    ExpertBotSendResultFunction({
      id: chatId.value,
      messageContent: result.data || "",
    });
  } else {
    ReloadPage();
  }
}

async function ExpertBotSendResultFunction(data) {
  const result = await ExpertBotSendResultApiFunction(data);
  if (result.status === 200) {
    RedirectPage("/expert-bot?" + result?.data?.message?.chatId || 0);
  } else {
    ReloadPage();
  }
}

function MarkDownConverter(text) {
  const md = new MarkdownIt();
  return md.render(
    text
      .replaceAll("【1†source】", "")
      .replaceAll("【2†source】", "")
      .replaceAll("【3†source】", "")
      .replaceAll("【4†source】", "")
      .replaceAll("【5†source】", "")
      .replaceAll("【6†source】", "")
      .replaceAll("【7†source】", "")
      .replaceAll("【8†source】", "")
      .replaceAll("【9†source】", "")
  );
}

function PreselectedChat(title) {
  inputLoading.value = true;
  ExpertBotChatCreateFunction(title);
}

onMounted(() => CheckPropsFunction());
</script>

<template>
  <div class="flex flex-col min-h-screen max-h-screen">
    <Header :auth="true" active="expert-bot" />
    <div class="flex-1 flex gap-7 container p-5 mx-auto">
      <div
        :class="{
          'sidebar-container hidden md:block': sidebarClose,
          'hidden md:block': !sidebarClose,
        }"
      >
        <Sidebar
          title="New Chat"
          :sidebarClose="sidebarClose"
          :SidebarCloseStartFunction="SidebarCloseStartFunction"
          :SidebarCloseStopFunction="SidebarCloseStopFunction"
        />
      </div>
      <div class="flex-1">
        <div class="flex flex-col justify-between gap-5 h-full">
          <div
            class="h-[calc(100vh-275px)] overflow-auto"
            v-if="propsValue.length > 0 || inputLoading"
          >
            <div class="" v-for="(item, index) in chatDetails" :key="item.id">
              <div
                class="grid grid-cols-1 md:grid-cols-6 mb-5"
                v-if="item.author === 'bot'"
                :id="chatDetails?.length - 1 === index ? 'last-component' : ''"
              >
                <div class="col-span-1"></div>
                <div class="col-span-1 md:col-span-3">
                  <div class="flex gap-4">
                    <img
                      src="../assets/images/roboProfile.png"
                      alt=""
                      class="h-14 w-14"
                    />
                    <div
                      class="py-4 px-7 rounded-xl bg-tertiary flex-1 w-[calc(100%-80px)]"
                    >
                      <div
                        class="text-primary text-sm font-normal markdown-container"
                        v-html="MarkDownConverter(item.content)"
                      ></div>
                    </div>
                  </div>
                </div>
                <div class="col-span-1">
                  <div class="pt-5 pl-4">
                    <div
                      class="flex justify-end md:justify-start gap-2 items-center"
                    >
                      <img
                        src="../assets/logos/dateIcon.svg"
                        alt=""
                        class="h-3 w-3"
                      />
                      <p class="text-xs font-normal text-gray-600 flex-none">
                        {{ moment(item.createdAt).format("DD MMM YYYY") }}
                      </p>
                      <img
                        src="../assets/logos/timeIcon.svg"
                        alt=""
                        class="h-3 w-3"
                      />
                      <p class="text-xs font-normal text-gray-600 flex-none">
                        {{ moment(item.createdAt).format("hh:mm A") }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="grid grid-cols-1 md:grid-cols-6 mb-5"
                v-if="item.author === 'user'"
              >
                <div class="col-span-1"></div>
                <div class="col-span-1 md:col-span-3">
                  <div class="flex gap-4">
                    <img
                      src="../assets/images/ProfilePhoto.png"
                      alt=""
                      class="h-14 w-14 rounded-full"
                    />
                    <div class="py-4 px-7 rounded-xl flex-1">
                      <p class="text-primary text-sm font-normal">
                        {{ item.content }}
                      </p>
                    </div>
                  </div>
                </div>
                <div class="col-span-1">
                  <div class="pt-5 pl-4">
                    <div
                      class="flex justify-end md:justify-start gap-2 items-center"
                    >
                      <img
                        src="../assets/logos/dateIcon.svg"
                        alt=""
                        class="h-3 w-3"
                      />
                      <p class="text-xs font-normal text-gray-600 flex-none">
                        {{ moment(item.createdAt).format("DD MMM YYYY") }}
                      </p>
                      <img
                        src="../assets/logos/timeIcon.svg"
                        alt=""
                        class="h-3 w-3"
                      />
                      <p class="text-xs font-normal text-gray-600 flex-none">
                        {{ moment(item.createdAt).format("hh:mm A") }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="" v-if="inputLoading">
              <div
                class="grid grid-cols-1 md:grid-cols-6"
                v-if="loadingViewText !== ''"
              >
                <div class="col-span-1"></div>
                <div class="col-span-1 md:col-span-3">
                  <div class="flex gap-4">
                    <img
                      src="../assets/images/ProfilePhoto.png"
                      alt=""
                      class="h-14 w-14 rounded-full"
                    />
                    <div class="py-4 px-7 rounded-xl flex-1">
                      <p class="text-primary text-sm font-normal">
                        {{ loadingViewText }}
                      </p>
                    </div>
                  </div>
                </div>
                <div class="col-span-1">
                  <div class="pt-5 pl-4">
                    <div
                      class="flex justify-end md:justify-start gap-2 items-center"
                    >
                      <img
                        src="../assets/logos/dateIcon.svg"
                        alt=""
                        class="h-3 w-3"
                      />
                      <p class="text-xs font-normal text-gray-600 flex-none">
                        {{ moment(loadingViewTime).format("DD MMM YYYY") }}
                      </p>
                      <img
                        src="../assets/logos/timeIcon.svg"
                        alt=""
                        class="h-3 w-3"
                      />
                      <p class="text-xs font-normal text-gray-600 flex-none">
                        {{ moment(loadingViewTime).format("hh:mm A") }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="grid grid-cols-1 md:grid-cols-6 mt-5"
                id="loading-component"
              >
                <div class="col-span-1"></div>
                <div class="col-span-1 md:col-span-3">
                  <div class="flex gap-4">
                    <img
                      src="../assets/images/roboProfile.png"
                      alt=""
                      class="h-14 w-14"
                    />
                    <div
                      class="py-4 px-7 rounded-xl bg-tertiary flex-1 flex gap-3 items-center"
                    >
                      <h5 class="text-primary text-base font-medium">
                        Chat Bot is Typing
                      </h5>
                      <img
                        src="../assets/logos/chatLoading.svg"
                        alt=""
                        class="h-10 w-10"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="" v-if="propsValue.length === 0 && !inputLoading"></div>
          <div class="grid grid-cols-1 md:grid-cols-6">
            <div class="col-span-1"></div>
            <div class="col-span-1 md:col-span-3">
              <div class="" v-if="propsValue.length === 0 && !inputLoading">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-5">
                  <div
                    class="border border-secondary rounded-xl py-3 px-6 cursor-pointer"
                    @click="
                      () =>
                        PreselectedChat(
                          'Process of using zip code data for targeted advertising on Facebook?'
                        )
                    "
                  >
                    <h5 class="text-primary font-medium text-base">
                      Process of using
                    </h5>
                    <p class="text-primary/[0.5] text-xs font-normal">
                      zip code data for targeted advertising on Facebook?
                    </p>
                  </div>
                  <div
                    class="border border-secondary rounded-xl py-3 px-6 cursor-pointer"
                    @click="
                      () =>
                        PreselectedChat(
                          'How can I check and improve the load time of my webpage?'
                        )
                    "
                  >
                    <h5 class="text-primary font-medium text-base">
                      How can I check
                    </h5>
                    <p class="text-primary/[0.5] text-xs font-normal">
                      and improve the load time of my webpage?
                    </p>
                  </div>
                  <div
                    class="border border-secondary rounded-xl py-3 px-6 cursor-pointer"
                    @click="
                      () =>
                        PreselectedChat(
                          'What are the five effective methods for scaling Facebook ads?'
                        )
                    "
                  >
                    <h5 class="text-primary font-medium text-base">
                      What are the
                    </h5>
                    <p class="text-primary/[0.5] text-xs font-normal">
                      five effective methods for scaling Facebook ads?
                    </p>
                  </div>
                  <div
                    class="border border-secondary rounded-xl py-3 px-6 cursor-pointer"
                    @click="
                      () =>
                        PreselectedChat(
                          'How does page load time affect user experience and SEO?'
                        )
                    "
                  >
                    <h5 class="text-primary font-medium text-base">
                      How does page
                    </h5>
                    <p class="text-primary/[0.5] text-xs font-normal">
                      load time affect user experience and SEO?
                    </p>
                  </div>
                </div>
              </div>
              <CustomerInputBox
                active="true"
                :loading="inputLoading"
                :loadingStartFunction="InputLoadingStartFunction"
                :loadingStopFunction="InputLoadingStopFunction"
                :loadingUserViewingStartFunction="UserViewingStartFunction"
                :loadingUserViewingStopFunction="UserViewingStopFunction"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
