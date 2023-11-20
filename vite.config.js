import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";

// export default defineConfig({
//   base: isProduction ? `${herokuDomain}/` : "/",
//   plugins: [vue()],
//   server: {
//     port: isProduction ? 5173 : 4173,
//     proxy: {
//       "/api": {
//         target: isProduction ? `${herokuDomain}:5000` : "http://localhost:5000",
//         changeOrigin: true,
//         rewrite: (path) => path.replace(/^\/api/, ""),
//       },
//     },
//   },
// });

export default ({ mode }) => {
  process.env = { ...process.env, ...loadEnv(mode, process.cwd(), "") };

  const isProduction = process.env.ENV === "prod";
  const herokuDomain = "https://zdai-ad-copy-745906f359ba.herokuapp.com";

  // console.log(process.env);
  // console.log(process.env.DYNO?.split("run.")?.[1] || "5000");

  return defineConfig({
    base: "/",
    plugins: [vue()],
    server: {
      port: isProduction ? process.env.PORT || 5173 : 4173,
      proxy: {
        "/api": {
          target: isProduction ? "https://zdai-ad-copy-745906f359ba.herokuapp.com" : "http://localhost:5000",
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, ""),
        },
      },
    },
  });
};
