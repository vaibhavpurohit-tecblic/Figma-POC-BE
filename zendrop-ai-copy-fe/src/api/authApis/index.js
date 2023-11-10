import axios from "axios";

export default async function LoginApiFunction() {
  const result = await axios
    .get("/api/login")
    .then((res) => {
      // const additionalHeaderValue = response.headers["additional-header"];
      // console.log("Additional Header Value:", additionalHeaderValue);

      // Process the successful response
      console.log("Response Data:", response.data);
    })
    .catch((error) => {
      console.log(error, "Responce");
      if (error.response) {
        // The request was made, but the server responded with an error
        if (error.response.status === 302) {
          // Handle redirection
          const redirectLocation = error.response.headers.location;
          console.log("Redirect Location:", redirectLocation);

          // Now, you can make another request to the redirect location if needed
          axios
            .get(redirectLocation)
            .then((redirectResponse) => {
              console.log("Redirect Response Data:", redirectResponse.data);
            })
            .catch((redirectError) => {
              console.error("Error in redirect:", redirectError.message);
            });
        } else {
          // Handle other errors
          console.error("Error Data:", error.response.data);
        }
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
