import pytest
from app import create_app, db
from app.models import Produto
from config import TestConfig

@pytest.fixture
def app():
    app = create_app()  # cria o app normalmente
    # sobrescreve a configuração para teste
    app.config.from_object(TestConfig)
    with app.app_context():
        db.create_all()  # cria tabelas em memória
        yield app
        db.drop_all()  # limpa tudo após o teste

@pytest.fixture
def db_session(app):
    from app import db
    yield db
    db.session.remove()

def test_criar_produto(db_session):
    p = Produto(nome="Caneta", preco=3.5)
    db_session.session.add(p)
    db_session.session.commit()

    produtos = Produto.query.all()
    assert len(produtos) == 1
    assert produtos[0].nome == "Caneta"
    assert produtos[0].preco == 3.5
