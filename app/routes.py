from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Produto
from app.forms import ProdutoForm, DeleteForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    produtos = Produto.query.all()
    delete_form = DeleteForm()
    return render_template('home.html', produtos=produtos, delete_form=delete_form)

# Add produto
@main.route('/add', methods=['GET', 'POST'])
def add_produto():
    form = ProdutoForm()
    if form.validate_on_submit():
        p = Produto(
            nome=form.nome.data,
            preco=form.preco.data,
            quantidade=form.quantidade.data  # <- aqui!
        )
        db.session.add(p)
        db.session.commit()
        flash("Produto adicionado com sucesso!", "success")
        return redirect(url_for("main.home"))
    return render_template("produto_form.html", form=form, titulo="Adicionar Produto")


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_produto(id):
    produto = Produto.query.get_or_404(id)
    form = ProdutoForm(obj=produto)
    if form.validate_on_submit():
        produto.nome = form.nome.data
        produto.preco = form.preco.data
        produto.quantidade = form.quantidade.data  # <- aqui!
        db.session.commit()
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for("main.home"))
    return render_template("produto_form.html", form=form, titulo="Editar Produto")


@main.route('/delete/<int:id>', methods=['POST'])
def delete_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto deletado com sucesso!', 'success')
    return redirect(url_for('main.home'))
