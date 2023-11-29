import uuid
import time
from datetime import datetime, timezone
import openai
from openai import OpenAI

from config import Config
from app.models.chats import Chats
from app.models.messages import Messages

openai.api_key = Config().API_KEY
assistant_id=Config().ASSISTANT_ID
client  = OpenAI(api_key=openai.api_key)
EXPERT_BOT = client.beta.assistants.retrieve(assistant_id=assistant_id)


def get_user_chat_by_user_id(userId):
    chats_by_user = Chats.query.filter_by(userId=userId).all()
    chats = []

    for chat in chats_by_user:
        chats.append({
            "id": chat.id,
            "userId": chat.userId,
            "productId": chat.productId,
            "title": chat.title,
            "messages": chat.messages,
            "lastMessageId": chat.lastMessageId,
            "status": chat.status,
            "createdAt": chat.createdAt,
            "postedAt": chat.postedAt,
            "answeredAt": chat.answeredAt,
            "closedAt": chat.closedAt
        })

    return chats


def create_user_chat_by_user_id(userId, messageContent, db):
    chat = Chats(
        id=str(uuid.uuid4()),
        userId=userId,
        productId=1,
        title=messageContent,
        messages=0,
        status='posted',
        createdAt=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        postedAt=None,
        answeredAt=None,
        closedAt=None,
        lastMessageId=None
    )

    db.session.add(chat)
    db.session.commit()

    chat_details = {
        "id": chat.id,
        "userId": chat.userId,
        "productId": chat.productId,
        "title": chat.title,
        "messages": chat.messages,
        "lastMessageId": chat.lastMessageId,
        "status": chat.status,
        "createdAt": chat.createdAt,
        "postedAt": chat.postedAt,
        "answeredAt": chat.answeredAt,
        "closedAt": chat.closedAt
    }

    return chat_details


def get_user_chat_by_chat_id(userId, chatId):
    chat = Chats.query.filter_by(userId=userId, id=chatId).first()

    chat_details = {
        "id": chat.id,
        "userId": chat.userId,
        "productId": chat.productId,
        "title": chat.title,
        "messages": chat.messages,
        "lastMessageId": chat.lastMessageId,
        "status": chat.status,
        "createdAt": chat.createdAt,
        "postedAt": chat.postedAt,
        "answeredAt": chat.answeredAt,
        "closedAt": chat.closedAt
    }

    return chat_details


def delete_user_chat_by_chat_id(userId, chatId, db):
    chat = Chats.query.filter_by(userId=userId, id=chatId).first()

    chat.status = "closed"
    chat.closedAt = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    db.session.commit()


def generate_ad(prompt):
    output = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Write an ad. copy for: " + prompt,
        max_tokens=256,
        temperature=0
    )

    result = output["choices"][0]["text"]
    return result


def generate_expert_bot_thread(prompt):
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
        instructions="Please address the user as Jane Doe. The user has a premium account."
    )

    while run.status != 'completed':
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        time.sleep(3)

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    bot_response = ""

    for msg in messages.data:
        if msg.role == 'assistant':
            bot_response += msg.content[0].text.value + '\n\n'

    return bot_response


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
