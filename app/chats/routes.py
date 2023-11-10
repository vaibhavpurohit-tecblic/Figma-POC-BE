import uuid
from flask import request, jsonify

from app.extensions import db
from app.utils import get_user_chat_by_user_id, create_user_chat_by_user_id, get_user_chat_by_chat_id, \
    delete_user_chat_by_chat_id
from app.chats import bp


@bp.route('/api/<int:userId>/ad-copy', methods=['GET', 'POST'])
def method_user_chat_by_user_id(userId):
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

        chat = create_user_chat_by_user_id(userId, messageContent, db)

        response = {
            "status": "ok",
            "data": {
                "chat": chat
            },
            "pid": str(uuid.uuid4()),
            "message": ""
        }
        return jsonify(response)


@bp.route('/api/<int:userId>/ad-copy/<chatId>', methods=['GET', 'DELETE'])
def method_user_chat_by_chat_id(userId, chatId):
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
        delete_user_chat_by_chat_id(userId, chatId, db)

        response = {
            "status": "ok",
            "pid": str(uuid.uuid4()),
            "message": ""
        }

        return jsonify(response)
