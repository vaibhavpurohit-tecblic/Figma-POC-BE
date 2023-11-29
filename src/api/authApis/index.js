import axios from "axios";

export async function LogoutApiFunction() {
  const result = await axios
    .get("/api/logout")
    .then((res) => {
      return res;
    })
    .catch((error) => {
      console.log(error, "Responce");
      if (error.response) {
        // The request was made, but the server responded with an error
        console.error("Error Data:", error.response.data);
      } else if (error.request) {
        // The request was made but no response was received
        console.error("No response received:", error.request);
      } else {
        // Something happened in setting up the request that triggered an Error
        console.error("Request setup error:", error.message);
      }
    });

  return result;
}
