import os


class Config:
    SERVICE_NAME = "url_shortener"
    SERVICE_NAME_UPPER = SERVICE_NAME.upper()

    HOST = 'localhost'
    PORT = 9072
    DEBUG = True
    TESTING = True

    REPRESENTATION_URL = HOST + ':' + str(PORT)

    SECRET_KEY = os.getenv('SECRET_KEY', 'lo02pfu743jjdildp20djl03kdk3iodj')

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:germany33@localhost:3306/shortener"

    RUN_SETTING = {
        'host': HOST,
        'port': PORT,
        'debug': DEBUG,
        'threaded': True
    }
