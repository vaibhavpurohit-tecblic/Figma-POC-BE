import axios from "axios";

export async function AdCopyListApiFunction() {
  const result = await axios
    .get("/api/" + 4 + "/ad-copy")
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.log(err);
      return {};
    });

  return result;
}

export async function AdCopyChatCreateApiFunction(data) {
  const result = await axios
    .post("/api/" + 4 + "/ad-copy", data)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.log(err);
      return {};
    });

  return result;
}

export async function AdCopyChatDetailsApiFunction() {
  const result = await axios
    .get("/api/" + 4 + "/ad-copy" + 1)
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
    .delete("/api/" + 4 + "/ad-copy" + 1)
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function AdCopyChatMessagesListApiFunction(data) {
  const result = await axios
    .get("/api/" + 4 + "/ad-copy/" + data.id + "/message")
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.log(err);
      return {};
    });

  return result;
}

export async function AdCopyChatMessagesAddApiFunction(data) {
  const result = await axios
    .post("/api/" + 4 + "/ad-copy/" + data.id + "/message", data)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.log(err);
      return {};
    });

  return result;
}
