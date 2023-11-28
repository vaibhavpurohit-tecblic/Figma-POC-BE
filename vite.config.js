import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";


export default ({ mode }) => {
  process.env = { ...process.env, ...loadEnv(mode, process.cwd(), "") };
  const isProduction = process.env.ENV === "prod";
  const herokuDomain = "https://zdai-ad-copy-745906f359ba.herokuapp.com";

  return defineConfig({
    base: "/",
    plugins: [vue()],
    build: {
      assetsDir: "assets",
    },
    server: {
      // port: isProduction ? process.env.PORT || 5173 : 4173,
      proxy: {
        "/api": {
          target: isProduction ? herokuDomain : "http://localhost:5000",
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, ""),
        },
      },
    },
  });
};
