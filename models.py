from app import app, db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)


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


class Messages(db.Model):
    id = db.Column(db.String, primary_key=True)
    chatId = db.Column(db.String, db.ForeignKey('chats.id'))
    author = db.Column(db.String)
    content = db.Column(db.Text)
    createdAt = db.Column(db.DateTime)


with app.app_context():
    db.create_all()
