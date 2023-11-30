<script setup>
import { onMounted, ref } from "vue";
import Header from "../components/General/Header.vue";
import Sidebar from "../components/General/Sidebar.vue";
import ProductSelect from "../components/General/ProductSelect.vue";
import CustomerInputBox from "../components/General/CustomerInputBox.vue";

const propsValue = ref("");

function CheckPropsFunction() {
  propsValue.value = window.location.search;
}

onMounted(() => CheckPropsFunction());
</script>

<template>
  <div class="flex flex-col min-h-screen max-h-screen">
    <Header :auth="true" active="ad-copy" />
    <div class="flex-1 flex gap-7 container p-5 mx-auto">
      <div class="sidebar-container">
        <Sidebar title="Create New Ad Copy" />
      </div>
      <div class="flex-1">
        <div class="flex flex-col justify-between gap-5 h-full">
          <div class="h-[calc(100vh-275px)] overflow-auto">
            <div class="grid grid-cols-6">
              <div class="col-span-1"></div>
              <div class="col-span-3">
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
                      <ProductSelect :active="propsValue.length === 0" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="" v-if="propsValue.length > 0">
              <div class="grid grid-cols-6 mt-5">
                <div class="col-span-1"></div>
                <div class="col-span-3">
                  <div class="flex gap-4">
                    <img
                      src="../assets/images/roboProfile.png"
                      alt=""
                      class="h-14 w-14"
                    />
                    <div class="py-4 px-7 rounded-xl bg-tertiary flex-1">
                      <p class="text-primary text-sm font-normal">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                        sed do eiusmod tempor incididunt ut labore et dolore
                        magna aliqua. Ut enim ad minim veniam, quis nostrud
                        exercitation ullamco laboris nisi ut aliquip ex ea
                        commodo consequat. Duis aute irure dolor in
                        reprehenderit in voluptate velit esse cillum dolore eu
                        fugiat nulla pariatur. Excepteur sint occaecat cupidatat
                        non proident, sunt in culpa qui officia deserunt mollit
                        anim id est laborum."
                      </p>
                      <p class="text-primary text-sm font-normal">
                        Neque porro quisquam est, qui dolorem ipsum quia dolor
                        sit amet, consectetur, adipisci velit, sed quia non
                        numquam eius modi tempora incidunt ut labore et.
                      </p>
                      <p class="text-primary text-sm font-normal">
                        Duis aute irure dolor in reprehenderit in voluptate
                        velit esse cillum dolore eu fugiat nulla pariatur.
                        Excepteur sint occaecat cupidatat non proident, sunt in
                        culpa qui officia deserunt mollit anim id est laborum.
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
          </div>
          <div class="grid grid-cols-6">
            <div class="col-span-1"></div>
            <div class="col-span-3">
              <CustomerInputBox :active="propsValue.length > 0" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
