from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UrlMappingModel(db.Model):
    __tablename__ = 'url_mapper'
    ...
