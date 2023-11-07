import { createApp } from "vue";
import { createRouter, createWebHistory } from 'vue-router'
import Home from "../view/Home.vue";
import About from "../view/About.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/about", component: About },
];

export const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHistory(),
  routes, // short for `routes: routes`
});
