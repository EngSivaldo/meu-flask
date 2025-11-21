from . import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=0)  # NOVO CAMPO

    def __repr__(self):
        return f"<Produto {self.id} - {self.nome}>"
