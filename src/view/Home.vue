<script setup>
import { onMounted, ref } from "vue";
import Header from "../components/General/Header.vue";

const redirectLink = ref("/ad-copy");

function RedirectLinkChangeFunction() {
  if (document?.cookie?.split("is_login=")?.[1]) {
    redirectLink.value = "/ad-copy";
  } else {
    redirectLink.value = "/";
  }
}

onMounted(() => RedirectLinkChangeFunction());
</script>

<template>
  <div class="flex flex-col gap-3 min-h-screen max-h-screen overflow-hidden">
    <Header :auth="false" active="" />
    <div
      class="flex-1 home-screen-background-img flex flex-col justify-center md:relative home-screen-blurred-container overflow-y-auto md:overflow-y-hidden overflow-x-hidden"
    >
      <div class="container mx-auto p-5 h-[calc(100vh-100px)] md:h-auto">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-7">
          <div class="">
            <h3 class="text-8xl text-primary font-semibold">
              Create<br />
              with<br />
              ZD-<span class="text-secondary">AI</span>
            </h3>
            <p class="text-primary leading-6 text-sm font-normal mt-6">
              Your AI Content Generator by Zendrop. Elevate your dropshipping
              game with this powerful tool designed to supercharge your sales.
            </p>
            <router-link :to="redirectLink">
              <button
                class="text-base text-primary font-normal border border-primary rounded-[100px] w-full mt-7 py-2"
              >
                Create Now
              </button>
            </router-link>
          </div>
          <div class="place-self-center">
            <div class="flex flex-col gap-4 w-full">
              <div class="flex gap-3">
                <div class="">
                  <img
                    src="../assets/logos/ad-copy.gif"
                    alt="Ad Copy Logo"
                    class="h-[77px] w-[77px]"
                  />
                </div>
                <div class="flex flex-col justify-evenly">
                  <h6 class="text-base text-primary font-semibold">
                    Ad Copies
                  </h6>
                  <p class="text-sm text-primary font-normal">
                    Compelling Ad Copies that Captivates
                  </p>
                </div>
              </div>
            </div>
            <div class="flex flex-col gap-4 w-full">
              <div class="flex gap-3">
                <div class="">
                  <img
                    src="../assets/logos/video-creator.gif"
                    alt="Ad Copy Logo"
                    class="h-[77px] w-[77px]"
                  />
                </div>
                <div class="flex flex-col justify-evenly">
                  <h6 class="text-base text-primary font-semibold">
                    Video Creator
                  </h6>
                  <p class="text-sm text-primary font-normal">
                    Crafting Visual Stories that Resonate
                  </p>
                </div>
              </div>
            </div>
            <div class="flex flex-col gap-4 w-full">
              <div class="flex gap-3">
                <div class="">
                  <img
                    src="../assets/logos/expert-bot.gif"
                    alt="Ad Copy Logo"
                    class="h-[77px] w-[77px]"
                  />
                </div>
                <div class="flex flex-col justify-evenly">
                  <h6 class="text-base text-primary font-semibold">
                    Expert Bot
                  </h6>
                  <p class="text-sm text-primary font-normal">
                    Expert Advice, Always by Your Side
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div class="relative robo-blurred-container">
            <img
              src="../assets/images/roboMan.png"
              alt="Robo Man"
              class="mt-20"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-screen-background-img {
  background-image: url(../assets/images/AppBackground.png);
}

@media only screen and (min-width: 501px) {
  .home-screen-blurred-container::after {
    content: "";
    position: absolute;
    left: 75vw;
    top: 10vh;
    height: 100vh;
    width: 100vw;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
  }
}

@media only screen and (max-width: 500px) {
  .robo-blurred-container::after {
    content: "";
    position: absolute;
    left: 50vw;
    top: 0;
    height: 100%;
    width: 100vw;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
  }
}
</style>
