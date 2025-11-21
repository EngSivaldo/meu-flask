from app import create_app, db
from app.models import Produto

# Criar o app
app = create_app()

# Usar contexto do app
with app.app_context():
    # Criar tabelas no banco
    db.create_all()

    # Inserir produtos iniciais
    p1 = Produto(nome="Caneta", preco=3.5)
    p2 = Produto(nome="Caderno", preco=15.0)
    p3 = Produto(nome="Lápis", preco=2.0)

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    # Consultar produtos e mostrar no console
    produtos = Produto.query.all()
    for produto in produtos:
        print(produto)
