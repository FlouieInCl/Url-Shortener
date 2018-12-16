import os

from app import create_app
from app.configs import Config


if __name__ == '__main__':
    app = create_app(Config)

    if  'SECRET_KEY' not in os.environ:
        print("[WARNING] secret key isn't defined in environment")

    app.run(**app.config['RUN_SETTING'])
