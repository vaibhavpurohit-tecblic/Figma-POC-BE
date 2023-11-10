import axios from "axios";

export default async function ProductListApiFunction() {
  const result = await axios
    .get("/api/api/trending_products")
    .then((res) => console.log(res))
    .catch((err) => console.log(err));

  return result;
}
