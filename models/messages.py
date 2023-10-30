from app import app, db


class Messages(db.Model):
    id = db.Column(db.String, primary_key=True)
    chatId = db.Column(db.String, db.ForeignKey('chats.id'))
    author = db.Column(db.String)
    content = db.Column(db.Text)
    createdAt = db.Column(db.DateTime)


with app.app_context():
    db.create_all()
