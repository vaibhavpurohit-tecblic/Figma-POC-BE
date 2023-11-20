import axios from "axios";

export default async function ProductListApiFunction() {
  const result = await axios
    .get("/api/api/trending_products")
    .then((res) => {
      return res?.data?.data?.trending_product || [];
    })
    .catch((err) => {
      console.error(err);
      return [];
    });

  return result;
}
