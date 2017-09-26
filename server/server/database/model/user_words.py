import datetime

from server.database import db
from server.database.model import DbLanguage, DbWordType, DbWord


class DbUserWord(db.Model):
    __tablename__ = 'user_words'

    id_user_word = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    id_word = db.Column(db.Integer, db.ForeignKey(DbWord.id_word), nullable=False)
    id_language = db.Column(db.Integer, db.ForeignKey(DbLanguage.id_language), nullable=False)
    id_type = db.Column(db.Integer, db.ForeignKey(DbWordType.id_type), nullable=False)

    score = db.Column(db.Integer, nullable=False, index=True)
    is_learnt = db.Column(db.Boolean, nullable=False, default=False)
    last_learn_db_dts = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<DbUserWord [{}] - score={}, is_learnt={}>'.format(self.id_user_word, self.score, self.is_learnt)
