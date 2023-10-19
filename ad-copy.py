import openai
from flask import Flask, request, jsonify
import json
import uuid
import datetime
from datetime import datetime, timezone

openai.api_key = "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"

app = Flask(__name__)

def generate_ad(prompt):
    output = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Write an ad. copy for: " + prompt,
        max_tokens=256,
        temperature=0
    )

    result = output["choices"][0]["text"]
    return result

def get_data():
    data_file = open('data.json')
    data = json.load(data_file)

    return data

def get_user_chat_by_user_id(userId):
    data = get_data()
    users = data["users"]
    chats = []

    for user in users:
        if user["id"] == userId:
            for chat in user["chats"]:
                del chat['messagesHistory']
                chats.append(chat)

    return chats

def create_user_chat_by_user_id(userId, messageContent):
    data = get_data()
    users = data["users"]
    chat_details = {}

    for user in users:
        if user["id"] == userId:
            chat_details = {
                "id": str(uuid.uuid4()),
                "userId": userId,
                "productId": 1,
                "title": messageContent,
                "messages": 0,
                "lastMessageId": None,
                "status": "posted",
                "createdAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
                "postedAt": None,
                "answeredAt": None,
                "closedAt": None,
                "messagesHistory": []
            }

            user["chats"].append(chat_details)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return chat_details

def get_user_chat_by_chat_id(userId, chatId):
    data = get_data()
    users = data["users"]
    chat_details = {}

    for user in users:
        if user["id"] == userId:
            for chat in user["chats"]:
                if chat["id"] == chatId:
                    del chat['messagesHistory']
                    chat_details = chat

    return chat_details

def delete_user_chat_by_chat_id(userId, chatId):
    data = get_data()
    users = data["users"]

    for user in users:
        if user["id"] == userId:
            for chat in user["chats"]:
                if chat["id"] == chatId:
                    chat["status"] = "closed"
                    chat["closedAt"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_user_message_by_chat_id(userId, chatId):
    data = get_data()
    users = data["users"]
    message_details = []

    for user in users:
        if user["id"] == userId:
            for chat in user["chats"]:
                if chat["id"] == chatId:
                    message_details = chat['messagesHistory']

    return message_details

def create_user_message_by_chat_id(userId, chatId, messageContent, result):
    data = get_data()
    users = data["users"]
    message_details = {}
    responseMessageId = ""

    for user in users:
        if user["id"] == userId:
            for chat in user["chats"]:
                if chat["id"] == chatId:
                    user_message = {
                        "id": str(uuid.uuid4()),
                        "chatId": chatId,
                        "author": "user",
                        "content": messageContent,
                        "createdAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
                    }

                    bot_message = {
                        "id": str(uuid.uuid4()),
                        "chatId": chatId,
                        "author": "bot",
                        "content": result,
                        "createdAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
                    }

                    message_details = user_message
                    responseMessageId = bot_message["id"]
                    chat["messages"] += 2
                    chat["lastMessageId"] = responseMessageId
                    chat["status"] = "answered"
                    chat["postedAt"] = user_message["createdAt"]
                    chat["answeredAt"] = bot_message["createdAt"]
                    chat["messagesHistory"].extend([user_message, bot_message])

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return {"message_details": message_details, "responseMessageId": responseMessageId}

def get_user_message_by_message_id(userId, chatId, messageId):
    data = get_data()
    users = data["users"]
    message_details = {}

    for user in users:
        if user["id"] == userId:
            for chat in user["chats"]:
                if chat["id"] == chatId:
                    for message in chat["messagesHistory"]:
                        if message["id"] == messageId:
                            message_details = message

    return message_details

@app.route("/")
def index():
    return """
        ZENDROP - AD COPY APIs<br><br>
        /api/{userId}/ad-copy - GET<br>
        /api/{userId}/ad-copy - POST<br>
        /api/{userId}/ad-copy/{chatId} - GET<br>
        /api/{userId}/ad-copy/{chatId} - DELETE<br>
        /api/{userId}/ad-copy/{chatId}/message - GET<br>
        /api/{userId}/ad-copy/{chatId}/message - POST<br>
        /api/{userId}/ad-copy/{chatId}/message/{messageId} - GET<br><br>
        As per the JSON data,<br>
        userId: 1 or 2<br>
        chatId: id in response<br>
        messageId: id in response<br>
    """

@app.route("/api/<int:userId>/ad-copy", methods=["GET", "POST"])
def user_chat_by_user_id(userId):
    if request.method == "GET":
        chats = get_user_chat_by_user_id(userId)

        response = {
            "status": "ok",
            "data": {
                "chats": chats
            },
            "pid": str(uuid.uuid4()),
            "message": ""
        }

        return jsonify(response)
    elif request.method == "POST":
        messageContent = request.get_json()['messageContent']

        chat = create_user_chat_by_user_id(userId, messageContent)

        response = {
            "status": "ok",
            "data": {
                "chat": chat
            },
            "pid": str(uuid.uuid4()),
            "message": ""
        }
        return jsonify(response)

@app.route("/api/<int:userId>/ad-copy/<chatId>", methods=["GET", "DELETE"])
def user_chat_by_chat_id(userId, chatId):
    if request.method == "GET":
        chat = get_user_chat_by_chat_id(userId, chatId)

        response = {
            "status": "ok",
            "data": {
                "chat": chat
            },
            "pid": str(uuid.uuid4()),
            "message": ""
        }

        return jsonify(response)
    elif request.method == "DELETE":
        delete_user_chat_by_chat_id(userId, chatId)

        response = {
            "status": "ok",
            "pid": str(uuid.uuid4()),
            "message": ""
        }
    
        return jsonify(response)

@app.route("/api/<int:userId>/ad-copy/<chatId>/message", methods=["GET", "POST"])
def user_message_by_chat_id(userId, chatId):
    if request.method == "GET":
        messages = get_user_message_by_chat_id(userId, chatId)

        response = {
            "status": "ok",
            "data": {
                "messages": messages
            },
            "pid": str(uuid.uuid4()),
            "message": ""
        }

        return jsonify(response)
    elif request.method == "POST":
        messageContent = request.get_json()['messageContent']
        result = generate_ad(messageContent)

        message = create_user_message_by_chat_id(userId, chatId, messageContent, result)

        response = {
            "status": "ok",
            "data": {
                "message": message["message_details"],
                "responseMessageId": message["responseMessageId"]
            },
            "pid": str(uuid.uuid4()),
            "message": ""
        }

        return jsonify(response)

@app.route("/api/<int:userId>/ad-copy/<chatId>/message/<messageId>")
def user_message_by_message_id(userId, chatId, messageId):
    if request.method == "GET":
        message = get_user_message_by_message_id(userId, chatId, messageId)

        response = {
            "status": "ok",
            "data": {
                "message": message
            },
            "pid": str(uuid.uuid4()),
            "message": ""
        }

        return jsonify(response)

if __name__=="__main__":
    app.run()
