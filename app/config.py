import os

from dotenv import load_dotenv

load_dotenv()

class Config():
    TG_API_TOKEN = os.getenv("TG_API_TOKEN")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    UPLOAD_FOLDER = 'uploads'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
