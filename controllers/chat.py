import uuid
from datetime import datetime, timezone

from models.chats import Chats


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
