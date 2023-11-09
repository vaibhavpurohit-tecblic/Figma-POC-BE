import uuid

from flask import Blueprint, request, jsonify

from zdai_app import db
from controllers.message import get_user_message_by_chat_id, generate_ad, create_user_message_by_chat_id, \
    get_user_message_by_message_id

message_bp = Blueprint('message', __name__)


@message_bp.route('/api/<int:userId>/ad-copy/<chatId>/message', methods=['GET', 'POST'])
def method_user_message_by_chat_id(userId, chatId):
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

        message = create_user_message_by_chat_id(userId, chatId, messageContent, result, db)

        response = {
            "status": "ok",
            "data": {
                "message": message["user_message"],
                "responseMessageId": message["responseMessageId"]
            },
            "pid": str(uuid.uuid4()),
            "message": ""
        }

        return jsonify(response)


@message_bp.route('/api/<int:userId>/ad-copy/<chatId>/message/<messageId>', methods=['GET'])
def method_user_message_by_message_id(userId, chatId, messageId):
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
