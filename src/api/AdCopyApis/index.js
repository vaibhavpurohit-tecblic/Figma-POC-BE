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
      if (res.data.status === 200) {
        return res.data;
      } else {
        APIResponseFunction(res.data);
        return {};
      }
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
      if (res.data.status === 200) {
        return res.data;
      } else {
        APIResponseFunction(res.data);
        return {};
      }
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
      if (res.data.status === 202) {
        return res.data;
      } else {
        APIResponseFunction(res.data);
        return {};
      }
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}

export async function CheckAdCopyTaskStatusApiFunction(data) {
  // Polling interval, you can adjust this based on your requirements
  const pollingInterval = 10000; // 10 seconds

  while (true) {
    const taskResult = await axios
      .get("/api/task-status/" + data.id)
      .then((res) => {
        return res.data;
      })
      .catch((err) => {
        return {};
      });

    if (taskResult.status === "SUCCESS") {
      return taskResult;
    } else if (taskResult.status === "FAILURE") {
      return {};
    }

    // Wait for the next polling interval
    await new Promise((resolve) => setTimeout(resolve, pollingInterval));
  }
}

export async function AdCopySendResultApiFunction(data) {
  const result = await axios
    .post("/api/" + GetUserIDFlag() + "/ad-copy/" + data.id + "/result", data)
    .then((res) => {
      if (res.data.status === 200) {
        return res.data;
      } else {
        APIResponseFunction(res.data);
        return {};
      }
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}
