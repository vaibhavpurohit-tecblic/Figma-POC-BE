import uuid
from flask import request, jsonify
from app.models.messages import Messages
from app.models.chats import Chats

from app.extensions import db
from app.utils import get_user_message_by_chat_id, generate_ad, generate_expert_bot_thread, create_user_message_by_chat_id, \
    get_user_message_by_message_id, experimentalResult, experimentalQuestion, get_role_and_content
from app.messages import bp
import logging
from app.celery_config import celery

logging.basicConfig(level=logging.DEBUG)


@bp.route('/api/task-status/<string:task_id>', methods=['GET'])
def get_task_status(task_id):
    print("HAHA I AM CALLED")
    task = celery.AsyncResult(task_id)
    print("Task status", task)
    response_data = {
        'status': task.status,
        # 'message': task.info.get('message', ''),
        'message': task.info,
        'data': task.result,
    }
    return jsonify(response_data)


@celery.task
def generate_expert_bot_thread_async(messageContent, thread_id):
    try:
        # Your existing code for generate_expert_bot_thread
        result = generate_expert_bot_thread(messageContent, thread_id)
        return result
    except Exception as e:
        logging.error(f"An exception occurred: {e}")
        return {"status": 401, "message": "Unauthorized"}
    

@celery.task
def generate_ad_copy_thread_async(messageContent, product, userId, chatId,message):
    try:
        print("here 2")
        # Your existing code for generate_expert_bot_thread
        result = generate_ad(messageContent, product, userId, chatId, message)
        print("========================?>>>>>> one ", result)
        return result
    except Exception as e:
        logging.error(f"An exception occurred: {e}")
        return {"status": 401, "message": "Unauthorized"}



@bp.route('/api/<int:userId>/ad-copy/<chatId>/message', methods=['GET', 'POST'])
@bp.route('/api/<int:userId>/expert-bot/<chatId>/message', methods=['GET', 'POST'])
def method_user_message_by_chat_id(userId, chatId):
    product = 'expert-bot' if 'expert-bot' in request.url else 'ad-copy'

    if request.method == "GET":
        try:
            messages = get_user_message_by_chat_id(userId, chatId, product)

            response = {
                "status": 200,
                "data": {
                    "messages": messages
                },
                "pid": str(uuid.uuid4()),
                "message": "Success"
            }
            logging.info(f"GET method_user_message_by_chat_id successful for user {userId}, chat {chatId}")
        except Exception as e:
            logging.error(f"GET method_user_message_by_chat_id failed: {e}")
            response = {
                "status": 404,
                "message": "Not Found"
            }

        return jsonify(response)
    elif request.method == "POST":
        messageContent = request.get_json()['messageContent']
 
        try:
            if product == 'expert-bot':
                # Instead of calling generate_expert_bot_thread directly,
                # queue the task for background execution
                experimentalQuestion(userId, chatId, product, messageContent, db)

                chat = Chats.query.filter_by(userId=userId, id=chatId, product=product).first()
                thread_id = chat.thread_id

                result_task = generate_expert_bot_thread_async.apply_async(args=[messageContent, thread_id])
                # result = result_task.get()
                # result = generate_expert_bot_thread(messageContent)

                # Respond to the client immediately, do not wait for the result
                response = {
                    "status": 202,
                    "data": {
                        "message": "Task accepted for processing",
                        "taskId": result_task.id
                    },
                    "pid": str(uuid.uuid4()),
                    "message": "Accepted"
                }
                logging.info(f"POST method_user_message_by_chat_id accepted for user {userId}, chat {chatId}")
                return jsonify(response), 202
            else:
                print("here 1")
                experimentalQuestion(userId, chatId, product, messageContent, db)
                
                message = get_role_and_content(userId, chatId, product)
                
                print("here 2", message)

                # result = generate_ad(messageContent, userId, chatId, product)
                result = generate_ad_copy_thread_async.apply_async(args=[messageContent, product, userId, chatId, message])
                # print("------------->>> two", result)

                response = {
                    "status": 202,
                    "data": {
                        "message": "Task accepted for processing",
                        "taskId": result.id
                    },
                    "pid": str(uuid.uuid4()),
                    "message": "Accepted"
                }
                logging.info(f"POST method_user_message_by_chat_id accepted for user {userId}, chat {chatId}")
                return jsonify(response), 202

            # message = create_user_message_by_chat_id(userId, chatId, messageContent, result, product, db)

            # response = {
            #     "status": 200,
            #     "data": {
            #         "message": message["user_message"],
            #         "responseMessageId": message["responseMessageId"]
            #     },
            #     "pid": str(uuid.uuid4()),
            #     "message": "Success"
            # }
            # logging.info(f"POST method_user_message_by_chat_id successful for user {userId}, chat {chatId}")
        except Exception as e:
            logging.error(f"POST method_user_message_by_chat_id failed: {e}")
            response = {
                "status": 405,
                "message": "Method Not Allowed"
            }

        return jsonify(response)


@bp.route('/api/<int:userId>/ad-copy/<chatId>/message/<messageId>', methods=['GET'])
@bp.route('/api/<int:userId>/expert-bot/<chatId>/message/<messageId>', methods=['GET'])
def method_user_message_by_message_id(userId, chatId, messageId):
    product = 'expert-bot' if 'expert-bot' in request.url else 'ad-copy'

    if request.method == "GET":
        try:
            message = get_user_message_by_message_id(userId, chatId, messageId, product)

            response = {
                "status": 200,
                "data": {
                    "message": message
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



#  -----------------experimental-----------------
    
@bp.route('/api/<int:userId>/ad-copy/<chatId>/result', methods=['POST'])
@bp.route('/api/<int:userId>/expert-bot/<chatId>/result', methods=['POST'])
def method_user_message_by_chat_id_result(userId, chatId):
    product = 'expert-bot' if 'expert-bot' in request.url else 'ad-copy'

    messageContent = request.get_json()['messageContent']
    
    try:
        message = experimentalResult(userId, chatId, product, messageContent, db)
        print("HAHAHAHAHAHAHAHAHAAAAAAAA")
        print(message)
        response = {
                "status": 200,
                "data": {
                    "message": message["user_message"],
                },
                "pid": str(uuid.uuid4()),
                "message": "Success"
        }
        logging.info(f"POST method_user_message_by_chat_id successful for user {userId}, chat {chatId}")
    except Exception as e:
        logging.error(f"POST method_user_message_by_chat_id failed: {e}")
        response = {
            "status": 405,
            "message": "Method Not Allowed"
        }

    return jsonify(response)
        