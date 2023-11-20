import axios from "axios";

export default async function ProductListApiFunction() {
  const result = await axios
    .get("/api/api/trending_products")
    .then((res) => {
      return res;
    })
    .catch((err) => {
      console.error(err);
      return [];
    });

  return result;
}
