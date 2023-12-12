import { useToast } from "vue-toast-notification";
import "vue-toast-notification/dist/theme-sugar.css";

export function GetLoginFlag() {
  return (
    document?.cookie
      ?.split("; ")
      ?.filter((item) => item.includes("is_login"))?.[0]
      ?.split("=")?.[1] || false
  );
}

export function GetUserIDFlag() {
  return (
    document?.cookie
      ?.split("; ")
      ?.filter((item) => item.includes("userID"))?.[0]
      ?.split("=")?.[1] || false
  );
}

export function ChangeLoginFlag() {
  document.cookie = "is_login=";
}

export function ChangeUserIDFlag() {
  document.cookie = "userID=";
}

export function GetPagePath() {
  return window.location.pathname;
}

export function GetPageSearch() {
  return window?.location?.search?.slice(1) || "";
}

export function RedirectPage(link) {
  window.location.href = link;
}

export function APIResponseFunction(error) {
  const $toast = useToast();

  console.log(error);

  $toast.error(
    error?.message ? error.message : "Server is Busy Please Try Again",
    {
      position: "top-right",
      duration: 2000,
    }
  );
}
