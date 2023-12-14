<script setup>
import { onMounted, ref } from "vue";
import moment from "moment";
import Header from "../components/General/Header.vue";
import Sidebar from "../components/General/Sidebar.vue";
import ProductSelect from "../components/General/ProductSelect.vue";
import CustomerInputBox from "../components/General/CustomerInputBox.vue";
import { AdCopyChatMessagesListApiFunction } from "../api/AdCopyApis/index.js";
import { GetPageSearch } from "../components/Constants/index.js";

const propsValue = ref("");

const sidebarClose = ref(true);

function SidebarCloseStartFunction() {
  sidebarClose.value = false;
}

function SidebarCloseStopFunction() {
  sidebarClose.value = true;
}

const dropdownLoading = ref(false);

function DropDownLoadingStartFunction() {
  dropdownLoading.value = true;
}

const inputLoading = ref(false);

function InputLoadingStartFunction() {
  inputLoading.value = true;
}

function InputLoadingStopFunction() {
  inputLoading.value = false;
  CheckPropsFunction();
}

const initialProduct = ref("");

const chatDetails = ref([]);

async function AdCopyChatMessagesListFunction(data) {
  const result = await AdCopyChatMessagesListApiFunction(data);

  if (result.status === 200) {
    initialProduct.value =
      result?.data?.messages?.[0]?.content?.split(
        "Write an ad. copy for:"
      )?.[1] || "";
    chatDetails.value = result?.data?.messages?.splice(1) || [];
  } else {
    chatDetails.value = [];
  }
}

function CheckPropsFunction() {
  propsValue.value = GetPageSearch();

  if (GetPageSearch()?.length > 0) {
    AdCopyChatMessagesListFunction({
      id: GetPageSearch(),
    });
  }
}

onMounted(() => CheckPropsFunction());
</script>

<template>
  <div class="flex flex-col min-h-screen max-h-screen">
    <Header :auth="true" active="ad-copy" />
    <div class="flex-1 flex gap-7 container p-5 mx-auto">
      <div
        :class="{
          'sidebar-container hidden md:block': sidebarClose,
          'hidden md:block': !sidebarClose,
        }"
      >
        <Sidebar
          title="Create New Ad Copy"
          :sidebarClose="sidebarClose"
          :SidebarCloseStartFunction="SidebarCloseStartFunction"
          :SidebarCloseStopFunction="SidebarCloseStopFunction"
        />
      </div>
      <div class="flex-1">
        <div class="flex flex-col justify-between gap-5 h-full">
          <div class="h-[calc(100vh-275px)] overflow-auto">
            <div class="grid grid-cols-1 md:grid-cols-6">
              <div class="col-span-1"></div>
              <div class="col-span-1 md:col-span-3">
                <div class="flex flex-col gap-5">
                  <div class="flex gap-4">
                    <img
                      src="../assets/images/roboProfile.png"
                      alt=""
                      class="h-14 w-14"
                    />
                    <div class="py-4 px-7 rounded-xl bg-tertiary flex-1">
                      <h5 class="text-primary text-base font-medium">
                        Enter your details to Generate ad copy.
                      </h5>
                    </div>
                  </div>
                  <div class="flex gap-4">
                    <img
                      src="../assets/images/ProfilePhoto.png"
                      alt=""
                      class="h-14 w-14 rounded-full"
                    />
                    <div class="flex-1">
                      <ProductSelect
                        :active="propsValue.length === 0"
                        :loading="dropdownLoading"
                        :filledValues="initialProduct"
                        :loadingFunction="DropDownLoadingStartFunction"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="" v-if="propsValue.length > 0">
              <div class="" v-for="item in chatDetails" :key="item.id">
                <div
                  class="grid grid-cols-1 md:grid-cols-6 mt-5"
                  v-if="item.author === 'bot'"
                >
                  <div class="col-span-1"></div>
                  <div class="col-span-1 md:col-span-3">
                    <div class="flex gap-4">
                      <img
                        src="../assets/images/roboProfile.png"
                        alt=""
                        class="h-14 w-14"
                      />
                      <div class="py-4 px-7 rounded-xl bg-tertiary flex-1">
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
                <div
                  class="grid grid-cols-1 md:grid-cols-6 mt-5"
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
            </div>
            <div class="" v-if="dropdownLoading || inputLoading">
              <div class="grid grid-cols-1 md:grid-cols-6 mt-5">
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
          <div class="grid grid-cols-1 md:grid-cols-6">
            <div class="col-span-1"></div>
            <div class="col-span-1 md:col-span-3">
              <CustomerInputBox
                :active="propsValue.length > 0"
                :loading="inputLoading"
                :loadingStartFunction="InputLoadingStartFunction"
                :loadingStopFunction="InputLoadingStopFunction"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
