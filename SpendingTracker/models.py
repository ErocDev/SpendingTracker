from operator import itemgetter
from time import timezone
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true
from sqlalchemy.sql import func


db = SQLAlchemy()

class SpendingModel(db.Model):
    __tablename__ = "spending_table"

    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(50))
    cost = db.Column(db.Integer)
    time = db.Column(db.DateTime(timezone=True), default=func.now())


    def __repr__(self):
        return f"<Item: {self.item}> <Cost: {self.cost}>"
