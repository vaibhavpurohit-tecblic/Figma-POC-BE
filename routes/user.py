import uuid

from flask import Blueprint, request, jsonify

from app import db
from controllers.message import get_user_message_by_chat_id, generate_ad, create_user_message_by_chat_id, \
    get_user_message_by_message_id

user_bp = Blueprint('message', __name__)