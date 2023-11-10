<script setup>
import Header from "../components/General/Header.vue";
import Sidebar from "../components/General/Sidebar.vue";
import ProductSelect from "../components/General/ProductSelect.vue";
import CustomerInputBox from "../components/General/CustomerInputBox.vue";
</script>

<template>
  <div class="flex flex-col gap-3 min-h-screen overflow-hidden">
    <Header :auth="true" active="ad-copy" />
    <div class="flex-1 flex gap-7 container p-5 mx-auto">
      <Sidebar title="Create New Ad Copy" />
      <div class="flex-1 grid grid-cols-5">
        <div class="col-span-1"></div>
        <div class="col-span-3">
          <div class="flex flex-col justify-between gap-5 h-full">
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
                  <ProductSelect :active="true" />
                </div>
              </div>
            </div>
            <div class="">
              <CustomerInputBox />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
