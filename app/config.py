import os

class Config:
    """Flask configuration variables"""
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:your_password@localhost/expense_tracker'
    SQLAlchemy_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    