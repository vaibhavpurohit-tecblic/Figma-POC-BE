/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#243c5a",
        secondary: "#8472ED",
        tertiary: "#F2F1F7",
        quaternary: "#212240",
      },
    },
  },
  plugins: [],
};