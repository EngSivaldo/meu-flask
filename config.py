import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'minha_chave_secreta')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig:
    SECRET_KEY = 'teste_secreto'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # banco temporário em memória
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
