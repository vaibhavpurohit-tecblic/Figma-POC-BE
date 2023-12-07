import axios from "axios";

export async function ExpertBotListApiFunction() {
  const result = await axios
    .get("/api/" + 1 + "/expert-bot")
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function ExpertBotChatCreateApiFunction() {
  const result = await axios
    .post("/api/" + 1 + "/expert-bot")
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function ExpertBotChatDetailsApiFunction() {
  const result = await axios
    .get("/api/" + 1 + "/expert-bot" + 1)
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
    .delete("/api/" + 1 + "/expert-bot" + 1)
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function ExpertBotChatMessagesListApiFunction() {
  const result = await axios
    .get("/api/" + 1 + "/expert-bot/" + 1 + "/message")
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}

export async function ExpertBotChatMessagesAddApiFunction(data) {
  const result = await axios
    .post("/api/" + 4 + "/expert-bot/" + data.id + "/message", data)
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return result;
}
