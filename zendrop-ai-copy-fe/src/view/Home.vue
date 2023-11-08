<script setup>
import Header from "../components/General/Header.vue";
</script>

<template>
  <div class="flex flex-col gap-3 min-h-screen overflow-hidden">
    <Header :auth="false" active="" />
    <div
      class="flex-1 home-screen-background-img flex flex-col justify-center relative"
    >
      <div class="container mx-auto px-5">
        <div class="grid grid-cols-3 gap-7">
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
            <button
              class="text-base text-primary font-normal border border-primary rounded-[100px] w-full mt-7 py-2"
            >
              Create Now
            </button>
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
          <div class="">
            <img
              src="../assets/images/roboMan.png"
              alt="Robo Man"
              class="mt-20"
            />
          </div>
        </div>
        <div class="home-screen-blurred-container"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-screen-background-img {
  background-image: url(../assets/images/AppBackground.png);
}

.home-screen-blurred-container {
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
</style>
