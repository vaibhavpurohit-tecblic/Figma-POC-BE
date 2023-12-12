import axios from "axios";
import { APIResponseFunction } from "../../components/Constants/index.js";

export async function LogoutApiFunction() {
  const result = await axios
    .get("/api/logout")
    .then((res) => {
      return true;
    })
    .catch((error) => {
      APIResponseFunction(error);
      return false;
    });

  return result;
}
