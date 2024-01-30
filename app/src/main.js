import { createApp } from "vue";
import "./style.css";
import "./assets/style/index.css";
import App from "./App.vue";
import { router } from "./routes/route.js";

const app = createApp(App);

app.use(router);

app.mount("#app");
