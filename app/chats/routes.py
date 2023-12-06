import uuid
from flask import request, jsonify

from app.extensions import db
from app.utils import get_user_chat_by_user_id, create_user_chat_by_user_id, get_user_chat_by_chat_id, \
    delete_user_chat_by_chat_id
from app.chats import bp


@bp.route('/api/<int:userId>/ad-copy', methods=['GET', 'POST'])
@bp.route('/api/<int:userId>/expert-bot', methods=['GET', 'POST'])
def method_user_chat_by_user_id(userId):
    product = 'expert-bot' if 'expert-bot' in request.url else 'ad-copy'
    
    if request.method == "GET":
        try:
            chats = get_user_chat_by_user_id(userId, product)

            response = {
                "status": 200,
                "data": {
                    "chats": chats
                },
                "pid": str(uuid.uuid4()),
                "message": "Success"
            }
        except Exception as e:
            response = {
                "status": 404,
                "message": "Not Found"
            }

        return jsonify(response)
    elif request.method == "POST":
        messageContent = request.get_json()['messageContent']

        try:
            chat = create_user_chat_by_user_id(userId, messageContent, product, db)

            response = {
                "status": 200,
                "data": {
                    "chat": chat
                },
                "pid": str(uuid.uuid4()),
                "message": "Success"
            }
        except Exception as e:
            response = {
                "status": 405,
                "message": "Method Not Allowed"
            }

        return jsonify(response)


@bp.route('/api/<int:userId>/ad-copy/<chatId>', methods=['GET', 'DELETE'])
@bp.route('/api/<int:userId>/expert-bot/<chatId>', methods=['GET', 'DELETE'])
def method_user_chat_by_chat_id(userId, chatId):
    product = 'expert-bot' if 'expert-bot' in request.url else 'ad-copy'

    if request.method == "GET":
        try:
            chat = get_user_chat_by_chat_id(userId, chatId, product)

            response = {
                "status": 200,
                "data": {
                    "chat": chat
                },
                "pid": str(uuid.uuid4()),
                "message": "Success"
            }
        except Exception as e:
            response = {
                "status": 404,
                "message": "Not Found"
            }

        return jsonify(response)
    elif request.method == "DELETE":
        try:
            delete_user_chat_by_chat_id(userId, chatId, product, db)

            response = {
                "status": 200,
                "pid": str(uuid.uuid4()),
                "message": "Success"
            }
        except Exception as e:
            response = {
                "status": 405,
                "message": "Method Not Allowed"
            }

        return jsonify(response)
