import axios from "axios";
import { APIResponseFunction } from "../../components/Constants/index.js";

export async function ProductListApiFunction() {
  const result = await axios
    .get("/api/products")
    .then((res) => {
      return res?.data?.products_data?.list || [];
    })
    .catch((err) => {
      APIResponseFunction(err);
      return [];
    });

  return result;
}
