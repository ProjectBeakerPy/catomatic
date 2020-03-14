from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import logging 

app = Flask(__name__)
app.config.from_object(Config)
app.logger.setLevel(logging.INFO)

from app import routes

if __name__ == "__main__":
    app.run(host='0.0.0.0')