import axios from "axios";

export default async function LoginApiFunction() {
  const result = await axios
    .post("http://localhost:5000/login")
    .then((res) => console.log(res))
    .catch((err) => console.log(err));

  return result;
}
