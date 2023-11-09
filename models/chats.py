from zdai_app import  db
from sqlalchemy.orm import relationship


class Chats(db.Model):
    id = db.Column(db.String, primary_key=True)
    userId = db.Column(db.Integer)
    productId = db.Column(db.Integer)
    title = db.Column(db.String)
    status = db.Column(db.String)
    createdAt = db.Column(db.DateTime)
    postedAt = db.Column(db.DateTime)
    answeredAt = db.Column(db.DateTime)
    closedAt = db.Column(db.DateTime)
    lastMessageId = db.Column(db.String, db.ForeignKey('messages.id'))
    messages = db.Column(db.Integer)

    __tablename__ = 'chats'

# with app.app_context():
#     db.create_all()
