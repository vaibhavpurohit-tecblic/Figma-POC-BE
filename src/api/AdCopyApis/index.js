import axios from "axios";
import {
  GetUserIDFlag,
  APIResponseFunction,
} from "../../components/Constants/index.js";

export async function AdCopyListApiFunction() {
  const result = await axios
    .get("/api/" + GetUserIDFlag() + "/ad-copy")
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}

export async function AdCopyChatCreateApiFunction(data) {
  const result = await axios
    .post("/api/" + GetUserIDFlag() + "/ad-copy", data)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}

export async function AdCopyChatDetailsApiFunction() {
  const result = await axios
    .get("/api/" + GetUserIDFlag() + "/ad-copy" + 1)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}

export async function AdCopyChatDeleteApiFunction() {
  const result = await axios
    .delete("/api/" + GetUserIDFlag() + "/ad-copy" + 1)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}

export async function AdCopyChatMessagesListApiFunction(data) {
  const result = await axios
    .get("/api/" + GetUserIDFlag() + "/ad-copy/" + data.id + "/message")
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}

export async function AdCopyChatMessagesAddApiFunction(data) {
  const result = await axios
    .post("/api/" + GetUserIDFlag() + "/ad-copy/" + data.id + "/message", data)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}
