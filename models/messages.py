from zdai_app import  db


class Messages(db.Model):
    id = db.Column(db.String, primary_key=True)
    chatId = db.Column(db.String, db.ForeignKey('chats.id'))
    author = db.Column(db.String)
    content = db.Column(db.Text)
    createdAt = db.Column(db.DateTime)

    __tablename__ = 'messages'


# with app.app_context():
#     db.create_all()
