import axios from "axios";

export default async function ProductListApiFunction() {
  const result = await axios
    .get("http://localhost:5000/login")
    .then((res) => console.log(res))
    .catch((err) => console.log(err));

  return result;
}
