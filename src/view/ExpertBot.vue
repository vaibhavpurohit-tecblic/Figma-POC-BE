<script setup>
import { onMounted, ref } from "vue";
import Header from "../components/General/Header.vue";
import Sidebar from "../components/General/Sidebar.vue";
import CustomerInputBox from "../components/General/CustomerInputBox.vue";

const propsValue = ref("");

function CheckPropsFunction() {
  propsValue.value = window.location.search;
}

onMounted(() => CheckPropsFunction());
</script>

<template>
  <div class="flex flex-col min-h-screen max-h-screen">
    <Header :auth="true" active="expert-bot" />
    <div class="flex-1 flex gap-7 container p-5 mx-auto">
      <Sidebar title="Create New Ad Copy" />
      <div class="flex-1">
        <div class="flex flex-col justify-between gap-5 h-full">
          <div
            class="h-[calc(100vh-275px)] overflow-auto"
            v-if="propsValue.length > 0"
          >
            <div class="grid grid-cols-6 mt-5">
              <div class="col-span-1"></div>
              <div class="col-span-3">
                <div class="flex gap-4">
                  <img
                    src="../assets/images/ProfilePhoto.png"
                    alt=""
                    class="h-14 w-14 rounded-full"
                  />
                  <div class="py-4 px-7 rounded-xl flex-1">
                    <p class="text-primary text-sm font-normal">
                      I dont like this, Can you provide something interesting.
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-span-1">
                <div class="pt-5 pl-4">
                  <div class="flex gap-2 items-center">
                    <img
                      src="../assets/logos/dateIcon.svg"
                      alt=""
                      class="h-3 w-3"
                    />
                    <p class="text-xs font-normal text-gray-600 flex-none">
                      24 Aug 2023
                    </p>
                    <img
                      src="../assets/logos/timeIcon.svg"
                      alt=""
                      class="h-3 w-3"
                    />
                    <p class="text-xs font-normal text-gray-600 flex-none">
                      11:34 pm
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div class="grid grid-cols-6 mt-5">
              <div class="col-span-1"></div>
              <div class="col-span-3">
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
                      class="h-4 w-10"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <di class="" v-if="propsValue.length === 0"></di>
          <div class="grid grid-cols-6">
            <div class="col-span-1"></div>
            <div class="col-span-3">
              <div class="" v-if="propsValue.length === 0">
                <div class="grid grid-cols-2 gap-5 mb-5">
                  <div class="border border-secondary rounded-xl py-3 px-6">
                    <h5 class="text-primary font-medium text-base">
                      Market Trend
                    </h5>
                    <p class="text-primary/[0.5] text-xs font-normal">
                      Expert Bot market trends and Lorem Ipsum.
                    </p>
                  </div>
                  <div class="border border-secondary rounded-xl py-3 px-6">
                    <h5 class="text-primary font-medium text-base">
                      Market Trend
                    </h5>
                    <p class="text-primary/[0.5] text-xs font-normal">
                      Expert Bot market trends and Lorem Ipsum.
                    </p>
                  </div>
                  <div class="border border-secondary rounded-xl py-3 px-6">
                    <h5 class="text-primary font-medium text-base">
                      Market Trend
                    </h5>
                    <p class="text-primary/[0.5] text-xs font-normal">
                      Expert Bot market trends and Lorem Ipsum.
                    </p>
                  </div>
                  <div class="border border-secondary rounded-xl py-3 px-6">
                    <h5 class="text-primary font-medium text-base">
                      Market Trend
                    </h5>
                    <p class="text-primary/[0.5] text-xs font-normal">
                      Expert Bot market trends and Lorem Ipsum.
                    </p>
                  </div>
                </div>
              </div>
              <CustomerInputBox active="true" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
