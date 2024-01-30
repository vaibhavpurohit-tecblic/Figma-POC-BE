import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import Home from "../view/Home.vue";
import AdCopy from "../view/AdCopy.vue";
import ExpertBot from "../view/ExpertBot.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/ad-copy", component: AdCopy },
  { path: "/expert-bot", component: ExpertBot },
];

export const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHistory(),
  routes, // short for `routes: routes`
});
