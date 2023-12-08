# import uuid
# from flask import request, jsonify

# from app.extensions import db
# from app.utils import get_user_message_by_chat_id, generate_ad, generate_expert_bot_thread, create_user_message_by_chat_id, \
#     get_user_message_by_message_id
# from app.messages import bp


# @bp.route('/api/<int:userId>/ad-copy/<chatId>/message', methods=['GET', 'POST'])
# @bp.route('/api/<int:userId>/expert-bot/<chatId>/message', methods=['GET', 'POST'])
# def method_user_message_by_chat_id(userId, chatId):
#     product = 'expert-bot' if 'expert-bot' in request.url else 'ad-copy'

#     if request.method == "GET":
#         try:
#             messages = get_user_message_by_chat_id(userId, chatId, product)

#             response = {
#                 "status": 200,
#                 "data": {
#                     "messages": messages
#                 },
#                 "pid": str(uuid.uuid4()),
#                 "message": "Success"
#             }
#         except Exception as e:
#             response = {
#                 "status": 404,
#                 "message": "Not Found"
#             }

#         return jsonify(response)
#     elif request.method == "POST":
#         messageContent = request.get_json()['messageContent']
#         prompt = "Write an ad. copy for: " + messageContent

#         try:
#             if product == 'expert-bot':
#                 result = generate_expert_bot_thread(prompt)
#             else:
#                 result = generate_ad(prompt)

#             message = create_user_message_by_chat_id(userId, chatId, prompt, result, product, db)

#             response = {
#                 "status": 200,
#                 "data": {
#                     "message": message["user_message"],
#                     "responseMessageId": message["responseMessageId"]
#                 },
#                 "pid": str(uuid.uuid4()),
#                 "message": "Success"
#             }
#         except Exception as e:
#             response = {
#                 "status": 405,
#                 "message": "Method Not Allowed"
#             }

#         return jsonify(response)


# @bp.route('/api/<int:userId>/ad-copy/<chatId>/message/<messageId>', methods=['GET'])
# @bp.route('/api/<int:userId>/expert-bot/<chatId>/message/<messageId>', methods=['GET'])
# def method_user_message_by_message_id(userId, chatId, messageId):
#     product = 'expert-bot' if 'expert-bot' in request.url else 'ad-copy'

#     if request.method == "GET":
#         try:
#             message = get_user_message_by_message_id(userId, chatId, messageId, product)

#             response = {
#                 "status": 200,
#                 "data": {
#                     "message": message
#                 },
#                 "pid": str(uuid.uuid4()),
#                 "message": "Success"
#             }
#         except Exception as e:
#             response = {
#                 "status": 404,
#                 "message": "Not Found"
#             }

#         return jsonify(response)

### Shubham Updated code 
import uuid
from flask import request, jsonify

from app.extensions import db
from app.utils import (
    get_user_message_by_chat_id, generate_ad, generate_expert_bot_thread,
    create_user_message_by_chat_id, get_user_message_by_message_id
)
from app.messages import bp


def get_product_from_request(request):
    return 'expert-bot' if 'expert-bot' in request.url else 'ad-copy'


@bp.route('/api/<int:userId>/ad-copy/<chatId>/message', methods=['GET', 'POST'])
@bp.route('/api/<int:userId>/expert-bot/<chatId>/message', methods=['GET', 'POST'])
def method_user_message_by_chat_id(userId, chatId):
    product = get_product_from_request(request)

    if request.method == "GET":
        return handle_get_request(userId, chatId, product)
    elif request.method == "POST":
        return handle_post_request(userId, chatId, product)


def handle_get_request(userId, chatId, product):
    try:
        messages = get_user_message_by_chat_id(userId, chatId, product)
        return jsonify({
            "status": 200,
            "data": {"messages": messages},
            "pid": str(uuid.uuid4()),
            "message": "Success"
        })
    except Exception as e:
        # Log e for debugging
        return jsonify({"status": 404, "message": "Not Found"}), 404


def handle_post_request(userId, chatId, product):
    try:
        data = request.get_json()
        messageContent = data.get('messageContent')
        if not messageContent:
            return jsonify({"status": 400, "message": "Bad Request: Missing messageContent"}), 400

        prompt = "Write an ad. copy for: " + messageContent
        result = generate_expert_bot_thread(prompt) if product == 'expert-bot' else generate_ad(prompt)

        message = create_user_message_by_chat_id(userId, chatId, prompt, result, product, db)
        return jsonify({
            "status": 200,
            "data": {
                "message": message["user_message"],
                "responseMessageId": message["responseMessageId"]
            },
            "pid": str(uuid.uuid4()),
            "message": "Success"
        })
    except Exception as e:
        # Log e for debugging
        return jsonify({"status": 500, "message": "Internal Server Error"}), 500


@bp.route('/api/<int:userId>/ad-copy/<chatId>/message/<messageId>', methods=['GET'])
@bp.route('/api/<int:userId>/expert-bot/<chatId>/message/<messageId>', methods=['GET'])
def method_user_message_by_message_id(userId, chatId, messageId):
    product = get_product_from_request(request)

    try:
        message = get_user_message_by_message_id(userId, chatId, messageId, product)
        return jsonify({
            "status": 200,
            "data": {"message": message},
            "pid": str(uuid.uuid4()),
            "message": "Success"
        })
    except Exception as e:
        # Log e for debugging
        return jsonify({"status": 404, "message": "Not Found"}), 404
