import uuid
from datetime import datetime, timezone

import openai

from config import Config
from models import Chats, Messages

openai.api_key = Config().API_KEY


def generate_ad(prompt):
    output = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Write an ad. copy for: " + prompt,
        max_tokens=256,
        temperature=0
    )

    result = output["choices"][0]["text"]
    return result


def get_user_message_by_chat_id(userId, chatId):
    chat = Chats.query.filter_by(userId=userId, id=chatId).first()
    messages_by_chat_id = Messages.query.filter_by(chatId=chat.id).all()
    message_details = []

    for message in messages_by_chat_id:
        message_details.append({
            "id": message.id,
            "chatId": message.chatId,
            "author": message.author,
            "content": message.content,
            "createdAt": message.createdAt
        })

    return message_details


def create_user_message_by_chat_id(userId, chatId, messageContent, result, db):
    chat = Chats.query.filter_by(userId=userId, id=chatId).first()

    user_message = Messages(
        id=str(uuid.uuid4()),
        chatId=chat.id,
        author="user",
        content=messageContent,
        createdAt=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    )

    bot_message = Messages(
        id=str(uuid.uuid4()),
        chatId=chat.id,
        author="bot",
        content=result,
        createdAt=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    )

    db.session.add(user_message)
    db.session.commit()

    db.session.add(bot_message)
    db.session.commit()

    responseMessageId = bot_message.id
    chat.messages += 2
    chat.lastMessageId = responseMessageId
    chat.status = "answered"
    chat.postedAt = user_message.createdAt
    chat.answeredAt = bot_message.createdAt

    db.session.commit()

    return {
        "user_message": {
            "id": user_message.id,
            "chatId": user_message.chatId,
            "author": user_message.author,
            "content": user_message.content,
            "createdAt": user_message.createdAt
        },
        "responseMessageId": responseMessageId
    }


def get_user_message_by_message_id(userId, chatId, messageId):
    chat = Chats.query.filter_by(userId=userId, id=chatId).first()
    message = Messages.query.filter_by(id=messageId, chatId=chat.id).first()

    message_details = {
        "id": message.id,
        "chatId": message.chatId,
        "author": message.author,
        "content": message.content,
        "createdAt": message.createdAt,
    }

    return message_details
