import axios from "axios";

export async function AdCopyListApiFunction() {
  const result = await axios
    .get("/api/" + 4 + "/ad-copy")
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function AdCopyChatCreateApiFunction() {
  const result = await axios
    .post("/api/" + 4 + "/ad-copy")
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function AdCopyChatDetailsApiFunction() {
  const result = await axios
    .get("/api/" + 1 + "/ad-copy" + 1)
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function AdCopyChatDeleteApiFunction() {
  const result = await axios
    .delete("/api/" + 1 + "/ad-copy" + 1)
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function AdCopyChatMessagesListApiFunction() {
  const result = await axios
    .get("/api/" + 4 + "/ad-copy" + 1 + "/message")
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function AdCopyChatMessagesAddApiFunction() {
  const result = await axios
    .post("/api/" + 1 + "/ad-copy" + 1 + "/message")
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}