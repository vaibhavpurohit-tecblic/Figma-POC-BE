import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

const isProduction = process.env.NODE_ENV === "production";
const herokuDomain = "https://zdai-ad-copy-745906f359ba.herokuapp.com";

export default defineConfig({
  base: isProduction ? `/${herokuDomain}/` : "/",
  plugins: [vue()],
  server: {
    port: isProduction ? 5173 : 4173,
    proxy: {
      "/api": {
        target: isProduction ? `${herokuDomain}:5000` : "http://localhost:5000",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});
