import axios from "axios";

export async function ProductListApiFunction() {
  const result = await axios
    .get("/api/products")
    .then((res) => {
      console.log(res);
      return res?.data?.products_data?.list || [];
    })
    .catch((err) => {
      console.error(err);
      return [];
    });

  return result;
}

export async function ProductDetailsApiFunction({ id }) {
  console.log(id, "ProductDetailsApiFunction");
  const result = await axios
    .get("/api/products/" + id)
    .then((res) => {
      return res?.data?.product_detail || {};
    })
    .catch((err) => {
      return {};
    });

  return result;
}
