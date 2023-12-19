<script setup>
import { onMounted, ref } from "vue";
import { ProductListApiFunction } from "../../api/ProductApis/index.js";
import {
  AdCopyChatCreateApiFunction,
  AdCopyChatMessagesAddApiFunction,
} from "../../api/AdCopyApis/index.js";
import { RedirectPage, ReloadPage } from "../Constants/index.js";

const props = defineProps({
  active: Boolean,
  loading: Boolean,
  filledValues: String,
  loadingFunction: Function,
});

const isDropdown = ref(false);
const dropDownList = ref([]);
const dropDownValue = ref(null);

function DropdownTrigger() {
  if (props.active) {
    if (isDropdown.value) {
      isDropdown.value = false;
    } else {
      isDropdown.value = true;
    }
  }
}

async function ProductListFunction() {
  const result = await ProductListApiFunction();

  dropDownList.value = result;
}

function ProductSelectionFunction(product) {
  dropDownValue.value = product;
  isDropdown.value = false;
}

async function AdCopyChatMessagesAddFunction(data) {
  const result = await AdCopyChatMessagesAddApiFunction(data);

  if (result.status === 200) {
    RedirectPage("/ad-copy?" + result?.data?.message?.chatId);
  } else {
    ReloadPage();
  }
}

async function ProductDetailsFunction() {
  if (dropDownValue.value && props.active && !props.loading) {
    props.loadingFunction();
    const result = await AdCopyChatCreateApiFunction({
      messageContent: dropDownValue?.value?.product?.name || "",
    });

    if (result.status === 200) {
      AdCopyChatMessagesAddFunction({
        id: result.data.chat.id,
        messageContent: result.data.chat.title || "",
      });
    }
  }
}

onMounted(() => ProductListFunction());
</script>

<template>
  <p class="text-gray-400 font-normal text-sm">Select Product</p>
  <div class="relative">
    <div
      :class="{
        'border border-secondary py-3 px-6 rounded-xl flex gap-4 justify-between items-center mt-1 cursor-pointer':
          props.active && !props.loading,
        'border border-gray-500 py-3 px-6 rounded-xl flex gap-4 justify-between items-center mt-1 cursor-pointer':
          !props.active || props.loading,
      }"
      @click="DropdownTrigger"
    >
      <p
        class="flex-1 text-primary font-normal text-sm"
        v-if="dropDownValue === null && filledValues === ''"
      >
        Select your Product
      </p>
      <p class="flex-1 text-primary font-normal text-sm" v-else>
        {{ dropDownValue?.product?.name || filledValues || "" }}
      </p>
      <img
        src="../../assets/logos/downArrow.svg"
        alt="Profile Pic"
        class="rounded-full h-[15px] w-[15px]"
      />
    </div>
    <div class="absolute z-10 w-full" v-if="isDropdown">
      <div
        class="border border-secondary rounded-xl py-3 px-6 bg-white"
        v-if="dropDownList.length === 0"
      >
        <h5 class="text-primary font-medium">No Products Found</h5>
      </div>
      <div
        class="border border-secondary rounded-xl py-2 bg-white max-h-28 overflow-y-auto"
        v-else
      >
        <h5
          class="text-primary font-medium py-2 px-6 cursor-pointer hover:bg-secondary hover:text-white"
          v-for="item in dropDownList"
          @click="() => ProductSelectionFunction(item)"
        >
          {{ item.product.name }}
        </h5>
      </div>
    </div>
  </div>
  <button
    :class="{
      'bg-quaternary py-3 w-full mt-7 text-white rounded-xl':
        props.active && !props.loading,
      ' bg-gray-500 py-3 w-full mt-7 text-white rounded-xl':
        !props.active || props.loading,
    }"
    @click="() => ProductDetailsFunction()"
  >
    Create Now
  </button>
</template>

<style scoped></style>
