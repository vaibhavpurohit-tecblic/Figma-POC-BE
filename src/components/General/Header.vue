<script setup>
import { onMounted, ref } from "vue";
import { LogoutApiFunction } from "../../api/authApis/index.js";

defineProps({
  auth: Boolean,
  active: String,
});

const isDropdown = ref(false);

function DropdownTrigger() {
  if (isDropdown.value) {
    isDropdown.value = false;
  } else {
    isDropdown.value = true;
  }
}

const isLoggedIn = ref(false);

function IfUserLoggedInFunction() {
  if (document?.cookie?.split("is_login=")?.[1]) {
    isLoggedIn.value = true;
  } else {
    isLoggedIn.value = false;
    if (window.location.pathname !== "/") {
      window.location.href = "/";
    }
  }
}

async function LogoutFunction() {
  document.cookie = "is_login=";
  const result = await LogoutApiFunction();

  isLoggedIn.value = false;
  isDropdown.value = false;
  window.location.href = "/";
}

function LoginFunction() {
  // const result = await LoginApiFunction();

  const redirectURL = `${window.location.origin}/login`;

  window.location.href = redirectURL;
}

onMounted(() => IfUserLoggedInFunction());
</script>

<template>
  <div
    class="container my-6 px-5 mx-auto flex justify-between gap-5 items-center"
  >
    <div class="">
      <router-link to="/">
        <img
          src="../../assets/logos/logo.svg"
          alt="ZenDrop Logo"
          class="h-[30px] w-[200px] cursor-pointer"
        />
      </router-link>
    </div>
    <div class="flex justify-end items-center gap-5" v-if="isLoggedIn">
      <div
        class="box-shadow-header-container px-3 py-2 flex gap-2 items-center"
      >
        <router-link to="/ad-copy">
          <div
            :class="{
              'py-2 px-10 border-2 cursor-pointer border-transparent hover:border-secondary rounded-[100px]':
                active !== 'ad-copy',
              'py-2 px-10 border-2 cursor-pointer border-secondary rounded-[100px]':
                active === 'ad-copy',
            }"
          >
            <h5 class="text-primary font-normal text-base">Ad Copy</h5>
          </div>
        </router-link>
        <router-link to="/expert-bot">
          <div
            :class="{
              'py-2 px-10 border-2 cursor-pointer border-transparent hover:border-secondary rounded-[100px]':
                active !== 'expert-bot',
              'py-2 px-10 border-2 cursor-pointer border-secondary rounded-[100px]':
                active === 'expert-bot',
            }"
          >
            <h5 class="text-primary font-normal text-base">Expert Bot</h5>
          </div>
        </router-link>
      </div>
      <div class="relative">
        <div
          class="box-shadow-header-container p-1 flex pl-9 gap-4 items-center cursor-pointer"
          @click="DropdownTrigger"
        >
          <p class="text-primary font-normal text-base">John Smith</p>
          <img
            src="../../assets/logos/downArrow.svg"
            alt="Profile Pic"
            class="rounded-full h-[15px] w-[15px]"
          />
          <img
            src="../../assets/images/ProfilePhoto.png"
            alt="Profile Pic"
            class="rounded-full h-[45px] w-[45px]"
          />
        </div>
        <div class="absolute z-30" v-if="isDropdown">
          <div class="flex justify-center w-[220px]">
            <div
              class="flex flex-col bg-white w-[150px] rounded-b-xl shadow-lg"
            >
              <h5
                class="px-4 py-3 cursor-pointer text-sm text-primary font-normal hover:text-white hover:bg-secondary"
              >
                Settings
              </h5>
              <h5
                class="px-4 py-3 cursor-pointer text-sm text-primary font-normal hover:text-white hover:bg-secondary rounded-b-xl"
                @click="LogoutFunction"
              >
                Logout
              </h5>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="py-2 px-10 border-2 cursor-pointer border-secondary rounded-[100px] box-shadow-header-container"
      @click="LoginFunction"
      v-else
    >
      <h5 class="text-primary font-normal text-base">Login</h5>
    </div>
  </div>
</template>

<style scoped>
.box-shadow-header-container {
  border-radius: 100px;
  background: #fff;
  box-shadow: 0px 4px 35px 0px rgba(133, 115, 238, 0.2);
}
</style>
