from coding_edu import db


class UsersData(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
