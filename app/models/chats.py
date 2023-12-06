from app.extensions import db


class Chats(db.Model):
    id = db.Column(db.String, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    productId = db.Column(db.Integer)
    title = db.Column(db.String)
    status = db.Column(db.String)
    createdAt = db.Column(db.DateTime)
    postedAt = db.Column(db.DateTime)
    answeredAt = db.Column(db.DateTime)
    closedAt = db.Column(db.DateTime)
    lastMessageId = db.Column(db.String)
    messages = db.Column(db.Integer)
    product = db.Column(db.String)

    __tablename__ = 'chats'

    def __repr__(self):
        return f'<Chat {self.title}>'
