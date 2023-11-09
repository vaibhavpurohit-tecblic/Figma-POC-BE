from zdai_app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)

    __tablename__ = 'users'


# with app.app_context():
#     db.create_all()
