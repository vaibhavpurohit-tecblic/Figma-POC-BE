export function GetLoginFlag() {
  return document?.cookie?.split("is_login=")?.[1] || false;
}

export function GetUserIDFlag() {
  return document?.cookie?.split("userID=")?.[1]?.split(";")?.[0] || 0;
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
  console.log(error);
}
