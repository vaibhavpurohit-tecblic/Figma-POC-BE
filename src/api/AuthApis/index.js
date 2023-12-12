import axios from "axios";

export async function LogoutApiFunction() {
  const result = await axios
    .get("/api/logout")
    .then((res) => {
      return res;
    })
    .catch((error) => {
      return {};
    });

  return result;
}
