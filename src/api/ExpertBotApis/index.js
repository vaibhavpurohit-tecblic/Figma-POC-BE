import axios from "axios";

export async function ExpertBotListApiFunction() {
  const result = await axios
    .get("/api/" + 5 + "/expert-bot")
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.log(err);
      return {};
    });

  return result;
}

export async function ExpertBotChatCreateApiFunction(data) {
  const result = await axios
    .post("/api/" + 5 + "/expert-bot", data)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.log(err);
      return {};
    });

  return result;
}

export async function ExpertBotChatDetailsApiFunction() {
  const result = await axios
    .get("/api/" + 5 + "/expert-bot" + 1)
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function ExpertBotChatDeleteApiFunction() {
  const result = await axios
    .delete("/api/" + 5 + "/expert-bot" + 1)
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function ExpertBotChatMessagesListApiFunction(data) {
  const result = await axios
    .get("/api/" + 5 + "/expert-bot/" + data.id + "/message")
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.log(err);
      return {};
    });

  return result;
}

export async function ExpertBotChatMessagesAddApiFunction(data) {
  const result = await axios
    .post("/api/" + 5 + "/expert-bot/" + data.id + "/message", data)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.log(err);
      return {};
    });

  return result;
}
