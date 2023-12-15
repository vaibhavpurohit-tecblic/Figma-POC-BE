from app.extensions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    access_token = db.Column(db.String)

    __tablename__ = 'users'

    def __repr__(self):
        return f'<User {self.username}>'
