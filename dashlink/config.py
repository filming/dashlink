from dotenv import load_dotenv

import os

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # setting flask configuration values
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or f"sqlite:///{os.path.join(basedir, 'dashlink.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
