<script setup>
import { onMounted, ref } from "vue";
import {
  GetPagePath,
  GetPageSearch,
  RedirectPage,
  ReloadPage,
} from "../Constants/index.js";
import DeleteModal from "./DeleteModal.vue";
import {
  AdCopyChatTitleChangeApiFunction,
  AdCopyChatDeleteApiFunction,
} from "../../api/AdCopyApis/index.js";
import {
  ExpertBotChatTitleChangeApiFunction,
  ExpertBotChatDeleteApiFunction,
} from "../../api/ExpertBotApis/index.js";

const props = defineProps({
  title: String,
  id: String,
});

const active = ref(false);

function CheckIfIdMatch() {
  if (GetPageSearch() === props.id) {
    active.value = true;
  } else {
    active.value = false;
  }
}

function RedirectToPage() {
  if (!active.value) {
    RedirectPage(GetPagePath() + "?" + props.id);
  }
}

const editActive = ref(false);

const changeTitle = ref("");

function EditFlagChange() {
  editActive.value = true;
  changeTitle.value = props.title;
}

function EditFlagCloseChange() {
  editActive.value = false;
  changeTitle.value = "";
}

function TitleChangeFunction(e) {
  changeTitle.value = e.target.value;
}

async function AdCopyTitleChangeFunction() {
  const result = await AdCopyChatTitleChangeApiFunction({
    chat_id: GetPageSearch(),
    new_title: changeTitle.value,
  });

  if (result.status === 200) {
    ReloadPage();
  } else {
    ReloadPage();
  }
}

async function ExpertBotTitleChangeFunction() {
  const result = await ExpertBotChatTitleChangeApiFunction({
    chat_id: GetPageSearch(),
    new_title: changeTitle.value,
  });

  if (result.status === 200) {
    ReloadPage();
  } else {
    ReloadPage();
  }
}

function EditTitle() {
  if (GetPagePath() === "/ad-copy") {
    AdCopyTitleChangeFunction();
  } else if (GetPagePath() === "/expert-bot") {
    ExpertBotTitleChangeFunction();
  }
}

const deleteModalActive = ref(false);

function DeleteModalFlagChange() {
  deleteModalActive.value = true;
}

function DeleteModalFlagCloseChange() {
  deleteModalActive.value = false;
}

async function AdCopyDeleteFunction() {
  const result = await AdCopyChatDeleteApiFunction({
    id: GetPageSearch(),
  });

  if (result.status === 200) {
    RedirectPage(GetPagePath());
  } else {
    ReloadPage();
  }
}

async function ExpertBotDeleteFunction() {
  const result = await ExpertBotChatDeleteApiFunction({
    id: GetPageSearch(),
  });

  if (result.status === 200) {
    RedirectPage(GetPagePath());
  } else {
    ReloadPage();
  }
}

function DeleteChatFunction() {
  if (GetPagePath() === "/ad-copy") {
    AdCopyDeleteFunction();
  } else if (GetPagePath() === "/expert-bot") {
    ExpertBotDeleteFunction();
  }
}

onMounted(() => CheckIfIdMatch());
</script>

<template>
  <div
    :class="{
      'flex items-center justify-between gap-4 rounded-xl py-3 px-6 cursor-pointer':
        !active,
      'flex items-center justify-between gap-4 rounded-xl py-3 px-6 bg-secondary':
        active,
    }"
    @click="() => RedirectToPage()"
  >
    <div class="">
      <input
        type="text"
        class="w-full bg-transparent focus-visible:outline-none text-white text-base font-medium border-b border-b-white"
        :value="changeTitle"
        @input="TitleChangeFunction"
        v-if="editActive"
      />
      <h6
        :class="{
          'text-primary text-base font-medium': !active,
          'text-white text-base font-medium': active,
        }"
        v-else
      >
        {{ props.title }}
      </h6>
    </div>
    <div class="flex gap-3 flex-none" v-if="editActive">
      <img
        src="../../assets/logos/check.svg"
        alt="Edit Icon"
        class="w-5 h-5 cursor-pointer"
        @click="() => EditTitle()"
      />
      <img
        src="../../assets/logos/close.svg"
        alt="Delete Icon"
        class="w-4 h-4 cursor-pointer"
        @click="() => EditFlagCloseChange()"
      />
    </div>
    <div class="flex gap-3 flex-none" v-else>
      <img
        src="../../assets/logos/editActive.svg"
        alt="Edit Icon"
        class="w-5 h-5 cursor-pointer"
        v-if="active"
        @click="() => EditFlagChange()"
      />
      <img
        src="../../assets/logos/editInActive.svg"
        alt="Edit Icon"
        class="w-5 h-5"
        v-else
      />
      <img
        src="../../assets/logos/deleteActive.svg"
        alt="Delete Icon"
        class="w-5 h-5 cursor-pointer"
        v-if="active"
        @click="() => DeleteModalFlagChange()"
      />
      <img
        src="../../assets/logos/deleteInActive.svg"
        alt="Delete Icon"
        class="w-5 h-5"
        v-else
      />
    </div>
    <DeleteModal
      :chat="props.title"
      :deleteModalActive="deleteModalActive"
      :deleteChatFunction="DeleteChatFunction"
      :deleteModalFlagCloseChange="DeleteModalFlagCloseChange"
    />
  </div>
</template>

<style scoped></style>
