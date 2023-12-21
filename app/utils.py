import uuid
import time
import logging
from datetime import datetime, timezone, timedelta
from openai import OpenAI

from config import Config
from app.models.chats import Chats
from app.models.messages import Messages
from app.models.users import Users
from app.extensions import db

client = OpenAI(api_key=Config().API_KEY)
assistant_id = Config().ASSISTANT_ID
EXPERT_BOT = client.beta.assistants.retrieve(assistant_id=assistant_id)

logging.basicConfig(level=logging.DEBUG)


def get_user_chat_by_user_id(userId, product):
    chats_by_user = Chats.query.filter_by(userId=userId, product=product).all()
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


def create_user_chat_by_user_id(userId, messageContent, product, db):
    thread_id = create_thread()

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
        lastMessageId=None,
        product=product,
        thread_id=thread_id
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


def get_user_chat_by_chat_id(userId, chatId, product):
    chat = Chats.query.filter_by(userId=userId, id=chatId, product=product).first()

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


def delete_user_chat_by_chat_id(userId, chatId, product, db):
    chat = Chats.query.filter_by(userId=userId, id=chatId, product=product).first()

    chat.status = "closed"
    chat.closedAt = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    db.session.commit()


def generate_ad(messageContent, userId, chatId, product,message):
    try:
        
        print(message)
        
        # Get the content of the first message or an empty string if it's None
        first_message_content = message[0].get("content") or ""

        # Create an ad copy by concatenating it with a prefix
        ad_copy = f"Write an ad copy for: {first_message_content}"

        # Update the content of the first message with the ad copy
        
        print (message[0])
        message[0]["content"] = ad_copy

        # Assign the modified message to the variable 'messages'
        messages = message
        
        print (messages)
        
        print (message)
        
        # messages.append({"role": "user", "content": messageContent})    
        
        
        try:
            completion = client.chat.completions.create(
                model="gpt-4",
                messages=messages
            )
            
            print("here 7")

            result = completion.choices[0].message.content
            return result
        except Exception as e:
            print (e,"e")
            return {
                "status": 401,
                "message": "Unauthorized"
            }
    except Exception as e:    
        print (e,"e")
        

def get_role_and_content(userId, chatId, product):
    print("here 7")
    
    past_chat = get_user_message_by_chat_id(userId, chatId, product)
    print("here 8")
    
    messages = []

    print("here 9")
    for message in past_chat:
        role = 'assistant' if message['author'] == 'bot' else message['author']
        messages.append({"role": role, "content": message['content']})
        print("here 10")

    return messages


def generate_expert_bot_thread(messageContent, thread_id):
    try:
        message = client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=messageContent
        )

        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )

        while run.status != 'completed':
            run = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )
            time.sleep(3)

        messages = client.beta.threads.messages.list(
            thread_id=thread_id
        )

        bot_response = messages.data[0].content[0].text.value

        logging.info(f"Generated Expert Bot Thread for message: {messageContent}")
        return bot_response
    except Exception as e:
        # Log the exception for further investigation
        logging.error(f"An exception occurred: {e}")
        return {
            "status": 401,
            "message": "Unauthorized"
        }


def get_user_message_by_chat_id(userId, chatId, product):
    print("here 11", userId, chatId, product)
    chat = Chats.query.filter_by(userId=userId, id=chatId, product=product).first()
    print("here 12")
    
    messages_by_chat_id = Messages.query.filter_by(chatId=chat.id).order_by('createdAt').all()
    print("here 13")
    
    message_details = []

    for message in messages_by_chat_id:
        message_details.append({
            "id": message.id,
            "chatId": message.chatId,
            "author": message.author,
            "content": message.content,
            "createdAt": message.createdAt
        })
        print("here 14")
        
    print("here 15")

    return message_details


def create_user_message_by_chat_id(userId, chatId, messageContent, result, product, db):
    chat = Chats.query.filter_by(userId=userId, id=chatId, product=product).first()

    current_utc_datetime = datetime.now(timezone.utc)
    one_millisecond = timedelta(milliseconds=1)
    new_utc_datetime = current_utc_datetime + one_millisecond

    user_time = current_utc_datetime.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    bot_time = new_utc_datetime.replace(microsecond=0).isoformat().replace("+00:00", "Z")

    user_message = Messages(
        id=str(uuid.uuid4()),
        chatId=chat.id,
        author="user",
        content=messageContent,
        createdAt=user_time
    )

    # Logic to make sure user_message is commited before bot_message.
    
    bot_message = Messages(
        id=str(uuid.uuid4()),
        chatId=chat.id,
        author="bot",
        content=result,
        createdAt=bot_time
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


def get_user_message_by_message_id(userId, chatId, messageId, product):
    chat = Chats.query.filter_by(userId=userId, id=chatId, product=product).first()
    message = Messages.query.filter_by(id=messageId, chatId=chat.id).first()

    message_details = {
        "id": message.id,
        "chatId": message.chatId,
        "author": message.author,
        "content": message.content,
        "createdAt": message.createdAt,
    }

    return message_details


def register_new_user(user_details, db):
    try:
        user_id = user_details['id']
        user_name = user_details['name']
        user_exist = Users.query.filter_by(id=user_id).first()

        if not user_exist:
            user = Users(id=user_id, username=user_name)
            db.session.add(user)
            db.session.commit()
            logging.info(f"Registered New User :: {user_details['name']}")

        # TODO : Return user instance if already existed
        logging.info(f"User Already Existed :: {user_details['name']}")
        return {
            "status": 200,
            "message": "Success"
        }
    except Exception as e:
        logging.error(f"ERROR :: Register New User failed :: {e}")
        return {
            "status": 401,
            "message": "Unauthorized"
        }


def store_access_token_in_database(user_id, access_token):
    # Check if the user already exists in the database
    user = Users.query.filter_by(id=user_id).first()

    if user:
        # If the user exists, update the access token
        user.access_token = access_token
        db.session.commit()
        logging.info(f"Stored Access Token for user: {user_id}")
    else:
        # Handle the case where the user does not exist
        print(f"User with ID {user_id} not found in the database")
        logging.error(f"USER NOT FOUND: {user_id}")


def retrieve_access_token_from_database(user_id):
    # Retrieve the access token from the database based on the user ID
    user = Users.query.filter_by(id=user_id).first()

    if user:
        logging.info(f"Retrieved Access Token :: {user.access_token}")
        return user.access_token
    else:
        # Handle the case where the access token is not found
        print(f"Access token not found for user with ID {user_id}")
        logging.error(f"Access token not found for user with ID: {user_id}")
        return None

def experimentalResult(userId, chatId, product, messageContent,db):
        chat = Chats.query.filter_by(userId=userId, id=chatId, product=product).first()
        
        current_utc_datetime = datetime.now(timezone.utc)
        one_millisecond = timedelta(milliseconds=1)
        new_utc_datetime = current_utc_datetime + one_millisecond
        new_utc_datetime = current_utc_datetime + one_millisecond
            
        bot_time = current_utc_datetime.replace(microsecond=0).isoformat().replace("+00:00", "Z")
        bot_message = Messages(
            id=str(uuid.uuid4()),
            chatId=chat.id,
            author="bot",
            content=messageContent,
            createdAt=bot_time
        )


        db.session.add(bot_message)
        db.session.commit()
        
        print("I AM FROM RESULT")
        print(bot_message)

        return {
            "user_message": {
                "id": bot_message.id,
                "chatId": bot_message.chatId,
                "author": bot_message.author,
                "content": bot_message.content,
                "createdAt": bot_message.createdAt
            },
        }

def experimentalQuestion(userId, chatId, product, messageContent,db):
        chat = Chats.query.filter_by(userId=userId, id=chatId, product=product).first()

        current_utc_datetime = datetime.now(timezone.utc)
        one_millisecond = timedelta(milliseconds=1)
        new_utc_datetime = current_utc_datetime + one_millisecond
        new_utc_datetime = current_utc_datetime + one_millisecond
            
        user_time = current_utc_datetime.replace(microsecond=0).isoformat().replace("+00:00", "Z")

        user_message = Messages(
            id=str(uuid.uuid4()),
            chatId=chat.id,
            author="user",
            content=messageContent,
            createdAt=user_time
        )



        db.session.add(user_message)
        db.session.commit()

        return {
            "user_message": {
                "id": user_message.id,
                "chatId": user_message.chatId,
                "author": user_message.author,
                "content": user_message.content,
                "createdAt": user_message.createdAt
            },
        }

def create_thread():
    thread = client.beta.threads.create()
    return thread.id
