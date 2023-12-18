import axios from "axios";
import {
  GetUserIDFlag,
  APIResponseFunction,
} from "../../components/Constants/index.js";

export async function ExpertBotListApiFunction() {
  const result = await axios
    .get("/api/" + GetUserIDFlag() + "/expert-bot")
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}

export async function ExpertBotChatCreateApiFunction(data) {
  const result = await axios
    .post("/api/" + GetUserIDFlag() + "/expert-bot", data)
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

export async function ExpertBotChatDetailsApiFunction() {
  const result = await axios
    .get("/api/" + GetUserIDFlag() + "/expert-bot" + 1)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}

export async function ExpertBotChatDeleteApiFunction() {
  const result = await axios
    .delete("/api/" + GetUserIDFlag() + "/expert-bot" + 1)
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      APIResponseFunction(err);
      return {};
    });

  return result;
}

export async function ExpertBotChatMessagesListApiFunction(data) {
  const result = await axios
    .get("/api/" + GetUserIDFlag() + "/expert-bot/" + data.id + "/message")
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

export async function ExpertBotChatMessagesAddApiFunction(data) {
  const result = await axios
    .post(
      "/api/" + GetUserIDFlag() + "/expert-bot/" + data.id + "/message",
      data
    )
    .then((res) => {
      if (res.data.status === 202) {
        // The task is accepted for processing, check the task status
        console.log("here", res.data);
        async function TaskStats() {
          const tempSave = res.data;

          const result = await checkTaskStatus(res.data.data.taskId);
          console.log(result, tempSave);

          return tempSave;
        }

        TaskStats();
      } else if (res.data.status === 200) {
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

async function checkTaskStatus(taskId) {
  // Polling interval, you can adjust this based on your requirements
  const pollingInterval = 10000; // 10 seconds

  while (true) {
    const taskResult = await axios
      .get("/api/task-status/" + taskId)
      .then((res) => {
        console.log(res);
        // res.data;
        return res.data;
      })
      .catch((err) => {
        console.error(err);
        return {};
      });

    if (taskResult.status === "SUCCESS") {
      return taskResult.data;
    } else if (taskResult.status === "FAILURE") {
      console.error("Task failed:", taskResult.message);
      return {};
    }

    // Wait for the next polling interval
    await new Promise((resolve) => setTimeout(resolve, pollingInterval));
  }
}
