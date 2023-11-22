import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Nut(SqlAlchemyBase):
    __tablename__ = 'nuts'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    mass = sqlalchemy.Column(sqlalchemy.Integer)
    discount_perc = sqlalchemy.Column(sqlalchemy.Integer)
