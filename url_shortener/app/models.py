import datetime

from sqlalchemy.dialects.mysql import INTEGER as Integer
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UrlMappingModel(db.Model):
    __tablename__ = 'url_mapper'

    id = db.Column(Integer(unsigned=True), primary_key=True, autoincrement=True)
    original_url = db.Column(db.String(500), unique=True, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

