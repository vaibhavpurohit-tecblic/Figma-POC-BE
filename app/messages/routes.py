import uuid
from flask import request, jsonify

from app.extensions import db
from app.utils import get_user_message_by_chat_id, generate_ad, generate_expert_bot_thread, create_user_message_by_chat_id, \
    get_user_message_by_message_id
from app.messages import bp


@bp.route('/api/<int:userId>/ad-copy/<chatId>/message', methods=['GET', 'POST'])
@bp.route('/api/<int:userId>/expert-bot/<chatId>/message', methods=['GET', 'POST'])
def method_user_message_by_chat_id(userId, chatId):
    if request.method == "GET":
        print("HAHA")
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

        if 'expert-bot' in request.url:
            result = generate_expert_bot_thread(messageContent)
        else:
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


@bp.route('/api/<int:userId>/ad-copy/<chatId>/message/<messageId>', methods=['GET'])
@bp.route('/api/<int:userId>/expert-bot/<chatId>/message/<messageId>', methods=['GET'])
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
