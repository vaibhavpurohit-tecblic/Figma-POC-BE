import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  base: process.env.ENV === "prod" ? "https://zdai-ad-copy-745906f359ba.herokuapp.com/" : "/",
  plugins: [vue()],
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:5000", // Replace with your API base URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});
